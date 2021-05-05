import discord
import json
from pathlib import Path
from discord.ext import commands

class Send(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def send(self, ctx, target: discord.Member, *, input_message):

        if isinstance(ctx.channel, discord.channel.DMChannel):

            data_folder = Path("database/")
            file_to_open = data_folder / "blacklist.json"

            target_dm = target.dm_channel
            if target_dm is None:
                target_dm = await target.create_dm()

            embed=discord.Embed(title="New Disconym message", description=input_message, color=0x169cdf)
            embed.set_footer(text="Sent using Disconym - Anynymous Discord messanger")
            send_msg = await target_dm.send(embed=embed)

            await ctx.send(f"Message to {target.mention} has been delivered succesfully ")

            await send_msg.add_reaction("❌")


def setup(client):
    client.add_cog(Send(client))