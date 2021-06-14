from discord.ext import commands
from db_actions import Database

class Mention(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == f"<@!{self.client.user.id}>":
            prefix = Database.find_prefix(message.guild.id)[0]
            await message.channel.send(f"My prefix here is **{prefix}**\nRun `{prefix}help` for more info about the bot")

def setup(client):
    client.add_cog(Mention(client))