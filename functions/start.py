import discord
from discord.ext import commands

class Start(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):

        def setPresence():
            return self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Your Anonymous messages"))

        await setPresence()
        print("-------")
        print('Logged in with following details:')
        print('------')
        print('Discord bot name is ' + self.client.user.name)
        print('------')
        print('Discord bot ID is ' + str(self.client.user.id))
        print('------')

def setup(client):
    client.add_cog(Start(client))