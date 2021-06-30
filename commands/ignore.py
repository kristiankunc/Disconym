import discord
import datetime
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
                await ctx.send(f"Successfully added {user.mention} to your ignored list")

        elif action == "list":
            ignored_users = ""

            ignored_users_data = Database.get_ignored(ctx.author.id)
            for data in ignored_users_data:
                for user in data:
                    ignored_users += f"<@{user}> - `{user}`\n"

            bot_name = self.client.user.name
            bot_pfp = self.client.user.avatar_url

            embed=discord.Embed(title="Ignored Users", description=ignored_users, color=0x169cdf)
            embed.timestamp = datetime.datetime.now()

            embed.set_footer(text=bot_name, icon_url=bot_pfp)
            await ctx.send(embed=embed)
            
        elif action == "remove":
            if user != None:
                Database.remove_ignored(ctx.author.id, user.id)
                await ctx.send(f"Successfully removed {user.mention} from your ignored list")

def setup(client):
    client.add_cog(Ignore(client))