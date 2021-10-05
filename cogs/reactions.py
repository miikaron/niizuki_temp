import discord, os
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from os.path import join, dirname
import asyncio, json, traceback

database = None

# Load database from 'mydatabase.json'
def refresh_database():
    try:
        with open(join('file_niizuki', 'mydatabase.json'), 'r+') as f:
            global database
            database = json.load(f)
            return database
    except FileNotFoundError:
        print("reaction.py: file not found: 'mydatabase.json'")
    except json.decoder.JSONDecodeError:
        print("reaction.py: format error: 'mydatabase.json'")

refresh_database()

NII_ROLE = os.getenv("ROLE_NAME")
MERON = os.getenv("MERON")
MELONE_ID = int(MERON)

class Reaction(commands.Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_raw_reaction_add(self, payload):
        utente = self.client.get_user(payload.user_id)
        if payload.user_id == self.client.user.id or utente.bot:
            return
        try:
            channel = self.client.get_channel(payload.channel_id)
            reaction_message = await channel.fetch_message(payload.message_id)
        except Exception:
            print(traceback.format_exc())
            return

        # Moderation: 'spoiler'
        if str(payload.emoji) == "🏴":
            for reaction in reaction_message.reactions:
                users = await reaction.users().flatten()
            user = users[0]
            membro = await channel.guild.fetch_member(user.id)

            if NII_ROLE in [role.name.lower() for role in membro.roles] or user.id == MELONE_ID:
                if reaction_message.attachments:
                    attachment_list = [attachment for attachment in reaction_message.attachments]
                    try:
                        # Folder path
                        PATH = join('file_niizuki', 'spoiler_flag')
                        attachments_author_id = []

                        for attachment in attachment_list:
                            if not attachment.is_spoiler():
                                # Save attachment
                                spoiler_image = f'SPOILER_{reaction_message.author.name}_{attachment.filename}'
                                await attachment.save(os.path.join(PATH, spoiler_image))
                                # Send warning
                                if reaction_message.author.id not in attachments_author_id:
                                    await channel.send(embed = discord.Embed(
                                        description = f"<@{reaction_message.author.id}> ***metti lo spoiler!***\nDa: ||{user.name}||",
                                        colour = discord.Colour.purple()))
                                    attachments_author_id.append(reaction_message.author.id)
                                # Send text of attachment
                                if reaction_message.content:
                                    await channel.send(f"**{reaction_message.author.name}**: {reaction_message.content}") 
                                # Delete attachment
                                await reaction_message.delete(delay=1)

                        attachments_author_id.clear()
                        # Send files
                        for image in os.listdir(PATH):
                            if image.endswith(".txt") is False:
                                sent = await channel.send(file=discord.File(os.path.join(PATH, image)))
                                if sent:
                                    os.remove(os.path.join(PATH, image))
                    except Exception as e:
                        await channel.send(embed = discord.Embed(
                            description = f'Flag: {e}',
                            colour = discord.Colour.red()))

        # Azur Lane
        if reaction_message.author == self.client.user:
            embed_obj = reaction_message.embeds

            #Browse ship skins
            if str(payload.emoji) == "➡️" or str(payload.emoji) == "⬅️":
                try:
                    for emb in embed_obj:
                        NAVE = emb.author.name.split(" (", 1)[0].lower()    #Fetch ship's name from embed
                        SKIN = emb.description                              #Fetch skin name from embed

                        skin_name_list = []
                        for skin in database[NAVE]["skin"]:
                            if skin != " ":
                                skin_name_list.append(skin)

                        for name in skin_name_list:  
                            if name == SKIN:
                                skin_name_idx = skin_name_list.index(name)

                                skin_name = skin_name_list[0]
                                url_skin = skin_name_list[1]
            
                                #Next skin
                                if str(payload.emoji) == "➡️":
                                    try:
                                        if skin_name_idx < len(skin_name_list)-2:
                                            skin_name = skin_name_list[skin_name_idx+2]
                                            url_skin = skin_name_list[skin_name_idx+3]
                                        else:
                                            skin_name = skin_name_list[0]
                                            url_skin = skin_name_list[1]
                                    except Exception:
                                        print(traceback.format_exc())
                                        skin_name = skin_name_list[0]
                                        url_skin = skin_name_list[1] 

                                #Previous skin
                                elif str(payload.emoji) == "⬅️":
                                    try:
                                        if skin_name_idx > 0:
                                            skin_name = skin_name_list[skin_name_idx-2]
                                            url_skin = skin_name_list[skin_name_idx-1]
                                        else:
                                            skin_name = skin_name_list[len(skin_name_list)-2]
                                            url_skin = skin_name_list[len(skin_name_list)-1]
                                    except Exception:
                                        print(traceback.format_exc())
                                        skin_name = skin_name_list[len(skin_name_list)-2]
                                        url_skin = skin_name_list[len(skin_name_list)-1]

                                new_embed = discord.Embed(description = skin_name,
                                    colour = discord.Colour(database[NAVE]["colore_embed"]))
                                #Icona nave e nome
                                new_embed.set_author(name = database[NAVE]["nome_nave"],
                                    url = database[NAVE]["wiki_nave"][0],
                                    icon_url = database[NAVE]["wiki_nave"][2])
                                #Immagini
                                new_embed.set_thumbnail(url = database[NAVE]["wiki_nave"][1])
                                new_embed.set_image(url = url_skin)
                                new_embed.set_footer(text = "Retrofit " + database[NAVE]["retrofit"])
                                
                                await reaction_message.edit(embed=new_embed)
                except Exception:
                    print(traceback.format_exc())
                    refresh_database()
            
            #Change embed page (Limit Break | Skills)  
            if str(payload.emoji) == "📖":         
                try: 
                    for emb in embed_obj:
                        NAVE = emb.author.name.split(" (", 1)[0].lower()    #Fetch ship's name from embed
                        TEMPO = "**"+database[NAVE]["tempo"]+"**"           #Check

                        # Check if page is "main page"
                        if emb.description != TEMPO:
                            new_embed = discord.Embed(description = TEMPO,
                                colour = discord.Colour(database[NAVE]["colore_embed"]))
                            #Icona nave e nome
                            new_embed.set_author(name = database[NAVE]["nome_nave"],
                                url = database[NAVE]["wiki_nave"][0],
                                icon_url = database[NAVE]["wiki_nave"][2])
                            #Immagini e footer
                            new_embed.set_thumbnail(url = database[NAVE]["wiki_nave"][1])
                            new_embed.set_image(url = database[NAVE]["wiki_nave"][2])
                            new_embed.set_footer(text = "Clicca 📖 per tornare indietro")
                            #Skill 1 -> database[NAVE]["skill"][0].split("\n") [0]=title [1]=descritpion
                            new_embed.add_field(name = database[NAVE]["skill"][0].split("\n")[0],
                                value = database[NAVE]["skill"][0].split("\n")[1], inline = False)
                            #Skill 2
                            if database[NAVE]["skill"][1].isspace() == False:
                                new_embed.add_field(name = database[NAVE]["skill"][1].split("\n")[0],
                                    value = database[NAVE]["skill"][1].split("\n")[1], inline = False)
                            #Skill 3
                            if database[NAVE]["skill"][2].isspace() == False:
                                new_embed.add_field(name = database[NAVE]["skill"][2].split("\n")[0],
                                    value = database[NAVE]["skill"][2].split("\n")[1], inline = False)
                            #Skill 4
                            if database[NAVE]["skill"][3].isspace() == False:
                                new_embed.add_field(name = database[NAVE]["skill"][3].split("\n")[0],
                                    value = database[NAVE]["skill"][3].split("\n")[1], inline = False)
                            #Skill 5
                            if database[NAVE]["skill"][4].isspace() == False:
                                new_embed.add_field(name = database[NAVE]["skill"][4].split("\n")[0],
                                    value = database[NAVE]["skill"][4].split("\n")[1], inline = False)
                            new_embed.add_field(name = "Retrofit:",
                                value = "Retrofit " + database[NAVE]["retrofit"], inline = False)  
                        else:
                            #Fetch name list (skins)
                            skin_list = []
                            for idx, skin in enumerate(database[NAVE]["skin"]):
                                if idx % 2 == 0:
                                    skin_list.append(skin)

                            #Return to "main page"
                            new_embed = discord.Embed(title = database[NAVE]["tempo"],
                                description = "**Nazionalità:** " + database[NAVE]["nazionalità"] + " " +
                                database[NAVE]["abbreviazione"] + '\n' +
                                "**Tipo:** " + database[NAVE]["tipo"] +'\n' +
                                "_ _" + '\n' +
                                "**Skin: ** " + "\n".join(skin_list),
                                colour = discord.Colour(database[NAVE]["colore_embed"]))
                            #Icona nave e nome
                            new_embed.set_author(name = database[NAVE]["nome_nave"],
                                url = database[NAVE]["wiki_nave"][0],
                                icon_url = database[NAVE]["wiki_nave"][2])
                            #Immagini e footer
                            new_embed.set_thumbnail(url = database[NAVE]["wiki_nave"][1])
                            new_embed.set_image(url = database[NAVE]["wiki_nave"][2])
                            new_embed.set_footer(text = "Clicca 📖 per vedere le skill")
                            #Efficienza armamento
                            new_embed.add_field(name = "Efficienza armamento:",
                                value = database[NAVE]["efficienza"][0] + '\n' +
                                database[NAVE]["efficienza"][1] + '\n' +
                                database[NAVE]["efficienza"][2], inline = False)
                            #Limit Break
                            new_embed.add_field(name = "Limit Break",
                                value = database[NAVE]["rank"][0] + '\n' +
                                database[NAVE]["rank"][1] + '\n' +
                                database[NAVE]["rank"][2] + '\n' +
                                database[NAVE]["rank"][3] + '\n' +
                                database[NAVE]["rank"][4] + '\n' +
                                database[NAVE]["rank"][5], inline = False)
                            #Acquisizione
                            new_embed.add_field(name = "Info:",
                                value = database[NAVE]["acquisizione"], inline = False)
                            new_embed.add_field(name = "Retrofit:",
                                value = "Retrofit " + database[NAVE]["retrofit"], inline = False)   

                        await reaction_message.edit(embed=new_embed)
                except (IndexError, KeyError, TypeError):
                    refresh_database()
                except Exception:
                    print(traceback.format_exc())

def setup(client):
    client.add_cog(Reaction(client))