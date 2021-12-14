import discord, os
from discord import Game
from discord.ext import commands, tasks
import platform, sys, asyncio, random
from datetime import datetime
import pytz
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Custom commands prefix / help
client = commands.Bot(command_prefix = ('-!', '--'), intents=intents)
client.remove_command('help')

if __name__ == "__main__":
    for filename in os.listdir('./cogs'):
        try:
            if filename.endswith('.py') and filename != "__init__.py":
                client.load_extension(f'cogs.{filename[:-3]}')
        except Exception as e:
            exception = f"{type(e).__name__}: {e}"
            extension = f'cogs.{filename[:-3]}'
            print(f"Failed to load extension {extension}\n{exception}")

# Discord status (random)
def task_list():
    tasks = [
        'playing', 'listening', 'watching'
        ]
    return random.choice(tasks)

@tasks.loop(minutes=7)
async def status_task():  
    _play = [
        'Azur Lane',
        'Genshin Impact',
        'VLC Media Player',
        ]

    _watch = [
        'Azur Lane: Bisoku Zenshin! - PV',
        'Azur Lane Universe in Unison Animation PV',
        'Assault Lily BOUQUET - Opening Theme - Sacred world',
        'Assault Lily: Bouquet ED 1 - Edel Lilie',
        'TONIKAWA: Over The Moon For You - Opening (HD)',
        "I'm Standing on a Million Lives - Ending (HD)",
        'Majo no Tabitabi Opening Full - 『Literature』by Reina Ueda',
        ]

    _listen = [
        'Genshin Impact - The Wind and The Star Traveler',
        'Jade Moon Upon a Sea of Clouds - Disc 1: Glazed Moon Over the Tides｜Genshin Impact',
        'Jade Moon Upon a Sea of Clouds - Disc 2: Shimmering Sea of Clouds and Moonlight｜Genshin Impact',
        'Jade Moon Upon a Sea of Clouds - Disc 3: Battles of Liyue｜Genshin Impact',
        'City of Winds and Idylls - Disc 1: City of Winds and Idylls｜Genshin Impact',
        'City of Winds and Idylls - Disc 2: The Horizon of Dandelion｜Genshin Impact',
        'City of Winds and Idylls - Disc 3: Saga of the West Wind｜Genshin Impact',
        ]

    status = task_list()
    if status == 'playing':
        _name = random.choice(_play)
        _type = 0
        _status = discord.Status.dnd    #do_not_disturb

    elif status == 'listening':
        _name = random.choice(_listen)
        _type = 2
        _status = None

    elif status == 'watching':
        _name = random.choice(_watch)
        _type = 3
        _status = discord.Status.idle

    await client.change_presence(status=_status, activity=discord.Activity(name=_name, type=_type))
    print("User status updated")

@tasks.loop(minutes=7)
async def change_time_utc():
    channel = client.get_channel(920076324243140638) #Voice channel
    # Mountain Time Zone (UTC-7)
    MTZ = pytz.timezone("America/Phoenix")
    datetime_utc = datetime.now(MTZ)
    time_utc = datetime_utc.strftime('%H:%M')
    await channel.edit(name=f"🕘 {time_utc} | UTC-7")
    print(channel)

@client.event
async def on_ready():
    print(f"• Logged in as: {client.user.name}")
    print(f"• Discord.py API version: {discord.__version__}")
    print(f"• Running on: {platform.system()} {platform.release()} ({os.name})")
    print(f"• Python version: {platform.python_version()}")
    print("------------------------------")
    # Change time
    if client.get_guild(int(os.getenv("SERV_ID"))):
      change_time_utc.start()
    # Change bot status
    status_task.start()

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed = discord.Embed(
        title = "Parametri mancanti",
        description = f'{error}',
        colour = discord.Colour.red()))
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send(embed = discord.Embed(
        title = "Permessi mancanti",
        description = f'{error}',
        colour = discord.Colour.red()))
    elif isinstance(error, commands.errors.CheckFailure):
        await ctx.send(embed = discord.Embed(
        title = "Accesso negato",
        description = f'{error}',
        colour = discord.Colour.red()))
    elif isinstance(error, commands.errors.CommandNotFound):
        pass
    elif isinstance(error, Exception):
        await ctx.send(embed = discord.Embed(
        title = "Errore",
        description = f'{error}',
        colour = discord.Colour.red()))
            
client.run(os.getenv("CLIENT_TOKEN"))