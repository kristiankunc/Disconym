import discord
import datetime
from discord.ext import commands
from db_actions import Database
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

class Ignore(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash  (name="ignore",
                        description="List & Manage users in your ignored list",
                        options=[
                        create_option(
                            name="action",
                            description="Select action which you want to use for this command",
                            option_type=3,
                            required=True,
                            choices=[
                            create_choice(
                                name="Add",
                                value="add"
                            ),
                            create_choice(
                                name="Remove",
                                value="remove"
                            ),
                            create_choice(
                                name="list",
                                value="list"
                            )
                            ]
                        ),
                        create_option(
                            name="User",
                            description="Enter a user that you want to use for this command (only for add/remove)",
                            option_type=6,
                            required=False,
                        )
                        ])


    async def _ignore(self, ctx: SlashContext, action, user : discord.User = None):
        await self.ignore_command(ctx=ctx, action=action, user=user)


    @commands.command()
    async def ignore(self, ctx, action, user : discord.User = None):
        await self.ignore_command(ctx, action, user)


    async def ignore_command(self, ctx, action, user : discord.User = None):
        if action == "add":
            if user != None:
                ignored_code = Database.check_ignored(ctx.author.id, user.id)
                print(ignored_code)
                if ignored_code !=1:
                    Database.add_ignore(ctx.author.id, user.id)
                    await ctx.send(f"Successfully added **{user.name}** to your ignored list")

                else:
                    await ctx.send(f"You are already ignoring **{user.name}**")

        elif action == "list":
            ignored_users = ""

            ignored_users_data = Database.get_ignored(ctx.author.id)
            for data in ignored_users_data:
                for user in data:
                    ignored_users += f"<@{user}> - `{user}`\n"

            if ignored_users == "":
                ignored_users = "*There are no ignored users*"
                
            bot_name = self.client.user.name
            bot_pfp = self.client.user.avatar_url

            embed=discord.Embed(title="Ignored Users", description=ignored_users, color=0x169cdf)
            embed.timestamp = datetime.datetime.now()

            embed.set_footer(text=bot_name, icon_url=bot_pfp)
            await ctx.send(embed=embed)
            
        elif action == "remove":
            if user != None:
                Database.remove_ignored(ctx.author.id, user.id)
                await ctx.send(f"Successfully removed **{user.name}** from your ignored list")

        else:
            await ctx.send(f"Invalid action - {action}")

def setup(client):
    client.add_cog(Ignore(client))