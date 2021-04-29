import discord

prefix = "dn"
client = commands.Bot(command_prefix=prefix, intents=intents)

@client.event
async def on_ready():    
    print("Bot is ready")


with open("token.txt","r") as f:
    token = f.read()

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(token)