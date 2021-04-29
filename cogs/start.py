import discord
from discord.ext import commands
from discord.utils import get

class Start(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)

def setup(client):
    client.add_cog(Start(client))