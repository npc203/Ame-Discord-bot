import requests
from html import unescape
from bs4 import BeautifulSoup
import wikipedia
import discord
from discord.ext import commands
from discord.ext.commands import Cog
import random,json,datetime

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
        s = e.options[0]
        p = wikipedia.page(s).summary
    return p

class Info(Cog):
    """Getting stuff from the Internet"""
    def __init__(self,bot):
        self.headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
        self.URL = 'https://www.planetminecraft.com/server/emeraldbattlecraft-2702726/'
        self.bot=bot
        with open('data/quotes.json') as f:
            self.quotes = json.load(f)
        
        
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.command(help="Get's the player count in EBC")
    async def ping(self,ctx):
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
        
        #await ctx.send("```Players Online: "+soup.find("table").find(class_='stat').text+"\n"+','.join([i.text.replace('\n','') for i in soup.find_all(class_="mbl-user")])+"```")
        
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(help="Get's a random joke")
    async def joke(self,ctx):
        r=json.loads(requests.get("https://official-joke-api.appspot.com/random_joke").text)
        await  ctx.send('```'+r["setup"]+'\n'+r["punchline"]+'```')

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(help="Get's a random quote/big brain from the internet")
    async def quote(self,ctx):
        tell = random.choice(self.quotes)
        await ctx.send('```'+tell['quote']+'\nby:'+tell['author']+'```')

    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.command(help='Throws random wiki articles \n if argument is given, tries to get the specified page \n [Very unreliable] ')
    async def wiki(self,ctx,*arg):
        if not arg:
            await ctx.send(random_page())
        else:
            await ctx.send(specific_page(' '.join(arg)))
    
    @commands.cooldown(1, 20, commands.BucketType.user)
    @commands.command(help="Show's your avatar")
    async def avatar(self,ctx,*args):
        embed = discord.Embed(colour=discord.Colour.blue())
        if (ctx.message.mentions.__len__()>0):
            embed.set_image(url=ctx.message.mentions[0].avatar_url)
            embed.set_footer(text=ctx.message.mentions[0].display_name+" senpai looks cool! UwU")
        else:
            embed.set_image(url=ctx.message.author.avatar_url)
            embed.set_footer(text="You look nice senpai! UwU")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
