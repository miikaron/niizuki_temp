import discord, os
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from os.path import join
import asyncio

SPOILER_PREFIX = 'spoiler!'
sending = False

class Spoiler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        msg = message.content
        channel = message.channel

        if msg.lower().startswith(SPOILER_PREFIX):
            global sending
            if sending is False:
                if message.attachments:
                    try:
                        PATH = join('file_niizuki', 'spoiler')
                        for attachment in message.attachments:
                            if not attachment.is_spoiler():
                                # Save attachment
                                spoiler_image = f'SPOILER_{message.author.name}_{attachment.filename}'
                                await attachment.save(os.path.join(PATH, spoiler_image))

                        sending = True
                        await channel.send(embed = discord.Embed(
                            description = f'Messaggio di <@{message.author.id}>\nClicca qui se non vedi il nome: || {message.author.name} ||',
                            colour = discord.Colour.purple()))
                        
                        for image in os.listdir(PATH):
                            if image.endswith(".txt") is False:
                                is_sent = await channel.send(file=discord.File(os.path.join(PATH, image)))
                                if is_sent:
                                    os.remove(os.path.join(PATH, image))
                        await message.delete()
                        sending = False
                    except Exception as e:
                        print(f"Errore comando 'spoiler!' -- {e}")
            else:
                riprova = await channel.send(embed = discord.Embed(
                    description = f'Comando in uso...\nRiprova più tardi',
                    colour = discord.Colour.purple()))
                await riprova.delete(delay=5)  

def setup(client):
    client.add_cog(Spoiler(client))
