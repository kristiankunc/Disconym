import discord
import asyncio
import datetime
from discord.ext import commands
from db_actions import Database
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option

user_cache = []

class Send(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash  (name="send",
                        description="Send an anonymous message to desired user",
                        options=[
                            create_option(
                            name="recipient",
                            description="The user who is going to receive the message",
                            option_type=6,
                            required=True
                            ),

                            create_option(
                            name="message",
                            description="The actual message",
                            option_type=3,
                            required=True
                            )
                        ])

    async def _send(self, ctx: SlashContext, recipient: discord.Member, message: str):
        await self.send_command(ctx=ctx, target=recipient, input_message=message)

    @commands.command()
    @commands.dm_only()
    async def send(self, ctx, target: discord.Member, *, input_message):
        await self.send_command(ctx, target, input_message)

    async def send_command(self, ctx, target: discord.Member, *, input_message):
        status = False

        if ctx.author.id in user_cache:
            status = True
            await ctx.send("Please wait before sending another message.", hidden=True)

        elif ctx.author == target:
            status = True
            await ctx.send("You can't send messages to yourself", hidden=True)

        elif input_message == None:
            status = True
            await ctx.send("You can not send an empty message", hidden=True)

        elif Database.check_blacklist(ctx.author.id) == True:
            status = True
            await ctx.send("You are blacklisted from sending Disconym messages", hidden=True)

        elif Database.check_ignored(ctx.author.id, target.id) == 1:
            status = True
            await ctx.send("You can not send message to user who is in your ignored list", hidden=True)
            
        elif Database.check_ignored(ctx.author.id, target.id) == 2:
            status = True
            await ctx.send("You can not send message to user who is ignoring you", hidden=True)

        if status == False:
            try:
                target_dm = target.dm_channel

                if target_dm is None:
                    target_dm = await target.create_dm()

                log_channel = self.client.get_channel(840519497747398696)
                log_msg = await log_channel.send("⠀")

                bot_name = self.client.user.name
                bot_pfp = self.client.user.avatar_url

                msg_id = Database.add_log(log_msg.jump_url)
                new_msg_embed=discord.Embed(title="New Disconym message", description=f"{input_message}\n━━━━━━━━━━━━━━━\nMessage ID - `{msg_id}`", color=0x169cdf)
                new_msg_embed.set_footer(text=bot_name, icon_url=bot_pfp)
                new_msg_embed.timestamp = datetime.datetime.now()

                try:
                    await target_dm.send(embed=new_msg_embed)
                except:
                    await ctx.send(f"Failed to send a message to {target.mention}", hidden=True)

                await ctx.send(f"Message to {target.mention} has been delivered successfully", hidden=True)

                embed=discord.Embed(color=0x169cdf)
                embed.add_field(name="Message data", value=f"Author profile - {ctx.author.mention}\nAuthor name - `{ctx.author.name}`\nAuthor ID - `{ctx.author.id}`\n━━━━━━━━━━━━━━━\nRecipient profile - {target.mention}\nRecipient name - `{target.name}`\nRecipient ID - `{target.id}`", inline=False)
                embed.add_field(name="Message content", value=f"`{input_message}`")
                embed.set_footer(text=f"Message ID - {msg_id}")

                await log_msg.edit(embed=embed)

                user_cache.append(ctx.author.id)

                await asyncio.sleep(60)
                user_cache.remove(ctx.author.id)


            except:
                await ctx.send("Failed to send message to that user\nMake sure their DMs are opened and that it is not a bot", hidden=True)

                
def setup(client):
    client.add_cog(Send(client))