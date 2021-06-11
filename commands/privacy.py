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
        with open ("privacy.md", "r") as f:
            privacy_text = f.read()

        await ctx.send(privacy_text)

def setup(client):
    client.add_cog(Privacy(client))