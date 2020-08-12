import discord
import os
from discord.ext import commands
import datetime
client = commands.Bot(command_prefix='--')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
     client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    print("ready")
@client.event
async def on_command(ctx):
    with open('logs/all_logs.csv','a') as f:
        f.write(str(datetime.datetime.now())+','+str(ctx.command)+','+str(ctx.guild)+','+str(ctx.channel)+','+str(ctx.message.author)+'\n')
    await client.get_channel(743038667362140262).send(str(datetime.datetime.now())+','+str(ctx.command)+','+str(ctx.guild)+','+str(ctx.channel)+','+str(ctx.message.author)+'\n')
    print(ctx.command,ctx.guild,ctx.channel,ctx.message.author)
with open('token.txt','r') as f:
    token=f.read()
client.run(token)
