import discord, os
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from os.path import join
import asyncio, json, string, traceback
from dotenv import load_dotenv
load_dotenv()

from file_niizuki.scripts.convertitore import altri_nomi
from file_niizuki.scripts.tempo import ricerca_tempo
from file_niizuki.scripts.scrap import aggiorna_database

# Load database from 'mydatabase.json'
database = None

def update_database():
    try:
        print("Refresh")
        with open(join('file_niizuki', 'mydatabase.json'), 'r+') as f:
            global database
            database = json.load(f)
            return database
    except FileNotFoundError:
        print("al_ships.py: creazione file 'mydatabase.json'")
        f = open(join('file_niizuki', 'mydatabase.json'), "w")
        f.write("{\n}")
        f.close()
        database = {}
        return database
    except json.decoder.JSONDecodeError:
        print("al_ships.py: rimozione file 'mydatabase.json'")
        os.remove(join('file_niizuki', "mydatabase.json"))
        database = {}
        return database

update_database()

# Load blacklist from 'blacklist.json'
canali_extra = None

def load_blacklist():
    with open(join('file_niizuki', 'blacklist.json'), 'r+') as f:
        lista_id = json.load(f)
        global canali_extra
        canali_extra = lista_id["id_canali"]
        return canali_extra

load_blacklist()

# Controlla se esistono soprannomi della nave nel file 'convertitore.py'
class Check:
    def __init__(self, nave):
        self.nave = nave

    def controllo(self):
        if self.nave in altri_nomi:
            backup = self.nave
            for key in altri_nomi:
                backup = backup.replace(key, altri_nomi[key])
                if backup != self.nave:
                    self.nave = backup
                    break
class Nave:
    def __init__(self, nave, embed=None):
        self.nave = nave
        self.embed = embed

    def pacchetto(self):
        nave = self.nave

        #Fetch name list (skins)
        skin_list = []
        for idx, sk in enumerate(database[nave]["skin"]):
            if idx % 2 == 0:
                skin_list.append(sk)

        embed = discord.Embed(
            title = database[nave]["tempo"],
            description = f'Artista: {database[nave]["artista"]}\n' +
            f'Doppiatrice: {database[nave]["doppiatrice"]}\n\n' +
            #Info
            f'**Nazionalità:** {database[nave]["nazionalità"]} {database[nave]["abbreviazione"]}\n' +
            f'**Classe:** {database[nave]["classe"]} {database[nave]["tipo"]}\n' +
            f'**Numero ID:** {database[nave]["id"]}\n\n' +
            #Lista skin
            f'**Skin: **'+"\n".join(skin_list),
            colour = discord.Colour(database[nave]["colore_embed"]))
        #Icona nave e nome
        embed.set_author(name = database[nave]["nome_nave"] +
            " (" + database[nave]["rarità"]+")",
            url = database[nave]["wiki_nave"][0],
            icon_url = database[nave]["wiki_nave"][1])
        #Immagini e footer
        embed.set_thumbnail(url = database[nave]["wiki_nave"][2])
        embed.set_image(url = database[nave]["wiki_nave"][3])
        embed.set_footer(text = "Clicca 📖 per vedere le skill")
        #Efficienza armamento
        embed.add_field(name = "Efficienza armamento:",
            value = database[nave]["efficienza"][0] + '\n' +
        database[nave]["efficienza"][1] + '\n' +
        database[nave]["efficienza"][2], inline = False)
        #Limit Break
        embed.add_field(name = "Limit Break",
            value = database[nave]["rank"][0] + '\n' +
            database[nave]["rank"][1] + '\n' +
            database[nave]["rank"][2] + '\n' +
            database[nave]["rank"][3] + '\n' +
            database[nave]["rank"][4] + '\n' +
            database[nave]["rank"][5], inline = False)
        #Acquisizione
        embed.add_field(name = "Info:",
            value = database[nave]["acquisizione"], inline = False)
        embed.add_field(name = "Retrofit:",
            value = "Retrofit " + database[nave]["retrofit"], inline = False)
        self.embed = embed

SHIP_PREFIX = '!'
SKIN_PREFIX = 'skin!'
SEARCH_PREFIX = '%'
MERON = os.getenv("MERON")
MELONE_ID = int(MERON)

class Ships(commands.Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        global canali_extra
        msg = message.content
        channel = message.channel
        if channel.id in canali_extra:
                return
        MELONE = self.client.get_user(MELONE_ID)

        #Comando .help
        if msg.lower() == ".help":
            info = discord.Embed(
                title = "Elenco comandi disponibili:",
                description =  "**!**nave⠀→⠀info nave\n" +
                "> esempio: **!**Akashi\n \n" +
                "**skin!**nave⠀→⠀elenco skin nave \n" +
                "> esempio: **skin!**Akashi\n \n" +
                "**cat!**meowfficer⠀→⠀info meowfficer\n" +
                "> esempio: **cat!**Bishamaru\n \n" +
                "**cap!**capitolo⠀→⠀info capitolo mappa\n" +
                "> esempio: **cap!**9-4\n \n" +
                "**%**tempo di costruzione | nome nave\n" +
                "> esempio: **%**01:35:00⠀=⠀*Akashi*\n" +
                "> esempio2: **%**Sandy⠀=⠀*01:10:00*\n \n" +
                "**cat%**tempo⠀→⠀meowfficer\n" +
                "> esempio: **cat%**10:24:00⠀=⠀*Justice*",
                colour = discord.Colour.blue())

            await channel.send(embed = info)

        # Invio embed navi
        if msg.startswith(SHIP_PREFIX):
            fetch = msg.lower().split(SHIP_PREFIX)
            nave_grezza = fetch[1]

            #Fase di controllo
            richiamo = Check(nave_grezza)
            richiamo.controllo()
            nave = richiamo.nave

            if nave not in database:
                embed_nave = discord.Embed(
                    title = "Comunicazione:",
                    description = f"Niizuki non ha trovato questa nave nel database: __{nave}__\n" +
                    "𝐶-𝑐𝑜𝑚𝑎𝑛𝑑𝑎𝑛𝑡𝑒... 𝑛-𝑛𝑜𝑛 𝑡𝑖 𝑎𝑟𝑟𝑎𝑏𝑏𝑖𝑎𝑟𝑒, 𝑝𝑒𝑟 𝑓𝑎𝑣𝑜𝑟𝑒\n\n" +
                    "Usa il comando **.help** se hai bisogno di aiuto (≧ ﹏ ≦)\n" +
                    f"Oppure, prova a contattare {MELONE.mention}",
                    colour = discord.Colour.dark_green())
                embed_nave.set_footer(text="Clicca l'emoji per ricaricare il database")

                invio_embed = await channel.send(embed = embed_nave)
                await invio_embed.add_reaction(emoji = "📥")
                update_database()
            else:
                try:
                    invio = Nave(nave)
                    invio.pacchetto()
                    embed = invio.embed
                    nave_msg = await channel.send(embed = embed)
                    await nave_msg.add_reaction(emoji = "📖")
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

        # Invio skin navi
        if msg.lower().startswith(SKIN_PREFIX):
            fetch = msg.lower().split(SKIN_PREFIX)
            nave_grezza = fetch[1]

            #Fase di controllo
            richiamo = Check(nave_grezza)
            richiamo.controllo()
            nave = richiamo.nave

            if nave not in database:
                embed_skin = discord.Embed(
                    title = "Comunicazione:",
                    description = f"Non trovo nessuna skin di questa nave: __{nave}__\n" +
                    "N-non ho commesso errori, 𝑣𝑒𝑟𝑜?\n\n" +
                    "Usa il comando **.help** se hai bisogno di aiuto (≧ ﹏ ≦)\n" +
                    f"Oppure, prova a contattare {MELONE.mention}",
                    colour = discord.Colour.dark_green())
                embed_skin.set_footer(text="Clicca l'emoji per ricaricare il database")

                invio_embed = await channel.send(embed = embed_skin)
                await invio_embed.add_reaction(emoji = "📥")
                update_database()
            else:
                try:
                    embed_skin = discord.Embed(description = database[nave]["skin"][0],
                        colour = discord.Colour(database[nave]["colore_embed"]))
                    #Icona nave e nome
                    embed_skin.set_author(name = database[nave]["nome_nave"] +
                        " (" + database[nave]["rarità"]+")",
                        url = database[nave]["wiki_nave"][0],
                        icon_url = database[nave]["wiki_nave"][1])
                    #Immagini
                    embed_skin.set_thumbnail(url = database[nave]["wiki_nave"][2])
                    embed_skin.set_image(url = database[nave]["skin"][1])
                    embed_skin.set_footer(text = "Retrofit " + database[nave]["retrofit"])

                    skin_msg = await channel.send(embed = embed_skin)
                    await skin_msg.add_reaction(emoji = "⬅️")
                    await skin_msg.add_reaction(emoji = "➡️")
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

        # Cerca navi per tempo di costruzione
        if msg.lower().startswith(SEARCH_PREFIX):
            fetch = msg.lower().split(SEARCH_PREFIX)
            time_or_name = fetch[1]

            if time_or_name in ricerca_tempo:
                numero_navi = 0
                elementi = []
                for nave in database:
                    if database[nave]["tempo"] == ricerca_tempo[time_or_name]["tag"]:
                        if database[nave]["limited"] == "sì":
                            elementi.append(f'{database[nave]["nome_nave"]} {database[nave]["abbreviazione"]} **limited**')
                            numero_navi += 1
                        elif database[nave]["collab"] == "sì":
                            elementi.append(f'{database[nave]["nome_nave"]} {database[nave]["abbreviazione"]} **collab**')
                            numero_navi += 1
                        else:
                            elementi.append(f'{database[nave]["nome_nave"]} {database[nave]["abbreviazione"]}')
                            numero_navi += 1

                await channel.send(embed = discord.Embed(
                    title = "Navi disponibili nel database: %d" % numero_navi,
                    description = "\n".join(elementi),
                    colour = discord.Colour.green()))
            elif time_or_name in database or altri_nomi:
                try:
                    if time_or_name in altri_nomi:
                        backup = time_or_name
                        for key in altri_nomi:
                            backup = backup.replace(key, altri_nomi[key])
                            if backup != time_or_name:
                                time_or_name = backup
                                break 
                        
                    if database[time_or_name]["limited"] == "sì":
                        tempo = f'[__{database[time_or_name]["tempo"]}__] **limited**'
                    elif database[time_or_name]["collab"] == "sì":
                        tempo = f'[__{database[time_or_name]["tempo"]}__] **collab**'
                    else:
                        tempo = f'[__{database[time_or_name]["tempo"]}__]'

                    await channel.send(embed = discord.Embed(
                        title = "Tempo di costruzione",
                        description = f'{database[time_or_name]["nome_nave"]} {tempo}',
                        colour = discord.Colour.green()))
                except Exception:
                    out = time_or_name.translate(str.maketrans("", "", string.punctuation))
                    if out.isdigit() is False:
                        await channel.send(embed = discord.Embed(
                            title = "Comunicazione:",
                            description = f"Niizuki non ha trovato questa nave nel database: __{time_or_name}__\n" +
                            "𝐶-𝑐𝑜𝑚𝑎𝑛𝑑𝑎𝑛𝑡𝑒... 𝑛-𝑛𝑜𝑛 𝑡𝑖 𝑎𝑟𝑟𝑎𝑏𝑏𝑖𝑎𝑟𝑒, 𝑝𝑒𝑟 𝑓𝑎𝑣𝑜𝑟𝑒\n\n" +
                            "Usa il comando **.help** se hai bisogno di aiuto (≧ ﹏ ≦)\n" +
                            f"Oppure, prova a contattare {MELONE.mention}",
                            colour = discord.Colour.dark_green()))

def setup(client):
    client.add_cog(Ships(client))