import discord
import os
import json
from pathlib import Path
from discord.ext import commands
import mysql.connector as mysql

intents = discord.Intents.default()
intents.members = True

db_connection = None
cursor = None

with open("db_data.txt","r") as f:
    lines = f.readlines()
    HOST = lines[0]
    DATABASE = lines[1]
    USER = lines[2]
    PASSWORD = lines[3]

def db_connect():
    global db_connection
    global cursor
    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    cursor = db_connection.cursor()

def get_prefix(client, message):

    db_connect()

    cursor.execute("SELECT * from prefixes")
    data = cursor.fetchall()

    try:
        guild_id = message.guild.id
    except:
        return "!"

    for row in data:
        if row[0] == message.guild.id:
            return str(row[1])

    db_connection.close()
    cursor.close()

client = commands.Bot(command_prefix= (get_prefix), intents=intents)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

with open("token.txt","r") as f:
    token = f.read()


client.run(token)