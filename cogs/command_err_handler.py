import inspect
import discord
from discord.ext import commands
from db_actions import Database

class CommandErrorHandler(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(error)
        if isinstance(error, commands.BadArgument):
            await ctx.send("Member not found")

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing requiered argument")

        if isinstance(error, commands.PrivateMessageOnly):
            await ctx.send("This command can be only executed in private messages")

        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send("This command does not work in private messages")

        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not found")

        if isinstance(error, commands.TooManyArguments):
            await ctx.send("You entered too many arguments")

def setup(client):
    client.add_cog(CommandErrorHandler(client))