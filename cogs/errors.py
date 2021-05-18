import discord
import difflib
import datetime

from discord import embeds
from db_actions import Database
from discord.ext import commands

class Errors(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ok(self, ctx):
        for command in self.client.commands:
            print(command)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        command_list = []
        command_name = ctx.message.content.split(' ')[0].replace(Database.find_prefix(ctx.guild.id)[0], '')

        for command in self.client.commands:
            command_list.append(command.name)

        def genEmbed(error_code):
            error_responses = [f"Command **{command_name}** not found!\n{suggestCommand(command_name)}"]

            embed=discord.Embed(color=0xff1f1f)
            embed.add_field(name="Error", value=error_responses[error_code], inline=False)
            embed.set_footer(text=f"©️ {self.client.user.name}")
            embed.timestamp = datetime.datetime.now()
            return embed

        def suggestCommand(user_input):
            try:
                return f"Did you mean `{difflib.get_close_matches(user_input, command_list)[0]}`?"
            except:
                return "You can try `help`"

        if isinstance(error, commands.CommandNotFound):
            await ctx.send(embed=genEmbed(0))

def setup(client):
    client.add_cog(Errors(client))