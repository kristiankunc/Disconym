import discord
import os
import json
from discord.ext import commands
from db_actions import Database
from discord_slash import SlashCommand

intents = discord.Intents.default()
intents.members = True
    
def get_prefix(client, message):
    if message.guild == None:
        return "!"
    else:
        try:
            return Database.find_prefix(message.guild.id)
        except:
            Database.add_prefix(message.guild.id, ".")
            return "."

client = commands.Bot(command_prefix= (get_prefix), intents=intents, case_insensitive=True)
slash = SlashCommand(client, sync_commands=True, sync_on_cog_reload=True)

client.remove_command('help')

ignored_cogs = ["__init__.py"]

for filename in os.listdir("./commands"):
    if filename.endswith(".py") and filename not in ignored_cogs:
        client.load_extension(f"commands.{filename[:-3]}")

for filename in os.listdir("./functions"):
    if filename.endswith(".py") and filename not in ignored_cogs:
        client.load_extension(f"functions.{filename[:-3]}")

with open('config.json',) as f:
    config = json.load(f)
    token = config["token"]

client.run(token)