import discord
from db_actions import Database
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class Contribute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="contribute", description="Sends link to the GitHub repo")
    async def _contribute(self, ctx: SlashContext):
        await self.help(ctx)

    @commands.command(aliases=["c"], description="Sends link to the GitHub repo")
    async def contribute(self, ctx):
        await ctx.send("You can contribute here:\n<https://github.com/KristN1/disconym>")

def setup(client):
    client.add_cog(Contribute(client))