from discord.ext import commands, tasks
from db_actions import Database
class ApiLoop(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.update_api.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=15)
    async def update_api(self):
        await self.client.wait_until_ready()
        guilds = len(self.client.guilds)
        Database.update_api_data(int(guilds))
        
        
def setup(client):
    client.add_cog(ApiLoop(client))