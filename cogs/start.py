import discord
from discord.ext import commands
from discord.utils import get

class Send(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def dm(self, ctx, diruser : discord.User, message):
        print("dsdasdas")


def setup(client):
    client.add_cog(Send(client))