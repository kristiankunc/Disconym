import discord
import json
from pathlib import Path
from discord.ext import commands
import mysql.connector as mysql

main_folder = Path("/")
prefixes_file = main_folder / "db_data.txt"

with open("db_data.txt","r") as f:
    lines = f.readlines()
    HOST = lines[0]
    DATABASE = lines[1]
    USER = lines[2]
    PASSWORD = lines[3]

db_connection = None
cursor = None

def remove_prefix(guild_id):
    db_connect()

    delete_query = f"DELETE FROM prefixes WHERE guild_id = '{int(guild_id)}'"
    cursor.execute(delete_query)
    db_connection.commit()

    db_connection.close()
    cursor.close()
    
def add_prefix(guild_id, prefix):
    db_connect()

    insert_query = f"INSERT INTO prefixes (guild_id, prefix) VALUES ({int(guild_id)}, '{str(prefix)}')"
    cursor.execute(insert_query)
    db_connection.commit()

    db_connection.close()
    cursor.close()

def db_connect():
    global db_connection
    global cursor
    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    cursor = db_connection.cursor()

class Prefix(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True) 
    async def prefix(self, ctx, prefix):
        remove_prefix(ctx.guild.id)
        add_prefix(ctx.guild.id, prefix)

        await ctx.send(f'Prefix changed to: {prefix}')

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        add_prefix(guild.id, ".")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        remove_prefix(guild.id)

def setup(client):
    client.add_cog(Prefix(client))