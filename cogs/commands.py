import discord, os
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from os.path import join
import asyncio, json, traceback, pytz, time
from datetime import datetime, timezone
from dotenv import load_dotenv
load_dotenv()

from cogs.al_ships import update_database
from cogs.al_ships import load_blacklist
from file_niizuki.scripts.scrap import aggiorna_database

MERON = os.getenv("MERON")
NAEGI = os.getenv("NAEGI")
CANALE_LOG = os.getenv("CANALE_LOG")
MELONE_ID = int(MERON)
NAEGI_ID = int(NAEGI)
ID_CANALE_LOG = int(CANALE_LOG)

async def is_owner(ctx):
    return ctx.author.id == MELONE_ID or ctx.author.id == NAEGI_ID

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(send_messages=True)
    async def help(self, ctx):
        channel = ctx.channel

        default = discord.Embed(
            title = "Comandi speciali disponibili:",
            description = f"• Prefissi_bot disponibili:⠀**--**⠀⠀**-!**\n\n" +
            f"Prefisso_bot + **sanity** + [**sanity**] [**limite sanity** (facoltativo)]\n> permessi richiesti: avere il ruolo 'Arknights'\n" +
            f"Prefisso_bot + **say** + __testo_da_inviare__\n> permessi richiesti: gestire i messaggi\n" +
            f"Prefisso_bot + **embed** + __testo_da_inviare__\n> permessi richiesti: gestire i messaggi\n" +
            f"Prefisso_bot + **clear** + __numero messaggi da eliminare__ [max 30]\n> permessi richiesti: essere moderatore senior\n" +
            f"Prefisso_bot + **blacklist_show** [mostra canali nella blacklist]\n> permessi richiesti: essere moderatore\n" +
            f"Prefisso_bot + **blacklist_add** + __ID canale da aggiungere__\n> permessi richiesti: essere moderatore\n" +
            f"Prefisso_bot + **blacklist_remove** + __ID canale da rimuovere__\n> permessi richiesti: essere moderatore\n" +
            f"Prefisso_bot + **aggiorna_database** [bot offline durante l'aggiornamento]\n> permessi richiesti: essere moderatore senior",
            colour = discord.Colour.blue())
        
        developer = discord.Embed(
            title = "Comandi speciali disponibili [sviluppatori]:",
            description = f"• Prefissi_bot disponibili:⠀**--**⠀⠀**-!**\n\n" +
            f"Prefisso_bot + **sanity** + [**sanity**] [**limite sanity** (facoltativo)]\n> permessi richiesti: avere il ruolo 'Arknights'\n" +
            f"Prefisso_bot + **say** + __testo_da_inviare__\n> permessi richiesti: gestire i messaggi\n" +
            f"Prefisso_bot + **say** + __testo_da_inviare__\n> permessi richiesti: gestire i messaggi\n" +
            f"Prefisso_bot + **embed** + __testo_da_inviare__\n> permessi richiesti: gestire i messaggi\n" +
            f"Prefisso_bot + **clear** + __numero messaggi da eliminare__ [max 30]\n> permessi richiesti: essere moderatore senior\n" +
            f"Prefisso_bot + **blacklist_show** [mostra canali nella blacklist]\n> permessi richiesti: essere moderatore\n" +
            f"Prefisso_bot + **blacklist_add** + __ID canale da aggiungere__\n> permessi richiesti: essere moderatore\n" +
            f"Prefisso_bot + **blacklist_remove** + __ID canale da rimuovere__\n> permessi richiesti: essere moderatore\n" +
            f"Prefisso_bot + **aggiorna_database** [bot offline durante l'aggiornamento]\n> permessi richiesti: essere moderatore senior\n" +
            f"Prefisso_bot + **get_blacklist**⠀|⠀[ file.txt ]\n> permessi richiesti: essere sviluppatore\n" +
            f"Prefisso_bot + **get_database**⠀|⠀[ file.json ]\n> permessi richiesti: essere sviluppatore",
            colour = discord.Colour.blue())

        if ctx.message.author.id == MELONE_ID:
            await channel.send(embed = developer)
        else:
            await channel.send(embed = default)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(send_messages=True, manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx):
        channel = ctx.channel

        await ctx.message.delete()
        args = ctx.message.content.split()
        testo = " ".join(args[1:])

        await channel.trigger_typing()
        await asyncio.sleep(1)
        await channel.send(testo)

        if not ctx.message.author.id == MELONE_ID:
            indirizzo_log = self.client.get_channel(ID_CANALE_LOG)
            await indirizzo_log.send(testo + f' (Inviato da: **{ctx.message.author}**, canale **#{channel}**, comando: **say**)')

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(send_messages=True, manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    async def embed(self, ctx):
        channel = ctx.channel

        await ctx.message.delete()
        args = ctx.message.content.split()
        embed = discord.Embed(description = " ".join(args[1:]),
            colour = discord.Colour.purple())

        await channel.trigger_typing()
        await asyncio.sleep(1)
        await channel.send(embed = embed)

        if not ctx.message.author.id == MELONE_ID:
            indirizzo_log = self.client.get_channel(ID_CANALE_LOG)
            await indirizzo_log.send(embed + f' (Inviato da: **{ctx.message.author}**, canale **#{channel}**, comando: **embed**)')
    
    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(send_messages=True, manage_messages=True, read_message_history=True)
    @commands.has_any_role("Niizuki's database", "Admin", "Amministratore", "Moderator Senior")
    async def clear(self, ctx):
        channel = ctx.channel
        args =  ctx.message.content.split(" ")

        if args[1].isdigit():
            valore = int(args[1])
            if valore < 31:
                await channel.purge(limit=valore+1)
                text = "messaggio è stato mangiato da" if valore == 1 else "messaggi sono stati mangiati da"
                msg = await channel.send(embed = discord.Embed(
                    title = "Oh no!   >_<",
                    description = f"**{valore}** {text} {ctx.message.author.mention}",
                    colour = discord.Colour.purple()))
                await msg.delete(delay=5)

                if not ctx.message.author.id == MELONE_ID:
                    indirizzo_log = self.client.get_channel(ID_CANALE_LOG)
                    await indirizzo_log.send(f'**{ctx.message.author}** ha eliminato **{valore}** messaggio/i, canale **#{channel}**, comando: **clear**)')
            else:
                exceeded = await channel.send(embed = discord.Embed(
                    description = "Puoi eliminare fino a un massimo di 30 messaggi per volta",
                    colour = discord.Colour.purple()))
                await exceeded.delete(delay=5)
        else:
            error = await channel.send(embed = discord.Embed(
                description = "Inserisci un valore valido (max: 30)",
                colour = discord.Colour.purple()))
            await error.delete(delay=5)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True, manage_channels=True)
    @commands.has_any_role("Niizuki's database", "Admin", "Amministratore", "Moderator Senior", "Moderator", "Moderator")
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
                    nomi_canali.append(f"**{canale.name}**\nID canale\n*{id_canale}*")
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
    @commands.has_any_role("Niizuki's database", "Admin", "Amministratore", "Moderator Senior", "Moderator", "Moderator")
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
    @commands.has_any_role("Niizuki's database", "Admin", "Amministratore", "Moderator Senior", "Moderator", "Moderator")
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
    @commands.check(is_owner)
    @commands.bot_has_permissions(send_messages=True, attach_files=True, manage_messages=True)
    async def get_blacklist(self, ctx):
        channel = ctx.channel

        upload_blacklist = await channel.send(file=discord.File(os.path.join('file_niizuki', "blacklist.json")))
        await ctx.message.delete(delay=3)
        await upload_blacklist.delete(delay=5)
    
    @commands.command()
    @commands.guild_only()
    @commands.check(is_owner)
    @commands.bot_has_permissions(send_messages=True, attach_files=True, manage_messages=True)
    async def get_database(self, ctx):
        channel = ctx.channel

        upload_database = await channel.send(file=discord.File(os.path.join('file_niizuki', "mydatabase.json")))
        await ctx.message.delete(delay=5)
        await upload_database.delete(delay=30)
    
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role("Niizuki's database", "Admin", "Amministratore", "Moderator Senior")
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

        if not ctx.message.author.id == MELONE_ID:
            indirizzo_log = self.client.get_channel(ID_CANALE_LOG)
            await indirizzo_log.send(f"**{ctx.message.author}** ha avviato l'aggiornamento del database, canale **#{channel}**")

        aggiorna_database() # Imported
        update_database() # Imported

        await channel.send(embed = discord.Embed(
            description = "Aggiornamento terminato",
            colour = discord.Colour.purple()))

    # Arknights
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role("Niizuki's database", "Admin", "Amministratore", "Moderator Senior", "Moderator", "Moderator", "Arknights")
    async def sanity(self, ctx):
        weekday = datetime.today().weekday()
        channel = ctx.channel
        args = ctx.message.content.split()

        try:
            sanity_limit = args[2]
            if sanity_limit.isdigit():
                sanity_limit = int(sanity_limit)
            if sanity_limit > 135 or sanity_limit < 82:
                raise ValueError(f"**Attenzione:** valore **'sanity limit'** non valido\n[min=82, max=135, default=130]")
        except ValueError as e:
            await channel.send(embed = discord.Embed(
                description = f"{e}",
                colour = discord.Colour.purple()))
            sanity_limit = 135
            await channel.trigger_typing()
            await asyncio.sleep(1)
        except IndexError:
            sanity_limit = 130
        except TypeError:
            pass

        try:
            sanity_now = args[1]
            if sanity_now.isdigit():  
                sanity_now = int(sanity_now)

                if sanity_now > sanity_limit:
                    raise Exception(f"La sanity inserita **'{sanity_now}'** non può superare il limite **'{sanity_limit}'**")
                    
                ore_now = int(datetime.now(pytz.timezone('Europe/Berlin')).strftime("%H"))
                minuti_now = int(datetime.now(pytz.timezone('Europe/Berlin')).strftime("%M"))

                sanity = sanity_limit - sanity_now if sanity_now != sanity_limit else "full"
                if sanity == "full":
                    raise Exception(f"[sanity: **{sanity_now}**] [limite sanity: **{sanity_limit}**]\n\n**Attenzione:** hai la sanity piena!")
                
                tempo_refill = sanity * 6

                if tempo_refill != 6:
                    ore = int(tempo_refill / 60) + ore_now

                    if (tempo_refill / 60) >= 1:
                        minuti = int(((tempo_refill/60) - int(tempo_refill/60)) * 60) if tempo_refill % 60 != 0 else 00
                    else:
                        minuti = tempo_refill
                    
                    minuti_totali = minuti + minuti_now

                    #Carry over
                    if minuti_totali / 60 >= 1:
                        minuti_totali -= 60
                        ore += 1

                    #Next day
                    domani = False   
                    if ore >= 24:
                        ore -= 24
                        domani = " [di domani]"
                    
                    #Add leading zero
                    if len(str(minuti_totali)) == 1:
                        minuti_totali = str(minuti_totali).zfill(2)
                    if len(str(ore)) == 1:
                        ore = str(ore).zfill(2)

                    descrizione = f"[sanity: **{sanity_now}**] [limite sanity: **{sanity_limit}**] → Tempo refill: **{int(tempo_refill/60)}h e {minuti}min**\n\nLa tua sanity sarà piena alle **{ore}:{minuti_totali}**"
                    
                    #Descrizione next day
                    if domani:
                        descrizione += domani

                    my_sanity = discord.Embed(
                        description = descrizione,
                        colour = discord.Colour.blue())
                    if weekday == 0: #Monday
                        my_sanity.set_footer(text = "Ricordati di fare l'annihilation")
                    await channel.send(embed = my_sanity)
                else:
                    my_sanity = discord.Embed(
                        description = f"[sanity: **{sanity_now}**] [limite sanity: **{sanity_limit}**]\n\n**Attenzione:** avrai la sanity piena in meno di **6min**!",
                        colour = discord.Colour.dark_blue())
                    if weekday == 0:
                        my_sanity.set_footer(text = "Ricordati di fare l'annihilation")
                    await channel.send(embed = my_sanity)
            else:
                await channel.send(embed = discord.Embed(
                    description = "Inserisci un valore della sanity valido",
                    colour = discord.Colour.purple()))
        except (TypeError, IndexError):
            await channel.send(embed = discord.Embed(
                description = "Inserisci un valore valido",
                colour = discord.Colour.purple()))
        except Exception as e:
            exception = discord.Embed(
                description = f"{e}",
                colour = discord.Colour.dark_blue())
            if weekday == 0:
                exception.set_footer(text = "Ricordati di fare l'annihilation")
            await channel.send(embed = exception)

def setup(client):
    client.add_cog(Moderation(client))
