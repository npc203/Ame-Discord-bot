import discord
import os
from discord.ext import commands
import datetime
client = commands.Bot(command_prefix='--')
client.remove_command('help')
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
     client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    print("ready")
@client.event
async def on_command(ctx):
    await client.get_channel(743038667362140262).send(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+','+str(ctx.command)+','+str(ctx.guild)+','+str(ctx.channel)+','+str(ctx.message.author)+'\n')
    #print(ctx.command,ctx.guild,ctx.channel,ctx.message.author)

@client.event
async def on_command_error(ctx,err):
    if isinstance(err,commands.CommandNotFound):
        await ctx.send("```You either suck at typing or the command doesn't exist```")
    elif isinstance(err, commands.CommandOnCooldown):
            msg = 'UwU Don\'t abuse me senpai,try again in {:.2f}s'.format(err.retry_after)
            await ctx.send(msg)
    await client.get_channel(745259187457490946).send(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+','+str(ctx.command)+','+str(ctx.message.author)+','+str(ctx.guild)+','+type(err).__name__)

'''
@client.command()
async def help(ctx):
    embed=discord.Embed(colour=discord.Colour.orange())
    embed.set_author(name="Bot commands",icon_url="https://cdn.discordapp.com/avatars/601962388006109195/fb5e87a846e7e7ce12f07109f0a71802.png")
    embed.add_field(name='Information',value="ping,wiki",inline=True)
    embed.add_field(name='Chats',value="uwu,owo,xwx",inline=True)
    embed.add_field(name='Under construction',value="gomenasai",inline=False)
    await ctx.send(embed=embed)
'''

with open('token.txt','r') as f:
    token=f.read()
client.run(token)
