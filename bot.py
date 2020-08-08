import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='--')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
     client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    print("ready")

with open('token.txt','r') as f:
    token=f.read()
client.run(token)
