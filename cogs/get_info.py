import requests
from html import unescape
from bs4 import BeautifulSoup
import wikipedia
import discord
from discord.ext import commands
from discord.ext.commands import Cog
import random,json,datetime
import asyncio

def random_page():
   random = wikipedia.random(1)
   try:
       result = wikipedia.page(random).summary
   except wikipedia.exceptions.DisambiguationError as e:
       result = random_page()
   return result

def specific_page(string):
    try:
        p = wikipedia.page(string).summary
    except wikipedia.DisambiguationError as e:
        return e.options
    except wikipedia.exceptions.PageError as e:
        return "No Results Found Senpai, Use Google rather 😓"
    return p

class Info(Cog):
    """Getting stuff from the Internet"""
    def __init__(self,bot):
        self.headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
        self.URL = 'https://www.planetminecraft.com/server/emeraldbattlecraft-2702726/'
        self.bot=bot
        with open('data/quotes.json') as f:
            self.quotes = json.load(f)
        with open('data/love.txt','r',encoding="utf8") as f:
            self.love = f.readlines() 
        
        
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.command(help="1. --ping     : Sends the bot latency,\n 2. --ping ebc : Get's the player count in EBC")
    async def ping(self,ctx,*args):
        if not args:
            await ctx.send(f'Pong! in `{round(self.bot.latency * 1000)}ms`')
        else:
            page = requests.get(self.URL,headers=self.headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            embed = discord.Embed(title='EmeraldBattleCraft',url='https://www.planetminecraft.com/server/emeraldbattlecraft-2702726/',colour=discord.Colour.purple())
            #embed.set_author(name="EmeraldBattleCraft")
            embed.set_thumbnail(url="https://i.imgur.com/fXjogry.png")
            embed.set_footer(text="Warning: This isn't realtime!, The info is taken from the website.")
            table=soup.find("table")
        
            try:
                embed.add_field(name='Members Online: ',value=table.find(class_='stat').text,inline=False)
                embed.add_field(name='Players:',value=','.join([i.text.replace('\n','') for i in soup.find_all(class_="mbl-user")]),inline=False)
                await ctx.send(embed=embed)
            except Exception as e:
                embed.add_field(name='Members Online: ',value='0/20',inline=False)
                embed.add_field(name='Players:',value='No one here :(',inline=False)
                await self.bot.get_channel(745259187457490946).send(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+','+str(ctx.command)+','+str(ctx.message.author)+','+str(ctx.guild)+','+"EBC 0 player")
                await ctx.send(embed=embed) 
            del soup,page,table,embed
            
            #await ctx.send("```Players Online: "+soup.find("table").find(class_='stat').text+"\n"+','.join([i.text.replace('\n','') for i in soup.find_all(class_="mbl-user")])+"```")
        
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(help="Get's a random joke")
    async def joke(self,ctx):
        r=json.loads(requests.get("https://official-joke-api.appspot.com/random_joke").text)
        await  ctx.send('```'+r["setup"]+'\n'+r["punchline"]+'```')
        del r

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(help="Get's a random quote/big brain from the internet\n --quote love gives love quotes (probably)")
    async def quote(self,ctx,*args):
        if not args:
            tell = random.choice(self.quotes)
            await ctx.send('```'+tell['quote']+'\nby:'+tell['author']+'```')
        elif args[0]=='love':
            await ctx.send('```'+random.choice(self.love)+'```')

    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.command(help='Throws random wiki articles \n if argument is given, tries to get the specified page \n [Very unreliable] ')
    async def wiki(self,ctx,*,text):
        if not text:
            value = random_page()
        else:
            value = specific_page(text)
            if type(value) == list:
                value = value[:10] if len(value) > 10 else value
                pack = ('1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟')
                def check(reaction, user):
                    return user == ctx.message.author and str(reaction.emoji) in pack
                #Make the user pick the option
                embed = discord.Embed(title="Pick an Option:",url="https://www.youtube.com/watch?v=oHg5SJYRHA0")
                for i in range(len(value)):
                    embed.add_field(name=pack[i]+" "+value[i],value="​",inline=False)
                embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/foundation/thumb/2/20/Wikipedia-logo-v2-en_SVG.svg/200px-Wikipedia-logo-v2-en_SVG.svg.png')
                show = await ctx.send(embed=embed)
                [await show.add_reaction(pack[i]) for i in range(len(value))]
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60,check = check)
                    await show.delete()
                    value = wikipedia.page(value[pack.index(str(reaction))]).summary
                except asyncio.TimeoutError:
                    await show.edit(content='Senpai, You need to be a little fast')              
        try:         
            out = await ctx.send(value)
        except:
            paginated_text = self.paginate(value)
            for page in paginated_text:
                if page == paginated_text[-1]:
                    out = await ctx.send(page)
                    break
                await ctx.send(page)
        
    @commands.command(help='Shows the help command')
    async def help(self,ctx,*cog):
        # *cog indicates cog or a command
        if not cog:
            full = discord.Embed(title='Help',url='https://www.youtube.com/watch?v=oHg5SJYRHA0',description='Use `--help <command>` to find out more about them!',colour=discord.Colour.green())
            full.add_field(name="Categories:",value='​')
            for x in filter(lambda x: str(x) != 'Eval', self.bot.cogs):
                full.add_field(name = x , value='`{}`'.format('`,`'.join([cmd.name for cmd in self.bot.get_cog(x).get_commands() if not cmd.hidden])),inline=False)
            full.set_footer(text='Tip: you can also use --info <category>')
            await ctx.send(embed=full)
        else:
            command = self.bot.get_command(cog[0])
            if command is None:
                cmd_embed = discord.Embed(title='Error!',description='Gomenasai, given command doesn\'t exist : "'+cog[0]+'"',color=discord.Color.red())
            else:
                usage='--'+command.name+' '+' '.join([f'<{i[1]}>' for i in list(command.params.items())[2:]])
                cmd_embed = discord.Embed(title=command.name,url='https://www.youtube.com/watch?v=oHg5SJYRHA0',description=f'**Usage:** {usage}',colour=discord.Colour.green())
                cmd_embed.add_field(name='Description:',value=command.help)
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
    
    def paginate(self,text: str):
            '''Simple generator that paginates text.'''
            last = 0
            pages = []
            for curr in range(0, len(text)):
                if curr % 1980 == 0:
                    pages.append(text[last:curr])
                    last = curr
                    appd_index = curr
            if appd_index != len(text)-1:
                pages.append(text[last:curr])
            return list(filter(lambda a: a != '', pages))

def setup(bot):
    bot.add_cog(Info(bot))
