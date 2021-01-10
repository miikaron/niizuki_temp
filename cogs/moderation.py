import discord, os
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from os.path import join
import asyncio, json, traceback
from dotenv import load_dotenv
load_dotenv()

from cogs.al_ships import update_database
from cogs.al_ships import load_blacklist
from file_niizuki.scripts.scrap import aggiorna_database

MERON = os.getenv("MERON")
CANALE_LOG = os.getenv("CANALE_LOG")
MELONE_ID = int(MERON)
ID_CANALE_LOG = int(CANALE_LOG)

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx):
        channel = ctx.channel

        await ctx.message.delete()
        args = ctx.message.content.split()
        testo = " ".join(args[1:])

        await channel.trigger_typing()
        await asyncio.sleep(1)
        await channel.send(testo)

        MELONE = self.client.get_user(MELONE_ID)
        if not ctx.message.author.id == MELONE.id:
            indirizzo_log = self.client.get_channel(ID_CANALE_LOG)
            await indirizzo_log.send(testo + f' (Inviato da: **{ctx.message.author}**, canale **#{channel}**, comando: **testo**)')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def embed(self, ctx):
        channel = ctx.channel

        await ctx.message.delete()
        args = ctx.message.content.split()
        embed = discord.Embed(description = " ".join(args[1:]),
            colour = discord.Colour.green())

        await channel.trigger_typing()
        await asyncio.sleep(1)
        await channel.send(embed = embed)

        MELONE = self.client.get_user(MELONE_ID)
        if not ctx.message.author.id == MELONE.id:
            indirizzo_log = self.client.get_channel(ID_CANALE_LOG)
            await indirizzo_log.send(embed + f' (Inviato da: **{ctx.message.author}**, canale **#{channel}**, comando: **embed**)')
    
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True, manage_channels=True)
    async def blacklist_show(self, ctx):
        lista_id = []
        nomi_canali = [] 

        with open(join('file_niizuki', 'blacklist.json'), 'r') as f:
            data = json.load(f)
            canali_extra = data["id_canali"]
            for id_canale in canali_extra:
                lista_id.append(id_canale)

            for id_canale in lista_id:
                canale = self.client.get_channel(id_canale)
                if canale and canale.guild == ctx.channel.guild:
                    nomi_canali.append(f"**{canale.name}** | ID canale | *{id_canale}*")
            descrizione_embed = "\n".join(nomi_canali)

        if not nomi_canali:
            descrizione_embed = "Non ci sono canali nella blacklist"
            
        await ctx.channel.send(embed = discord.Embed(
            title = "Canali in blacklist:",
            description = descrizione_embed,
            colour = discord.Colour.purple()))

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True, manage_channels=True)
    async def blacklist_add(self, ctx):
        channel = ctx.channel
        args = ctx.message.content.split()
        STOP = False

        try:
            channel_id = args[1]
            blacklisted_channel = self.client.get_channel(int(channel_id))

            if blacklisted_channel:
                with open(join('file_niizuki', 'blacklist.json'), 'r') as infile:
                    lines = []
                    for line in infile:
                        if channel_id in line:
                            STOP = True
                        if not line.isspace():
                            lines.append(line)
                if STOP is False:
                    with open(join('file_niizuki', 'blacklist.json'), 'w') as f:
                        lines[-2] = lines[-2].strip() + ","
                        lines[-1] = "\n"+channel_id
                        lines.append("\n]}")
                        for line in lines:
                            f.write(line)

                    id_added = await channel.send(embed = discord.Embed(
                        description = "L'ID del canale è stato aggiunto correttamente",
                        colour = discord.Colour.purple()))
                    await id_added.delete(delay=5)

                    load_blacklist() # Imported
                else:
                    duplicated_id = await channel.send(embed = discord.Embed(
                        description = "L'ID del canale è già presente nella blacklist",
                        colour = discord.Colour.purple()))
                    await duplicated_id.delete(delay=5)
            else:
                await channel.send(embed = discord.Embed(
                description = "Inserisci un ID valido",
                colour = discord.Colour.purple()))
        except (ValueError, IndexError):
            await channel.send(embed = discord.Embed(
                description = "Inserisci un ID valido",
                colour = discord.Colour.purple()))
        except Exception:
            print(traceback.format_exc())

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True, manage_channels=True)
    async def blacklist_remove(self, ctx):
        channel = ctx.channel
        args = ctx.message.content.split()

        try:
            channel_id = args[1]
            send_message = False

            with open(join('file_niizuki', 'blacklist.json'), 'r') as f:
                lines = f.readlines()
            with open(join('file_niizuki', 'blacklist.json'), 'w') as f:
                out_lines = []
                for line in lines:
                    if line.strip(",\n") != channel_id:
                        out_lines.append(line)
                    else:
                        send_message = True

                if out_lines[-2].rstrip().endswith(","):
                    out_lines[-2] = out_lines[-2].rstrip().replace(",", "\n")

                for line in out_lines:
                    f.write(line)

                if send_message:
                    is_removed = await channel.send(embed = discord.Embed(
                        description = "L'ID del canale è stato rimosso correttamente",
                        colour = discord.Colour.purple()))
                    await is_removed.delete(delay=5)
                else:
                    not_found = await channel.send(embed = discord.Embed(
                        description = "L'ID del canale non è presente nella blacklist",
                        colour = discord.Colour.purple()))
                    await not_found.delete(delay=5)

            load_blacklist() # Imported
        except (ValueError, IndexError):
            await channel.send(embed = discord.Embed(
                description = "Inserisci un ID valido",
                colour = discord.Colour.purple()))
        except Exception:
            print(traceback.format_exc())
    
    @commands.command()
    @commands.guild_only()
    async def get_blacklist(self, ctx):
        channel = ctx.channel

        if ctx.author.id == MELONE_ID:
            upload_database = await channel.send(file=discord.File(os.path.join('file_niizuki', "blacklist.json")))
            await ctx.message.delete(delay=3)
            await upload_database.delete(delay=5)
    
    @commands.command()
    @commands.guild_only()
    async def get_database(self, ctx):
        channel = ctx.channel

        if ctx.author.id == MELONE_ID:
            upload_database = await channel.send(file=discord.File(os.path.join('file_niizuki', "mydatabase.json")))
            await ctx.message.delete(delay=3)
            await upload_database.delete(delay=5)
    
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role("Niizuki's database", "Admin", "Moderatore Senior")
    async def aggiorna_database(self, ctx):
        channel = ctx.channel
        
        update = discord.Embed(title="Attenzione:",
            description = f"{ctx.author.mention} ha avviato l'aggiornamento del database!",
            colour = discord.Colour.dark_blue())
        update.set_image(url = ctx.author.avatar_url)
        update.set_footer(text = "Pronto tra circa 12 minuti...")

        await channel.send(embed = update)

        await channel.send("**Si prega di non usare il bot durante l'aggiornamento. Grazie per la comprensione**")
        print("Aggiornamento avviato da Melone")

        aggiorna_database() # Imported
        update_database() # Imported

        await channel.send(embed = discord.Embed(
            description = "Aggiornamento terminato",
            colour = discord.Colour.purple()))

def setup(client):
    client.add_cog(Moderation(client))