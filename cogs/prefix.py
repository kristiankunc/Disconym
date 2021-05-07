import discord
from pathlib import Path
from discord.ext import commands
import mysql.connector as mysql
from db_actions import Database

class Prefix(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True) 
    async def prefix(self, ctx, prefix):
        Database.replace_prefix(ctx.guild.id, prefix)
        
        await ctx.send(f'Prefix changed to: {prefix}')

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        Database.add_prefix(guild.id, ".")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        Database.remove_prefix(guild.id)

def setup(client):
    client.add_cog(Prefix(client))