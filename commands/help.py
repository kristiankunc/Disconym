import discord
import asyncio
import datetime
from db_actions import Database
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="help", description="Show all the commands and their syntax")
    async def _help(self, ctx: SlashContext):
        await self.help(ctx)

    @commands.command()
    async def help(self, ctx):
        prefix = Database.find_prefix(ctx.guild.id)[0]
        embed = None
        help_msg = None
        author = ctx.author
        robot_emoji = "🤖"
        hand_emoji = "✍️"
        book_emoji = "📕"
        home_emoji = "🏠"

        def gen_embed(category, fields):
            global embed

            if category == 0:
                title = "Help Menu"
                descriptionn = "Use reactions to get more info about a category"
                field_vaulues = "🤖 General Commands__Other - not so useful commands__✍️ Sending Messages__Main feature of the bot__📕 Reporting Users__How to report and block user"
            elif category == 1:
                title = "🤖 General Commands"
                descriptionn = "General commands desc\narguments in () are required, and <> are optional"
                field_vaulues = f"Latency__`{prefix}ping`__Prefix__`{prefix}prefix (new_prefix)`__Privacy Policy__`{prefix}privacy`__Contributing__`{prefix}contribute`"
            elif category == 2:
                title = "✍️ Sending messages"
                descriptionn = "How to send a new message to user\narguments in () are required, and <> are optional"
                field_vaulues = f"Send__`{prefix}send (Usernam#tag) (message)`\n*must be executed in bot's private messages*"
            elif category == 3:
                title = "📕 Reporting Users"
                descriptionn = "How to report a user\narguments in () are required, and <> are optional"
                field_vaulues = f"Submit a report__`{prefix}report (message_id) <reason>`"

            values_list = field_vaulues.split("__")
            values_loop = 0

            bot_name = self.client.user.name
            bot_pfp = self.client.user.avatar_url

            embed=discord.Embed(title=title, description=descriptionn, color=0x169cdf)
            embed.timestamp = datetime.datetime.now()
            embed.set_footer(text=bot_name, icon_url=bot_pfp)


            while fields > 0:
                embed.add_field(name=values_list[values_loop], value=values_list[values_loop+1], inline=False)
                values_loop += 2
                fields -= 1

            if help_msg == None:
                return ctx.send(embed=embed)
            else:
                return help_msg.edit(embed=embed)

        help_msg = await gen_embed(0, 3)

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
                    await gen_embed(1, 4)
                elif str(reaction.emoji) == hand_emoji:
                    await gen_embed(2, 1)
                elif str(reaction.emoji) == book_emoji:
                    await gen_embed(3, 1)
                elif str(reaction.emoji) == home_emoji:
                    await gen_embed(0, 3)
                
                

def setup(client):
    client.add_cog(Help(client))