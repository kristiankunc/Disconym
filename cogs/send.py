import discord
from discord.ext import commands
from db_actions import Database

class Send(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def send(self, ctx, target: discord.Member, *, input_message):

        if isinstance(ctx.channel, discord.channel.DMChannel):

            if Database.check_blacklist(ctx.author.id) == False:
                target_dm = target.dm_channel
                if target_dm is None:
                    target_dm = await target.create_dm()

                log_channel = self.client.get_channel(840519497747398696)
                log_msg = await log_channel.send("⠀")

                msg_id = Database.add_log(log_msg.jump_url)
                new_msg_embed=discord.Embed(title="New Disconym message", description=f"{input_message}\n━━━━━━━━━━━━━━━\nMessage ID - `{msg_id}`", color=0x169cdf)
                new_msg_embed.set_footer(text=f"© Disconym 2021")
                send_msg = await target_dm.send(embed=new_msg_embed)

                embed=discord.Embed(color=0x169cdf)
                embed.add_field(name="Message data", value=f"Author profile - {ctx.author.mention}\nAuthor name - `{ctx.author.name}`\nAuthor ID - `{ctx.author.id}`\n━━━━━━━━━━━━━━━\nRecipient profile - {target.mention}\nRecipient name - `{target.name}`\nRecipient ID - `{target.id}`", inline=False)
                embed.add_field(name="Message content", value=f"`{input_message}`")
                embed.set_footer(text=f"Message ID - {msg_id}")

                await log_msg.edit(embed=embed)

                await ctx.send(f"Message to {target.mention} has been delivered succesfully ")

            else:
                await ctx.send("Error, you are blacklisted from sending Disconym messages")


def setup(client):
    client.add_cog(Send(client))