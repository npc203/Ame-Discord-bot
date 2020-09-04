import discord
from discord.ext import commands
from discord.ext.commands import Cog
import random
import asyncio
class Fun(Cog):
    """Has a bunch of fun commands"""
    def __init__(self, bot):
        self.bot = bot
        self.perms=("Admin","Owner","Co-Owner")
        self.setup()
    
    def setup(self):
        #this stuff is expected to work but it aint working, PLS DO SOMETHING, its not an async error
        #the fix i did was...call the self.links again in their respective call functions (adds stress on computation)
        self.links = self.bot.get_channel(747063339447877753)
        self.db = self.bot.get_channel(743058819545956384)
    
    #@commands.cooldown(1, 7, commands.BucketType.user)
    @commands.command(help='1.add\n2.list\n3.no argument = random fact')
    async def facts(self,ctx,*args):   
        self.db = self.bot.get_channel(743058819545956384)
        try:
            a=(await self.db.history(limit=500).flatten())
            size = len(a)//10+1
        except IndexError:
            await ctx.send("Database error")    
        if not args:
            await ctx.send('```'+random.choice([i.content for i in a])+'```')
        elif len([x for x in [str(i.name) for i in ctx.message.author.roles] if x in self.perms])>0:
            await ctx.message.delete() 
            def check(reaction, user):
                #return str(reaction.emoji) in ['⬅️', '➡️']
                return user == ctx.message.author and str(reaction.emoji) in ['⬅️', '➡️']  
            if args[0]=='list':       
                page= 1
                actual=[str(i)+'. '+a for i,a in enumerate([i.content for i in a],1)]
                show = await ctx.send('```'+'Facts List:\n\n'+'\n'.join(actual[:10])+f'\n\n\npage {page}/{size}'+'```')
                await show.add_reaction( '⬅️')
                await show.add_reaction('➡️')                  
                while True:
                    try:
                        reaction, user = await self.bot.wait_for('reaction_add', timeout=60,check = check)
                        #print(reaction.emoji)
                        if reaction.emoji == '⬅️' and page-1>0:
                            page -= 1
                        elif reaction.emoji == '➡️' and page+1<=size:
                            page += 1
                        await show.edit(content='```'+'Facts List:\n\n'+'\n'.join(actual[(page-1)*10:page*10])+f'\n\npage {page}/{size}'+'```')
                        
                    except asyncio.TimeoutError:
                        await show.edit(content='Timeout, facts closed uwu')
                        break
                else:
                    await ctx.send('```'+"Why are you gay?"+'```')
            elif args[0]=='add':
                msg=' '.join(args[1:])
                await self.db.send(msg)
                await ctx.send("```yaml\nfact added: "+msg+"\nby: "+str(ctx.message.author)+"```")
            else:
                await ctx.send('Error, you suck at typing kiddo, '+str(ctx.message.author))
        else:
            await ctx.send('```yaml\nSIKE, Not enough permissions NOOB\nfact failed to add/manipulate: '+' '.join(args[1:])+"\nby: "+str(ctx.message.author)+'```')

    @commands.command(aliases=['dog', 'cat',"truth"],hidden=True)
    async def surprise(self,ctx,*args):
        await ctx.message.delete()
        try:
            self.links = self.bot.get_channel(747063339447877753)
            a=(await self.links.history(limit=50).flatten())
        except IndexError:
            await ctx.send("Database error")
        await ctx.send(("Requested by: "+str(ctx.message.author)+"\n"+random.choice([i.content for i in a])))      

def setup(bot):
    bot.add_cog(Fun(bot))