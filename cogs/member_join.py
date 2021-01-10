import discord, os
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from os.path import join, dirname
import asyncio, traceback
from dotenv import load_dotenv
load_dotenv()

class Join(commands.Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_member_join(self, member):
        fetch = self.client.get_channel(710166892475842663)
        if fetch:
            ROLE_CHANNEL = fetch.name
        else:
            ROLE_CHANNEL = "<Error>"

        EMBED_DESCRIPTION = [
            #ITA
            "Benvenuto/a nel server",
            #EN
            "We wish you a pleasant stay!",
        ]

        EMBED_FOOTER = [
            #Azur Lane IT
            "Ti auguro una buona permanenza nel server!",
            #C.I.I. ITA
            "Click the emoji to change the language of the message to English",
            #C.I.I. EN
            "We wish you a pleasant stay!",
            ]

        EMBED_FIELD_NAME = [
            #ITA
            "Istruzioni per accedere al server:",
            #EN
            "Important:",
            ]

        EMBED_FIELD_VALUE = [
            #Azur Lane IT
            "Ricordati di consultare il canale **regolamento**.\n__ __\nPer ulteriori chiarimenti, tagga uno degli amministratori/moderatori",
            #C.I.I. ITA
            "Dai un'occhiata al canale **"+ROLE_CHANNEL+"** per scegliere un ruolo e vedere gli altri canali del server ^^ \
            \n\nPer ulteriori chiarimenti, tagga uno degli admin/moderatori\n\n Ti auguro una buona permanenza nel server!",
            #C.I.I. EN
            "Choose a role from the channel **"+ROLE_CHANNEL+"** to gain access to the rest of the server ^^ \
            \n\nFor further clarification, tag an admin or a moderator.",
            ]

        #Default values
        DESCRIPTION = EMBED_DESCRIPTION[0]
        FOOTER = EMBED_FOOTER[0]
        FIELD_NAME = EMBED_FIELD_NAME[0]
        FIELD_VALUE = EMBED_FIELD_VALUE[0]

        #Default embed: 'welcome'
        welcome = discord.Embed(
            description=f'{member.mention} ||{member}||\n'+DESCRIPTION+f' **{member.guild.name}**',
            colour = discord.Colour.green())
        welcome.set_image(url = "attachment://welkum.png")
        welcome.set_footer(text = FOOTER)
        welcome.add_field(name = FIELD_NAME, value = FIELD_VALUE)

        #Check member server ID and send embed
        SERV_ID = os.getenv("SERV_ID")
        if member.guild.id == int(SERV_ID): #C.I.I.
            try:
                FOOTER = EMBED_FOOTER[1]
                FIELD_NAME = EMBED_FIELD_NAME[1]
                FIELD_VALUE = EMBED_FIELD_VALUE[1]
                channel = self.client.get_channel(552571690589225017)  #ID canale: #generale
                
                #Embed: welcome_ita
                welcome_ita = discord.Embed(
                    description=f'{member.mention} ||{member}||\n'+DESCRIPTION+f' **{member.guild.name}**',
                    colour = discord.Colour.green())
                welcome_ita.set_image(url = "attachment://welkum.png")
                welcome_ita.set_footer(text = FOOTER)
                welcome_ita.add_field(name = FIELD_NAME, value = FIELD_VALUE)

                img_path = os.path.join('file_niizuki', 'images')
                benvenuto = await channel.send(file=discord.File(os.path.join(img_path, "ops.gif")), embed=welcome_ita)
                await benvenuto.add_reaction(emoji="\U0001F530")

                #Check reaction
                await self.client.wait_for('reaction_add', check=lambda r, u: str(r.emoji)=="\U0001F530" and u==member)

                #Change language to English
                DESCRIPTION = EMBED_DESCRIPTION[1]
                FOOTER = EMBED_FOOTER[2]
                FIELD_NAME = EMBED_FIELD_NAME[1]
                FIELD_VALUE = EMBED_FIELD_VALUE[2]

                welcome_en = discord.Embed(
                    description=f'{member.mention} ||{member}||\n'+DESCRIPTION+f' **{member.guild.name}**',
                    colour = discord.Colour.green())
                welcome_en.set_image(url = "attachment://welkum.png")
                welcome_en.set_footer(text = FOOTER)
                welcome_en.add_field(name = FIELD_NAME, value = FIELD_VALUE)
                
                await benvenuto.edit(embed = welcome_en)
            except Exception:
                print(traceback.format_exc())
        else:
            try:
                channel = get(member.guild.channels, name="welcome")

                img_path = os.path.join('file_niizuki', 'images')
                await channel.send(file=discord.File(os.path.join(img_path, "ops.gif")), embed=welcome)
            except Exception:
                print(traceback.format_exc())

def setup(client):
    client.add_cog(Join(client))