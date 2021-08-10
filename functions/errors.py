from typing import AsyncIterable
import discord
import difflib
import datetime
from discord import embeds
from discord.ext.commands.errors import MissingPermissions
from db_actions import Database
from discord.ext import commands

class Errors(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def handle_error(self, ctx, error, slash):
        bot_name = self.client.user.name
        bot_pfp = self.client.user.avatar_url

        if slash == True:
            if ctx.guild_id != None:
                prefix = Database.find_prefix(ctx.guild.id)[0]
            else:
                prefix = "!"

            author = self.client.get_user(ctx.author_id)
            channel = self.client.get_channel(ctx.channel_id)
            command_name = ctx.name

        elif slash == False:
            if ctx.guild != None:
                prefix = Database.find_prefix(ctx.guild.id)[0]
            else:
                prefix = "!"

            command_name = ctx.message.content.split(' ')[0].replace(prefix, '')

        def genEmbed(error_response):
            embed=discord.Embed(title="Error", description=error_response, color=0xff1f1f)
            embed.set_footer(text=bot_name, icon_url=bot_pfp)
            embed.timestamp = datetime.datetime.now()
            return embed

        def suggestCommand(user_input):
            available_commands = []
            for command in self.client.commands:
                available_commands.append(command.name)

            try:
                return f"Did you mean `{prefix}{difflib.get_close_matches(user_input, available_commands)[0]}`?"
            except:
                return f"You can do `{prefix}help` to see all the available commands"

        if isinstance(error, commands.CommandNotFound):
            await ctx.send(embed=genEmbed(f"Command **{command_name}** not found!\n{suggestCommand(command_name)}"))
        elif isinstance(error, commands.PrivateMessageOnly):
            await ctx.send(embed=genEmbed(f"Command **{command_name}** can be only used in private messages!"))
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=genEmbed(f"Missing required argument!\nUse `{prefix}help` for the correct syntax"))
        elif isinstance(error, MissingPermissions):
            await ctx.send(embed=genEmbed(f"You are missing permissions to run **{command_name}**"))
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=genEmbed(f"Member **{error.argument}** not found"))
        elif isinstance(error, commands.UserNotFound):
            await ctx.send(embed=genEmbed(f"User **{error.argument}** not found"))

        else:
            print("-------------------")
            print(error)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await self.handle_error(ctx, error, False)

    @commands.Cog.listener()
    async def on_slash_command_error(self, ctx, error):
        await self.handle_error(ctx, error, True)

def setup(client):
    client.add_cog(Errors(client))