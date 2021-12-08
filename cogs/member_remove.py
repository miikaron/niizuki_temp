import discord, os
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from os.path import join, dirname
import asyncio
from dotenv import load_dotenv
load_dotenv()

class Remove(commands.Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_member_remove(self, member):
        SERV_ID = os.getenv("SERV_ID")
        if member.guild.id == int(SERV_ID): #C.I.I
            channel = self.client.get_channel(552571690589225017)  #ID canale: #generale
        else:
            channel = get(member.guild.channels, name="welcome")

        bye = discord.Embed(
            description=f'Ops... {member.mention} ||**{member}**||\nha abbandonato il server',
            colour = discord.Colour.dark_green())
        bye.set_image(url = "attachment://rain.gif")

        img_path = os.path.join('file_niizuki', 'images')
        await channel.send(file=discord.File(os.path.join(img_path, "rain.gif")), embed=bye)

def setup(client):
    client.add_cog(Remove(client))