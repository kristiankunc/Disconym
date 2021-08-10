from db_actions import Database
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="dms",
                        description="Open/Close your Disconym DMs",
                        options=[
                        create_option(
                            name="option",
                            description="Select the open or close option",
                            option_type=3,
                            required=True,
                            choices=[
                            create_choice(
                                name="Open",
                                value="open"
                            ),
                            create_choice(
                                name="Close",
                                value="close"
                            )
                            ]
                        )
                        ])

    async def dms_slash(self, ctx: SlashContext, option):
        await self.dms(ctx, option)

    @commands.command()
    async def dms(self, ctx, option):
        if option.lower() == "open":
            Database.dms_open(ctx.author.id)
            await ctx.send("Your Disconym DMs have been opened!")

        elif option.lower() == "close":
            Database.dms_close(ctx.author.id)
            await ctx.send("Your Disconym DMs have been closed!")

        else:
            await ctx.send("Invalid option, select from open/close")

def setup(client):
    client.add_cog(Ping(client))