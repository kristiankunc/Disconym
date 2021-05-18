import discord
import asyncio
import datetime
from discord import user
from discord.ext import commands
from db_actions import Database

user_cache = []

class Report(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def report(self, ctx, log_id, reason=None):
        if ctx.author.id in user_cache:
            await ctx.send("Please wait before submitting another report")

        else:
            user_cache.append(ctx.author.id)
            author = ctx.message.author
            pfp = author.avatar_url

            reports_channel = self.client.get_channel(840568536542871572)

            report_embed=discord.Embed(color=0x341aff)
            report_embed.add_field(name="New report submitted", value=f"Report author profile - {ctx.author.mention}\nReport author name - `{ctx.author.name}`\nReport author ID - `{ctx.author.id}`\nReport reason - `{reason}`", inline=False)
            report_embed.add_field(name="Message data", value=f"Message ID - `{log_id}`\nMessage log link - {Database.get_log(log_id)[0]}")
            report_msg = await reports_channel.send(embed=report_embed)

            await report_msg.add_reaction("✅")

            report_embed=discord.Embed(title ="Report Submitted", description ="Your report has been submitted and will be reviewed by the moderation team", color=0x341aff)
            report_embed.set_footer(text=f"©️ {self.client.user.name}")
            report_embed.timestamp = datetime.datetime.now()
            await ctx.channel.send(embed=report_embed)

            await asyncio.sleep(300)
            user_cache.remove(ctx.author.id)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.channel_id == 840568536542871572:
            if payload.user_id != 837418967155998740:

                current_guild = self.client.get_guild(payload.guild_id)
                current_channel = current_guild.get_channel(payload.channel_id)
                current_msg = await current_channel.fetch_message(payload.message_id)

                await current_msg.remove_reaction( "✅", payload.member)

                report_author = self.client.get_user(int(current_msg.embeds[0].fields[0].value.split("`")[3]))
                report_log_url = (current_msg.embeds[0].fields[1].value.split(" ")[7])
                
                log_channel = self.client.get_channel(int(report_log_url.split("/")[5]))
                log_message = await log_channel.fetch_message(int(report_log_url.split("/")[6]))

                report_for_user = self.client.get_user(int(log_message.embeds[0].fields[0].value.split("`")[3]))

                report_reason_req = await current_channel.send("Please send the blacklist reason")
                report_reason = await self.client.wait_for("message", check=lambda m:m.author==payload.member and m.channel.id==current_channel.id)
                await report_reason.delete()
                await report_reason_req.delete()

                Database.add_blacklist(report_for_user.id, report_reason.content)

                if report_for_user.dm_channel is None:
                    target_dm = await report_for_user.create_dm()
                else:
                    target_dm = report_for_user.dm_channel

                await target_dm.send(f"You have been blacklisted from sending Disconym messages by `{payload.member.name}` for `{report_reason.content}`")
                await report_author.dm_channel.send(f"Your report has been accepted by `{payload.member.name}`")
                


def setup(client):
    client.add_cog(Report(client))