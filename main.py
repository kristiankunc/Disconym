import discord
import os
from pathlib import Path
from discord.ext import commands
import mysql.connector as mysql
from db_actions import Database

intents = discord.Intents.default()
intents.members = True

def get_prefix(client, message):
    if message.guild == None:
        return "!"
    else:
        return Database.find_prefix(message.guild.id)

client = commands.Bot(command_prefix= (get_prefix), intents=intents)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

with open("token.txt","r") as f:
    token = f.read()


client.run(token)