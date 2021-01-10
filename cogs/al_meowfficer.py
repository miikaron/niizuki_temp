import discord, os
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from os.path import join
import asyncio, traceback
from dotenv import load_dotenv
load_dotenv()

from file_niizuki.scripts.tempo import ricerca_tempo_gatte
from file_niizuki.scripts.catdatabase import catdatabase

class Gatta:
    def __init__(self, gatta, embed=None):
        self.gatta = gatta
        self.embed = embed

    def pacchetto_gatta(self):
        gatta = self.gatta
        embed = discord.Embed(
            title = catdatabase[gatta]["tempo_gatta"],
            description = "**Nazionalità:** " + catdatabase[gatta]["esteso_gatta"] + " " +
            catdatabase[gatta]["nazionalità_gatta"] + '\n' +
            "**Meowfficer: **" + catdatabase[gatta]["wiki_gatta"][4],
            colour = discord.Colour(catdatabase[gatta]["colore_gatta"]))
        #Icona nave e nome
        embed.set_author(name = catdatabase[gatta]["nome_gatta"] +
            " " + catdatabase[gatta]["rarità_gatta"],
            url = catdatabase[gatta]["wiki_gatta"][0],
            icon_url = catdatabase[gatta]["wiki_gatta"][1])
        #Immagini e footer
        embed.set_thumbnail(url = catdatabase[gatta]["wiki_gatta"][2])
        embed.set_image(url = catdatabase[gatta]["wiki_gatta"][3])
        embed.set_footer(text = catdatabase[gatta]["acquisizione_gatta"])
        #Stat
        embed.add_field(name = "Stat:",
            value = "**Support:** " + catdatabase[gatta]["stat_gatta"][0] + '\n' +
            "**Command:** " + catdatabase[gatta]["stat_gatta"][1] + '\n' +
            "**Tactics:** " + catdatabase[gatta]["stat_gatta"][2], inline = False)
        #Skill
        embed.add_field(name = "Skill:",
            value = catdatabase[gatta]["skill_gatta"][0], inline = False)
        #Condition
        embed.add_field(name = "Condizioni:",
            value = "1) " + catdatabase[gatta]["condition"][0] + '\n' +
        "2) " + catdatabase[gatta]["condition"][1] + '\n' +
        "3)  " + catdatabase[gatta]["condition"][2], inline = False)
        #Effect
        embed.add_field(name = "Effetto:",
            value = "1) " + catdatabase[gatta]["effect"][0] + '\n' +
            "2) " + catdatabase[gatta]["effect"][1] + '\n' +
            "3) " + catdatabase[gatta]["effect"][2], inline = False)
        self.embed = embed

CAT_PREFIX = 'cat!'
SEARCH_CAT_PREFIX = 'cat%'
MERON = os.getenv("MERON")
MELONE_ID = int(MERON)

class Cats(commands.Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        msg = message.content
        channel = message.channel
        MELONE = self.client.get_user(MELONE_ID)

        # Invio embed meowfficer
        if msg.lower().startswith(CAT_PREFIX):
            fetch = msg.lower().split(CAT_PREFIX)
            gatta = fetch[1]
    
            if gatta not in catdatabase:
                await channel.send(embed = discord.Embed(
                    title = "Comunicazione:",
                    description = f"Niizuki non ha trovato questa meowfficer nel database: __{gatta}__\n" +
                    "𝐶-𝑐𝑜𝑚𝑎𝑛𝑑𝑎𝑛𝑡𝑒... 𝑛-𝑛𝑜𝑛 𝑡𝑖 𝑎𝑟𝑟𝑎𝑏𝑏𝑖𝑎𝑟𝑒, 𝑝𝑒𝑟 𝑓𝑎𝑣𝑜𝑟𝑒\n_ _\n" +
                    "Usa il comando **.help** se hai bisogno di aiuto (≧ ﹏ ≦)\n" +
                    f"Oppure, prova a contattare {MELONE.mention}",
                    colour = discord.Colour.dark_green()))
            else:
                try:
                    invio = Gatta(gatta)
                    invio.pacchetto_gatta()
                    embed = invio.embed
                    await channel.send(embed = embed)
                except Exception as e:
                    embed_errore = discord.Embed(
                        title = "Ops...",
                        description = f'È apparso un errore selvatico: {e}',
                        colour = discord.Colour.red())
                    embed_errore.set_image(url = "attachment://ops.gif")
                    embed_errore.set_footer(text = MELONE.name+" arriverà fra breve, forse", icon_url = MELONE.avatar_url)

                    await channel.send(f'{MELONE.mention}')
                    img_path = os.path.join('file_niizuki', 'images')
                    await channel.send(file=discord.File(os.path.join(img_path, "ops.gif")), embed=embed_errore)
                    print(traceback.format_exc())
        
        # Cerca gatti per tempo di costruzione
        if msg.lower().startswith(SEARCH_CAT_PREFIX):
            fetch = msg.lower().split(SEARCH_CAT_PREFIX)
            cat_time = fetch[1]

            if cat_time in ricerca_tempo_gatte:
                numero_gatte = 0
                elementi = []
                for cat_name in catdatabase:
                    if catdatabase[cat_name]["tempo_gatta"] == ricerca_tempo_gatte[cat_time]["tag"]:
                        if catdatabase[cat_name]["rarità_gatta"] == "(Super Rare)":
                            elementi.append(f'{cat_name} [SR] {catdatabase[cat_name]["nazionalità_gatta"]}')
                            numero_gatte += 1
                        else:
                            elementi.append(f'{cat_name} {catdatabase[cat_name]["nazionalità_gatta"]}')
                            numero_gatte += 1

                risultato = discord.Embed(
                    title = "Meowfficer disponibili nel database: %d" % numero_gatte,
                    description = "\n".join(elementi),
                    colour = discord.Colour.green())
                risultato.set_image(url = catdatabase[cat_name]["wiki_gatta"][3])

                await channel.send(embed = risultato)

def setup(client):
    client.add_cog(Cats(client))