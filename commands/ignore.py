from re import U
import discord
from discord.ext import commands
from db_actions import Database

class Ignore(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def ignore(self, ctx, action, user : discord.User = None):
        if action == "add":
            if user != None:
                Database.add_ignore(ctx.author.id, user.id)
                await ctx.send(f"Sucessfuly added {user.mention} to your ignored list")

        elif action == "list":
            ignored_users = Database.get_ignored(ctx.author.id)
            await ctx.send(ignored_users)
            
        elif action == "remove":
            if user != None:
                Database.remove_ignored(ctx.author.id, user.id)
                await ctx.send(f"Sucessfuly removed {user.mention} from your ignored list")

def setup(client):
    client.add_cog(Ignore(client))