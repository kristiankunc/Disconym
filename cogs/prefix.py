import discord
import json
from pathlib import Path
from discord.ext import commands

data_folder = Path("database/")
prefixes_file = data_folder / "prefixes.json"

class Prefix(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True) 
    async def prefix(self, ctx, prefix):

        with open(prefixes_file, 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open(prefixes_file, 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'Prefix changed to: {prefix}')
        name=f'{prefix}BotBot'


        @commands.Cog.listener()
        async def on_guild_join(self, guild):
            print("joined")
            with open('prefixes.json', 'r') as f:
                prefixes = json.load(f)

            prefixes[str(self.guild.id)] = 'bl!'

            with open('prefixes.json', 'w') as f:
                json.dump(prefixes, f, indent=4)

        @commands.Cog.listener()
        async def on_guild_remove(self, guild):
            print("left")
            with open('prefixes.json', 'r') as f:
                prefixes = json.load(f)

            prefixes.pop(str(self.guild.id))

            with open('prefixes.json', 'w') as f:
                json.dump(prefixes, f, indent=4)

def setup(client):
    client.add_cog(Prefix(client))