import discord
import os
import json
from pathlib import Path
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

data_folder = Path("database/")
prefixes_file = data_folder / "prefixes.json"

def get_prefix(client, message):
    with open(prefixes_file, 'r') as f:
        prefixes = json.load(f)
        try:
            return prefixes[str(message.guild.id)]
        except:
            return "!"

client = commands.Bot(command_prefix= (get_prefix), intents=intents)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


@client.command()
async def ping(ctx):
    await ctx.channel.send("Pong")


with open("token.txt","r") as f:
    token = f.read()


client.run(token)