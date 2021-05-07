import discord
import db_actions
import mysql.connector as mysql
from discord.ext import commands
from db_actions import Database

class Database_ctr(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add_prefix(self, ctx, guild_id, prefix):
        Database.add_prefix(guild_id, prefix)

        await ctx.send(f"Prefix added\nGuild ID - {guild_id}\nPrefix - {prefix}")

    @commands.command()
    async def remove_prefix(self, ctx, guild_id):
        Database.remove_prefix(guild_id)

        await ctx.send(f"Prefix removed\nGuild ID - {guild_id}")

    @commands.command()
    async def replace_prefix(self, ctx, guild_id, prefix):
        Database.replace_prefix(guild_id, prefix)

        await ctx.send(f"Prefix replaced\nGuild ID - {guild_id}\nPrefix - {prefix}")

    
    @commands.command()
    async def add_blacklist(self, ctx, user_id, *, reason):
        Database.add_blacklist(user_id, reason)

        await ctx.send(f"User {user_id} has been blacklisted")

    @commands.command()
    async def remove_blacklist(self, ctx, user_id):
        Database.remove_blacklist(user_id)

        await ctx.send(f"User {user_id} has been removed from the blacklist")

def setup(client):
    client.add_cog(Database_ctr(client))