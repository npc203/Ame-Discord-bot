import discord
from discord.ext import commands
from discord.ext.commands import Cog,has_permissions
import random
class Admin(Cog):
    """Has some administration related commands"""
    def __init__(self,bot):
        self.limit=50
        self.bot = bot

    async def cog_check(self, ctx):
        if len([x for x in [str(i.name) for i in ctx.message.author.roles] if x in ("Admin","Owner","Co-Owner")])>0:
            return True
        else:
            await ctx.send("Senpai, You aren't ***high*** enough")
            return False

    @commands.command(help='Meant for Pinging the given name on every available text channel \n You need to have Owner/Admin/Co-Owner role to use this command')
    async def punish(self,ctx,name,times):
        try:
            times=int(times)
        except ValueError:
            ctx.send("Senpai, U need to give the command in the format `--punish <mention person> <number of times>` OwO")
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
        print("It is done")
    
    @commands.command(help='Cleans the mess made by punish command \n You need to have Owner/Admin/Co-Owner role to use this command',hidden=True)
    async def clean(self,ctx,times):
        await ctx.message.delete()    
        if times>self.limit:
            await ctx.send("Pls don't abuse me senpai uwu") 
        else:   
            for channel in ctx.guild.text_channels:
                try:
                    await channel.purge(limit=int(times))
                except:
                    print("Skipped: #",channel,sep='')
        print("It is done")

    @commands.command(help='Deletes messages upto the given limit in the present channel \n You need to have Owner/Admin/Co-Owner role to use this command')
    async def purge(self,ctx,limit:int):
        await ctx.message.delete()
        if limit>self.limit:
            await ctx.send("Pls don't abuse me senpai uwu")
        else:
            await ctx.channel.purge(limit=limit)

    
    @commands.command(help='SPAMS \n You need to have Owner/Admin/Co-Owner role to use this command')
    async def spam(self,ctx,*args):
        if int(args[-1]) > self.limit:
            await ctx.send("Pls don't abuse me senpai uwu")
        else:
            for i in range(int(args[-1])):
                await ctx.send(' '.join(args[:-1]))

    @has_permissions(manage_channels=True)
    @commands.command(help='Changes topic of the channel')
    async def topic(self,ctx,*,text):
        await ctx.channel.edit(topic=text)
    
    @commands.group(pass_context=True, invoke_without_command=True)
    async def ticket(self,ctx,*args):
        if args:
            if ctx.invoked_subcommand is None:
                await ctx.send('Invalid Ticket command passed...')
        else:
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                ctx.guild.me: discord.PermissionOverwrite(read_messages=True)
            }

            channel = await ctx.guild.create_text_channel(f'ticket-{ctx.author.name}-{ctx.author.discriminator}')
            await channel.send("Use `--close` or `--ticket close` to delete this channel")
            success = discord.Embed(title = "Successfully Created a Ticket",description=f"Created the channel:<#{channel.id}>")
            success.set_thumbnail(url="http://clipart-library.com/images_k/movie-ticket-transparent/movie-ticket-transparent-20.jpg")
            await ctx.send(embed = success)
           
    
    @ticket.command()
    async def delete(self,ctx):
        check = ctx.channel.name.split('-')
        if len(check)>0 and check[0]=="ticket":
            await ctx.channel.delete()
        else:
            await ctx.send("Not a valid ticket channel")

    @commands.command(name='close')
    async def actual_command(self,ctx):
        await self.delete(ctx)
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