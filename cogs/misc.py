import discord
from discord.ext import commands
from discord.ext.commands import Cog
import random,requests
class Miscellaneous(Cog):
    def __init__(self,bot):
        self.perms=("Admin","Owner")
    @commands.command(help='Meant for Pinging the given name on every available text channel \n only epic people can use it')
    async def punish(self,ctx,name,times):
        if len([x for x in [str(i.name) for i in ctx.message.author.roles] if x in self.perms])>0:
                await ctx.message.delete()
                for channel in ctx.guild.text_channels:
                    try:
                        for _ in range(int(times)):
                            await channel.send(name)
                        await channel.purge(limit=int(times))
                    except:
                        print("Skipped: #",channel,sep='')
        else:
            print(type(ctx.message.author),ctx.message.author)
            await ctx.send("```***There was an attempt***```")
        print("It is done")
    
    @commands.command(help='Cleans the mess made by punish command \n only epic people can use it')
    async def clean(self,ctx,times):
        if len([x for x in [str(i.name) for i in ctx.message.author.roles] if x in self.perms])>0:
                await ctx.message.delete()        
                for channel in ctx.guild.text_channels:
                    try:
                        await channel.purge(limit=int(times))
                    except:
                        print("Skipped: #",channel,sep='')
        else:
            #print(type(ctx.message.author),ctx.message.author)
            await ctx.send("```***There was an attempt***```")
        print("It is done")

    @commands.command(help='Deletes messages upto the given limit in the present channel \n only epic people can use it')
    async def purge(self,ctx,limit):
        #print([str(i.name) for i in ctx.message.author.roles],self.perms )
        if len([x for x in [str(i.name) for i in ctx.message.author.roles] if x in self.perms])>0:
            await ctx.message.delete()
            await ctx.channel.purge(limit=int(limit))
        else:
            await ctx.send("***There was an attempt***")
    
    @commands.command(help='SPAMS \n only epic people can use it')
    async def spam(self,ctx,text,limit:int):
        if len([x for x in [str(i.name) for i in ctx.message.author.roles] if x in self.perms])>0:
            for i in range(limit):
                await ctx.send(text)
        else:
            await ctx.send("***There was an attempt***")
        

    

def setup(bot):
    bot.add_cog(Miscellaneous(bot))