import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

prefix = "dn"
client = commands.Bot(command_prefix=prefix, intents=intents)

@client.event
async def on_ready():
    await setPresence()

    print("-------")
    print('Logged in with details')
    print('------')
    print('Discord bot name is ' + client.user.name)
    print('------')
    print('Discord bot id is ' + str(client.user.id))
    print('------')


def setPresence():
    return client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Your anonymous messages"))



for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

with open("token.txt","r") as f:
    token = f.read()

client.run(token)