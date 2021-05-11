import discord
import asyncio
from discord import embeds
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = None
        help_msg = None
        author = ctx.author
        robot_emoji = "🤖"
        hand_emoji = "✍️"
        book_emoji = "📕"

        def gen_embed(category, fields):
            global embed

            if category == 0:
                title = "Help Menu"
                descriptionn = "Use reactions to get more info about a category"
                field_vaulues = "🤖 General Commands_Other - not so useful commands_✍️ Sending Messages_Main feature of the bot_📕 Reporting Users_How to report a user"
            elif category == 1:
                title = "🤖 General Commands"
                descriptionn = "General commands desc"
                field_vaulues = "Title1_val1"
            elif category == 2:
                title = "✍️ Sending messages"
                descriptionn = "Sending messages desc"
                field_vaulues = "Title1_val1"
            elif category == 3:
                title = "📕 Reporting Users"
                descriptionn = "Reporting Users desc"
                field_vaulues = "Title1_val1"      

            values_list = field_vaulues.split("_")
            values_loop = 0

            embed=discord.Embed(title=title, description=descriptionn, color=0x169cdf)
            embed.set_footer(text="© Disconym")

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

        def check(reaction, user):
            return user == ctx.author

        while True:
            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout=15.0, check=check)
            except asyncio.TimeoutError:
                break
            else:
                await help_msg.remove_reaction(reaction.emoji, author)

                if str(reaction.emoji) == robot_emoji:
                    await gen_embed(1, 1)
                elif str(reaction.emoji) == hand_emoji:
                    await gen_embed(2, 1)
                elif str(reaction.emoji) == book_emoji:
                    await gen_embed(3, 1)
                
                

def setup(client):
    client.add_cog(Help(client))