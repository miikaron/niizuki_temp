import discord, os
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from datetime import datetime, timezone
import pytz, time, asyncio
from dotenv import load_dotenv
load_dotenv()

def Checktime():
    return datetime.now(pytz.timezone('Europe/Berlin')).strftime("%H")
#---------------------------------------------------------------------------------------------------
                            # Lista saluti
#---------------------------------------------------------------------------------------------------
buongiorno_ping = [
    "good morning", "guten morgen", "buenos dias", "bonjour",
    "buongiorno", "buondì",  "buon dì", "'giorno", "buongiornissimo",
    "'morning", "buon pomeriggio", "good afternoon",
    "ohayo", "おはよう", "お早う", "早上好", "中午好", "早安"
    ]
buonanotte_ping = [
    "buonanotte", "晚安", "oyasumi", "おやすみ", "御休み",
    "notte", "buona notte", "good night", "gute nacht", "buenas noches"
    ]
saluti_frase = [
    "ciao", "salve", "ave", "hello", "hi", "konnichiwa", "hola", "hallo",
    "你好", "大家好", "你们好", "今晩は", "こんいちは", "guten tag", "grüß gott", "bye", "salut",
                            # Sera
    "buonasera", "good evening", "下午好", "晚上好", "konbanwa", "今晩は",
    "bye~", "salve~", "hello~", "konnichiwa~", "你好~", "大家好~", "こんいちは~", "konbanwa~"
    ]
saluti = [
    "giorno", "sera", "buona serata",
    "we", "wa", "ni hao", "bye-bye",
    "a dopo", "a più tardi", "a domani"
    ]
#---------------------------------------------------------------------------------------------------
                            # Orario
#---------------------------------------------------------------------------------------------------
morning = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]
noon = ["12", "13", "14", "15", "16"]
evening = ["17", "18", "19", "20", "21"]

bot_prefixes = ('-', '+', '*', '!', '?', '.', ',', ':', ';', '_', '£', '$', '%', '&', '=', '^', '>', 'à', 'é', 'ì', 'ò', 'ù', '~', '`', '"')
IVR_ID = os.getenv("IVR")

class Saluti(commands.Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.content.startswith(bot_prefixes):
            return

        channel = message.channel
        emoji_saluto = discord.utils.get(self.client.emojis, name='SpeeWave')
        if emoji_saluto == None:
            emoji_saluto = "\U0001F44B"

        # Tutturu
        if ":tutturu:" in message.content.lower() and message.author.id == int(IVR_ID):
            await message.add_reaction(emoji_saluto)

        for word in message.content.lower().split():
            if len([word for word in message.content.split()]) == 1 and word in saluti:
                await message.add_reaction(emoji_saluto)
            elif word in saluti_frase:    
                await message.add_reaction(emoji_saluto)

        ora_locale = Checktime()

        def _check(filtered_msg):
            giorno_triggered = any(word in buongiorno_ping for word in filtered_msg.content.lower().split())
            notte_triggered = any(word in buonanotte_ping for word in filtered_msg.content.lower().split())
            saluto_triggered = True if giorno_triggered or notte_triggered else False
            is_reply = filtered_msg.reference or filtered_msg.mentions
            recent_msg = (datetime.utcnow()-filtered_msg.created_at).seconds < 60
            return saluto_triggered and not is_reply and recent_msg and message.author.id == filtered_msg.author.id

        if not message.mentions and not message.reference:
            is_short = len([word for word in message.content.split()]) < 5
            spam = len(list(filter(lambda filtered_msg: _check(filtered_msg), self.client.cached_messages))) >= 2 #allowed every 60s
            if is_short and not spam:
                saluto_giorno = False
                saluto_notte = False
                for word in message.content.lower().split():
                    if word in buongiorno_ping and not any(word in buonanotte_ping for word in message.content.lower().split()):
                        saluto_giorno = True
                    elif word in buonanotte_ping:
                        saluto_notte = True
                
                if saluto_giorno is True:
                    if ora_locale in morning:
                        saluto = "Buongiorno"
                    if ora_locale in noon:
                        saluto = "Buon pomeriggio"
                    if ora_locale in evening:
                        saluto = "Buonasera"
                    await message.add_reaction(emoji_saluto)
                    
                    if saluto:
                        await channel.trigger_typing()
                        await asyncio.sleep(0.5)
                        await channel.send(embed = discord.Embed(
                            description = f'{saluto} <@{message.author.id}>',
                            colour = discord.Colour.blue()))
                    saluto_giorno = False

                if saluto_notte is True:
                    #Check buonanotte
                    message_content = [word for word in message.content.lower().split()]
                    if "notte" in message_content and len(message_content) != 1:
                        return

                    await message.add_reaction(emoji_saluto)
                    await channel.trigger_typing()
                    await asyncio.sleep(0.5)
                    await channel.send(embed = discord.Embed(
                        description = f'Buonanotte <@{message.author.id}>',
                        colour = discord.Colour.blue()))
                    saluto_notte = False
                        
                
def setup(client):
    client.add_cog(Saluti(client))