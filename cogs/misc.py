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
    async def punish(self,ctx,name,times:int):
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
    @commands.command(help='Shows the help command')
    async def help(self,ctx,*cog):
        # *cog indicates cog or a command
        if not cog:
            full = discord.Embed(title='Help',url='https://www.youtube.com/watch?v=oHg5SJYRHA0',description='Use `--help <command>` to find out more about them!',colour=discord.Colour.green())
            cogs_desc = ''
            for x in self.bot.cogs:
                cogs_desc += ('{} : `{}`'.format(x,'`,`'.join([cmd.name for cmd in self.bot.get_cog(x).get_commands()])+'\n'))
            full.add_field(name="Categories:",value=cogs_desc,inline=False)
            full.set_footer(text='Tip: you can also use --info <category>')
            await ctx.send('',embed=full)
        else:
            command = self.bot.get_command(cog[0])
            if command is None:
                cmd_embed = discord.Embed(title='Error!',description='Gomenasai, given command doesn\'t exist : "'+cog[0]+'"',color=discord.Color.red())
            else:
                cmd_embed = discord.Embed(title=cog[0],url='https://www.youtube.com/watch?v=oHg5SJYRHA0',description=command.help,colour=discord.Colour.green())
                if command.aliases:
                    cmd_embed.set_footer(text='aliases: {}'.format(', '.join(command.aliases)))
                else:
                    cmd_embed.set_footer(text='aliases: None')
            await ctx.send(embed=cmd_embed)
    
    @commands.command(help='Gets info about a Specific Category')
    async def info(self,ctx,*args):
        if not args:
            specific_cog = discord.Embed(title='Error!',description='Gomenasai, Senpai needs to type something',color=discord.Color.red())
        else:
            cog = self.bot.get_cog(args[0])
            if cog is None:
                specific_cog = discord.Embed(title='Error!',description='Gomenasai, given Category doesn\'t exist :"'+args[0]+'"',color=discord.Color.red())
            else:
                specific_cog = discord.Embed(title=cog.qualified_name,url='https://www.youtube.com/watch?v=oHg5SJYRHA0',description=cog.__doc__,colour=discord.Colour.green())
                #print(cog, type(cog), cog.get_commands())
                count=1
                for c in cog.get_commands():
                    if not c.hidden:
                        #print(c.name,c.help)
                        specific_cog.add_field(name=f"{count}."+c.name,value=c.help,inline=False)
                    count+=1
                specific_cog.set_footer(text='Tip: You can use --help <command> for more info')
        await ctx.send(embed=specific_cog)

def setup(bot):
    bot.add_cog(Admin(bot))