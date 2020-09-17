import discord
from discord.ext import commands
from discord.ext.commands import Cog
import random,requests
class Admin(Cog):
    """Has some administration related commands"""
    def __init__(self,bot):
        self.perms=("Admin","Owner")
        self.limit=50
        self.bot = bot
    @commands.command(help='Meant for Pinging the given name on every available text channel \n only epic people can use it')
    async def punish(self,ctx,name,times):
        try:
            times=int(times)
        except ValueError:
            ctx.send("Senpai, U need to give the command in the format `--punish <mention person> <number of times>` OwO")
        if len([x for x in [str(i.name) for i in ctx.message.author.roles] if x in self.perms])>0:
                await ctx.message.delete()
                if times>self.limit:
                    await ctx.send("Pls don't abuse me senpai uwu")
                else:
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
                if times>self.limit:
                    await ctx.send("Pls don't abuse me senpai uwu") 
                else:   
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
    async def purge(self,ctx,limit:int):
        #print([str(i.name) for i in ctx.message.author.roles],self.perms )
        if len([x for x in [str(i.name) for i in ctx.message.author.roles] if x in self.perms])>0:
            await ctx.message.delete()
            if limit>self.limit:
                await ctx.send("Pls don't abuse me senpai uwu")
            else:
                await ctx.channel.purge(limit=limit)
        else:
            await ctx.send("***There was an attempt***")
    
    @commands.command(help='SPAMS \n only epic people can use it')
    async def spam(self,ctx,*args):
        if len([x for x in [str(i.name) for i in ctx.message.author.roles] if x in self.perms])>0:
            if int(args[-1]) > self.limit:
                await ctx.send("Pls don't abuse me senpai uwu")
            else:
                for i in range(int(args[-1])):
                    await ctx.send(' '.join(args[:-1]))
        else:
            await ctx.send("***There was an attempt***")
    '''
     #help section copy pasta, not so good   
    @commands.command(pass_context=True)
    @commands.has_permissions(add_reactions=True,embed_links=True)
    async def help(self,ctx,*cog):
        """Gets all cogs and commands of mine."""
        try:
            if not cog:
                """Cog listing.  What more?"""
                halp=discord.Embed(title='All my commands senpai',
                                description='Use `--help *item*` to find out more about them!')
                cogs_desc = ''
                for x in self.bot.cogs:
                    cogs_desc += ('{} : {}'.format(x,self.bot.cogs[x].__doc__)+'\n')
                halp.add_field(name='Categories:\n',value=cogs_desc[0:len(cogs_desc)-1],inline=False)
                cmds_desc = ''
                for y in self.bot.walk_commands():
                    if not y.cog_name and not y.hidden:
                        cmds_desc += ('{} - {}'.format(y.name,y.help)+'\n')
                #halp.add_field(name='Uncatergorized Commands',value=cmds_desc[0:len(cmds_desc)-1],inline=False)
                await ctx.message.add_reaction(emoji='✉')
                await ctx.message.author.send('',embed=halp)
            else:
                """Helps me remind you if you pass too many args."""
                if len(cog) > 1:
                    halp = discord.Embed(title='Error!',description='That is way too many cogs!',color=discord.Color.red())
                    await ctx.message.author.send('',embed=halp)
                else:
                    """Command listing within a cog."""
                    found = False
                    for x in self.bot.cogs:
                        for y in cog:
                            if x == y:
                                halp=discord.Embed(title=cog[0]+' Command List',description=self.bot.cogs[cog[0]].__doc__)
                                for c in self.bot.get_cog(y).get_commands():
                                    if not c.hidden:
                                        halp.add_field(name=c.name,value=c.help,inline=False)
                                found = True
                    if not found:
                        """Reminds you if that cog doesn't exist."""
                        halp = discord.Embed(title='Error!',description='How do you even use "'+cog[0]+'"?',color=discord.Color.red())
                    else:
                        await ctx.message.add_reaction(emoji='✉')
                    await ctx.message.author.send('',embed=halp)
        except Exception as e:
            print(e)
            await ctx.send("Excuse me, I can't send embeds.")
    '''

def setup(bot):
    bot.add_cog(Admin(bot))