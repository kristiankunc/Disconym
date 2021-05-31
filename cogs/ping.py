import discord
import datetime
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="ping", description="Show the bot's latency")
    async def ping_slash(self, ctx: SlashContext):
        await self.ping_command(ctx)

    @commands.command()
    async def ping(self, ctx):
        await self.ping_command(ctx)

    async def ping_command(self, ctx):
        embed=discord.Embed(color=0x08ccfd)
        embed.add_field(name="Pong", value=f"Latency is `{round(self.client.latency * 1000)}`ms", inline=False)
        embed.set_footer(text="© Disconym")
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Ping(client))