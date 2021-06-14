import discord
import datetime
from discord.ext import commands
from db_actions import Database
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option

class Prefix(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash  (name="prefix",
                        description="Change the prefix for this guild",
                        options=[
                            create_option(
                            name="prefix",
                            description="Your desired prefix",
                            option_type=3,
                            required=True
                            )
                        ])
    async def _prefix(self, ctx: SlashContext, prefix: str):
        await self.prefix(ctx, prefix)

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True) 
    async def prefix(self, ctx, prefix):
        bot_name = self.client.user.name
        bot_pfp = self.client.user.avatar_url

        Database.replace_prefix(ctx.guild.id, prefix)

        embed=discord.Embed(title = "Prefix changed", description = f"Prefix for **{ctx.guild.name}** has been changed to `{prefix}`", color=0x08ccfd)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=bot_name, icon_url=bot_pfp)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        Database.add_prefix(guild.id, ".")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        Database.remove_prefix(guild.id)

def setup(client):
    client.add_cog(Prefix(client))