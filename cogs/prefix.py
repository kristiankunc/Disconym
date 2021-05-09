import discord
from discord.ext import commands
from db_actions import Database

class Prefix(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True) 
    async def prefix(self, ctx, prefix):
        Database.replace_prefix(ctx.guild.id, prefix)

        embed=discord.Embed(title = "Prefix changed", description = f"Prefix for **{ctx.guild.name}** has been changed to `{prefix}`", color=0x08ccfd)
        embed.set_footer(text="© Disconym")
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        Database.add_prefix(guild.id, ".")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        Database.remove_prefix(guild.id)

def setup(client):
    client.add_cog(Prefix(client))