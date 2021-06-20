from datetime import datetime
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class Privacy(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash  (name="privacy",
                        description="See the privacy policy",
                        )

    async def _privacy(self, ctx: SlashContext):
        await self.privacy_command(ctx)

    @commands.command()
    async def privacy(self, ctx):
        await self.privacy_command(ctx)

    async def privacy_command(self, ctx):
        bot_name = self.client.user.name
        bot_pfp = self.client.user.avatar_url

        with open ("privacy.md", "r") as f:
            privacy_text = f.read()

        privacy_embed=discord.Embed(title="Disconym's Privacy Policy", description=privacy_text, color=0x169cdf)
        privacy_embed.set_footer(text=bot_name, icon_url=bot_pfp)
        privacy_embed.timestamp = datetime.now()
        await ctx.send(embed=privacy_embed)


def setup(client):
    client.add_cog(Privacy(client))