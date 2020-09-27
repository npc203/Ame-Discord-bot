import discord
from discord.ext import commands
from discord.ext.commands import Cog
import random,time,requests
import asyncio
class Fun(Cog):
    """Has a bunch of fun commands"""
    def __init__(self, bot):
        self.bot = bot
        self.perms=("Admin","Owner","Co-Owner")
        
    @commands.command(hidden=True)
    async def setup(self,ctx):
        #Automate this command
        if str(ctx.message.author) == 'epic guy#0715':
            self.links = self.bot.get_channel(747063339447877753)
            self.db = self.bot.get_channel(755839409768759487)
            self.serverinfo = {}
            for i in await self.db.history(limit=100).flatten():
                temp=[int(i) for i in i.content.split(',')]
                self.serverinfo[self.bot.get_guild(temp[0])]=(self.bot.get_channel(temp[1]),int(temp[2]))
                time.sleep(0.5)
            print(self.serverinfo)
            await ctx.send("Automate this pls :(")
        else:
            await ctx.send("You aren't *high* enough")

    @commands.command(help='invite the bot to other servers',aliases=["about"])
    async def invite(self,ctx):
        embed = discord.Embed(title="Ame", colour=discord.Colour(0x9b59b6), url="https://discord.com/api/oauth2/authorize?client_id=601962388006109195&permissions=537263168&scope=bot",
         description="A Developemental bot with fun commands, with a slight touch of anime theme. Please don't abuse my poor creation UwU")
        embed.set_thumbnail(url="https://media1.tenor.com/images/3254d98bf26b162bb4960483402918e7/tenor.gif")
        embed.add_field(name="Invite Link", value="Click [here](https://discord.com/api/oauth2/authorize?client_id=601962388006109195&permissions=537263168&scope=bot) to add the bot to your other servers")
        await ctx.send(embed=embed)

    
    @commands.command(help='Use this to assign the facts channel')
    async def assign(self,ctx):
        if len([x for x in [str(i.name) for i in ctx.message.author.roles] if x in self.perms])>0:
            await ctx.message.delete()
            if ctx.message.guild in self.serverinfo:
                channel = self.bot.get_channel(755839409768759487)
                msg = await channel.fetch_message(self.serverinfo[ctx.message.guild][1])
                await msg.edit(content=str(ctx.message.guild.id)+','+str(ctx.message.channel.id)+','+str(msg.id))
                self.serverinfo[ctx.message.guild]=(ctx.message.channel,msg.id)
            else:
                sent = await self.db.send(str(ctx.message.guild.id)+','+str(ctx.message.channel.id))
                await sent.edit(content=sent.content+','+str(sent.id))
                self.serverinfo[ctx.message.guild]=(ctx.message.channel,sent.id)
            print(self.serverinfo)
            await ctx.send('Successfully assigned this text channel as the Facts channel, pls delete this message')
        else:
            await ctx.send('Senpai!,you need to be high enough OwO.')

    #@commands.cooldown(1, 7, commands.BucketType.user)
    @commands.command(help='1.add\n2.list\n3.no argument = random fact')
    async def facts(self,ctx,*args):   
        if ctx.message.guild not in self.serverinfo:
            await ctx.send('Please create a new channel.||Preferrable hidden from everyone except staff and the bot|| and use the --assign command to assign the facts channel.')
        else:
            try:
                a=(await self.serverinfo[ctx.message.guild][0].history(limit=300).flatten())
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
                            await show.edit(content='Timeout, Fact List is closed uwu')
                            break
                    else:
                        await ctx.send('```'+"Why are you gay?"+'```')
                elif args[0]=='add':
                    msg=' '.join(args[1:])
                    await self.serverinfo[ctx.message.guild][0].send(msg)
                    await ctx.send("```yaml\nfact added: "+msg+"\nby: "+str(ctx.message.author)+"```")
                else:
                    await ctx.send('Error, you suck at typing kiddo, '+str(ctx.message.author))
            else:
                await ctx.send('```yaml\nSIKE, Not enough permissions NOOB\nfact failed to add/manipulate: '+' '.join(args[1:])+"\nby: "+str(ctx.message.author)+'```')

    @commands.command(aliases=['dog', 'cat',"truth"],hidden=True)
    async def surprise(self,ctx,*args):
        await ctx.message.delete()
        try:
            a=(await self.links.history(limit=50).flatten())
        except IndexError:
            await ctx.send("Database error")
        await ctx.send(("Requested by: "+str(ctx.message.author)+"\n"+random.choice([i.content for i in a])))      

    @commands.command(help='Tells whatever is given as the sentence, mimicing mentioned user\'s identity and name',aliases=['ts'])
    async def tellas(self,ctx,mention='',*sentence):
        if mention[2] != '!': #If the user is in android
            mention = '<@!'+mention[2:]
        if ctx.message.mentions and sentence:
            target= ctx.message.mentions[0] 
            if mention[3:-1]==str(target.id):
                await ctx.message.delete()
                for i in await ctx.channel.webhooks():
                    if i.user.id == self.bot.user.id:
                        hook = i
                        break
                else:
                    hook = await ctx.channel.create_webhook(name='bot_hook_'+str(ctx.channel)) 
                await hook.send(username=target.display_name,avatar_url=target.avatar_url,content=' '.join(sentence))
        else:
            await ctx.send('Senpai, u need to {} baka!'.format('mention someone' if sentence else 'type something'))
    

def setup(bot):
    bot.add_cog(Fun(bot))