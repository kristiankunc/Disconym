import discord
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

def find_user_blacklist(user_id):
    prefix_connect()
    
    cursor.execute("SELECT * from blacklist")
    data = cursor.fetchall()

    for row in data:
        if row[0] == user_id:
            return True

    db_connection.close()
    cursor.close()

def prefix_connect():
    global db_connection
    global cursor
    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    cursor = db_connection.cursor()

class Send(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def send(self, ctx, target: discord.Member, *, input_message):

        if isinstance(ctx.channel, discord.channel.DMChannel):

            if find_user_blacklist(ctx.author.id) == True:
                await ctx.send("Error, you are blacklisted from sending Disconym messages")

            else:
                target_dm = target.dm_channel
                if target_dm is None:
                    target_dm = await target.create_dm()

                embed=discord.Embed(title="New Disconym message", description=input_message, color=0x169cdf)
                embed.set_footer(text="Sent using Disconym - Anynymous Discord messanger")
                send_msg = await target_dm.send(embed=embed)

                await ctx.send(f"Message to {target.mention} has been delivered succesfully ")

                await send_msg.add_reaction("❌")


def setup(client):
    client.add_cog(Send(client))