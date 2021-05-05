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

def prefix_connect():
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
        with open(prefixes_file, 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open(prefixes_file, 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'Prefix changed to: {prefix}')
        name=f'{prefix}BotBot'


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print("added")

        prefix_connect()
        mySql_insert_query = f"INSERT INTO prefixes (guild_id, prefix) VALUES ({int(guild.id)}, '.')"

        cursor.execute(mySql_insert_query)
        db_connection.commit()

        db_connection.close()
        cursor.close()

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        print("removed")

        prefix_connect()
        sql = f"DELETE FROM prefixes WHERE guild_id = '{int(guild.id)}'"

        cursor.execute(sql)
        db_connection.commit()

def setup(client):
    client.add_cog(Prefix(client))