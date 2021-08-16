import discord
import asyncio
import tracemalloc
import datetime
from db_actions import Database
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
tracemalloc.start()
class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    def gen_embed(self, category, prefix, command = None):
        if category == 0:
            title = "Help Menu"
            description = "Use reactions to get more info about a category"
            field_values = "🤖 General Commands__Other - not so useful commands__✍️ Sending Messages__Main feature of the bot__📕 Reporting Users__How to report and block user"
        elif category == 1:
            title = "🤖 General Commands"
            description = "General commands desc\narguments in () are required, and [] are optional"
            field_values = f"Latency__`{prefix}ping`__Prefix__`{prefix}prefix (new_prefix)`__Ignore__`{prefix}ignore (action) [user]`__Privacy Policy__`{prefix}privacy`__Contributing__`{prefix}contribute`"
        elif category == 2:
            title = "✍️ Sending messages"
            description = "How to send a new message to user\narguments in () are required, and [] are optional"
            field_values = f"Send__`{prefix}send (Usernam#tag) (message)`\n*must be executed in bot's private messages*"
        elif category == 3:
            title = "📕 Reporting Users"
            description = "How to report a user\narguments in () are required, and [] are optional"
            field_values = f"Submit a report__`{prefix}report (message_id) [reason]`"

        elif category == 100:
            title = "👨‍💻 Command Syntax"
            description = f"Command syntax **help**\narguments in () are required, and [] are optional"
            field_values = f"{command.name} syntax__`{prefix}{command.name} {command.signature}`"

        values_list = field_values.split("__")
        fields = len(values_list) / 2
        values_loop = 0

        bot_name = self.client.user.name
        bot_pfp = self.client.user.avatar_url

        embed=discord.Embed(title=title, description=description, color=0x169cdf)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=bot_name, icon_url=bot_pfp)

        while fields > 0:
            embed.add_field(name=values_list[values_loop], value=values_list[values_loop+1], inline=False)
            values_loop += 2
            fields -= 1

        return embed

    @cog_ext.cog_slash(name="help", description="Show all the commands and their syntax")
    async def _help(self, ctx: SlashContext):
        await self.help(ctx)

    @commands.command()
    async def help(self, ctx, command_name = None):
        help_msg = None
        prefix = Database.find_prefix(ctx.guild.id)[0]

        if command_name != None:
            found_command = self.client.get_command(command_name)
            if found_command == None:
                await ctx.send("Command not found")
            else:
                await ctx.send(embed=self.gen_embed(100, prefix, found_command))


        else:
            author = ctx.author
            robot_emoji = "🤖"
            hand_emoji = "✍️"
            book_emoji = "📕"
            home_emoji = "🏠"

            help_msg = await ctx.send(embed=self.gen_embed(0, prefix))

            await help_msg.add_reaction(robot_emoji)
            await help_msg.add_reaction(hand_emoji)
            await help_msg.add_reaction(book_emoji)
            await help_msg.add_reaction(home_emoji)

            def check(reaction, user):
                return user == ctx.author

            while True:
                try:
                    reaction, user = await self.client.wait_for('reaction_add', timeout=25.0, check=check)
                except asyncio.TimeoutError:
                    break
                else:
                    await help_msg.remove_reaction(reaction.emoji, author)

                    if str(reaction.emoji) == robot_emoji:
                        await help_msg.edit(embed=self.gen_embed(1, prefix))
                    elif str(reaction.emoji) == hand_emoji:
                        await help_msg.edit(embed=self.gen_embed(2, prefix))
                    elif str(reaction.emoji) == book_emoji:
                        await help_msg.edit(embed=self.gen_embed(3, prefix))
                    elif str(reaction.emoji) == home_emoji:
                        await help_msg.edit(embed=self.gen_embed(0, prefix))
                

def setup(client):
    client.add_cog(Help(client))