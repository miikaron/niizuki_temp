import discord, os
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from pathlib import Path
from os.path import join
import asyncio, traceback
from dotenv import load_dotenv
load_dotenv()

from file_niizuki.scripts.mappe import campagna

MAP_PREFIX = 'cap!'
MERON = os.getenv("MERON")
MELONE_ID = int(MERON)

class Maps(commands.Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        msg = message.content
        channel = message.channel
        MELONE = self.client.get_user(MELONE_ID)

        # Invio embed mappa
        if msg.lower().startswith(MAP_PREFIX):
            fetch = msg.lower().split(MAP_PREFIX)
            mappa = fetch[1]

            if mappa not in campagna:
                await channel.send(embed = discord.Embed(
                    title = "Comunicazione:",
                    description = f"Niizuki non ha trovato questa mappa nel database: __{mappa}__\n_ _\n" +
                    "Usa il comando **.help** se hai bisogno di aiuto (≧ ﹏ ≦)" + '\n' +
                    f"Oppure, prova a contattare {MELONE.mention}",
                    colour = discord.Colour.dark_green()))
            else:
                try:
                    if campagna[mappa]["footer"] == "sì":
                        testo = "Completa la mappa facendo 3 stelle per sbloccare la modalità Hard"
                        nemici_hard = f'Hard: {campagna[mappa]["livello_nemici_hard"]}\n'
                        boss_hard = f'Hard: {campagna[mappa]["livello_boss_hard"]}\n'
                    else:
                        testo = " "
                        nemici_hard = " "
                        boss_hard = " "

                    embed = discord.Embed(description =
                        f'Requisiti per sbloccare la mappa: \nQG lv. {campagna[mappa]["requisiti"]}',
                        colour = discord.Colour.green())
                    embed.set_author(name = campagna[mappa]["nome"],
                        url = "https://azurlane.koumakan.jp/" + mappa,
                        icon_url = "https://azurlane.koumakan.jp/w/images/a/aa/Home_head_sortie.png")
                    #Immagini e footer
                    embed.set_thumbnail(url = campagna[mappa]["wiki_nave"][1])
                    embed.set_image(url = f'attachment://{campagna[mappa]["wiki_nave"][0]}.PNG')
                    embed.set_footer(text = testo)
                    #Informazioni
                    embed.add_field(name = "Infomazioni mappa", value =
                        f'**Livello dei nemici:** {campagna[mappa]["livello_nemici"]}\n' + nemici_hard +
                        f'**Boss:** {campagna[mappa]["boss"]} liv. {campagna[mappa]["livello_boss"]}\n' + boss_hard +
                        f'\n**Posizione boss:** {campagna[mappa]["posizione"]}\n' +
                        f'Battaglie necessarie per incontrare il boss: {campagna[mappa]["battaglie"][0]}\n' +
                        f'Run necessari per completare la mappa: {campagna[mappa]["battaglie"][1]}\n' +
                        f'\n**Ricompensa 3 stelle:**\n{campagna[mappa]["ricompensa"]}', inline = False)

                    node_img_path = os.path.join("file_niizuki", "al_node_map")
                    await channel.send(file=discord.File(os.path.join(node_img_path, f'{campagna[mappa]["wiki_nave"][0]}.PNG')), embed=embed)
                except Exception as e:
                    embed_errore = discord.Embed(
                        title = "Ops...",
                        description = f'È apparso un errore selvatico: {e}',
                        colour = discord.Colour.red())
                    embed_errore.set_image(url = "attachment://ops.gif")
                    embed_errore.set_footer(text = MELONE.name+" arriverà fra breve, forse", icon_url = MELONE.avatar_url)

                    await channel.send(f'{MELONE.mention}')
                    img_path = os.path.join("file_niizuki", "images")
                    await channel.send(file=discord.File(os.path.join(img_path, "ops.gif")), embed=embed_errore)
                    print(traceback.format_exc())

def setup(client):
    client.add_cog(Maps(client))

if __name__ == "__main__":
    path = Path(__file__)
    os.chdir(path.parents[1])
    print(os.getcwd())
