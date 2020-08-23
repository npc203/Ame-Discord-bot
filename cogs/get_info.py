import requests
from html import unescape
from bs4 import BeautifulSoup
import wikipedia
import discord
from discord.ext import commands
from discord.ext.commands import Cog
import random,json
from joke.jokes import *
from joke.quotes import *

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

class Information(Cog):
    """Getting stuff from the Internet"""
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
        self.URL = 'https://www.planetminecraft.com/server/emeraldbattlecraft-2702726/'
        
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.command(help="Get's the player count in EBC")
    async def ping(self,ctx):
        page = requests.get(self.URL,headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        embed = discord.Embed(title='EmeraldBattleCraft',url='https://www.planetminecraft.com/server/emeraldbattlecraft-2702726/',colour=discord.Colour.purple())
        #embed.set_author(name="EmeraldBattleCraft")
        embed.set_thumbnail(url="https://i.imgur.com/fXjogry.png")
        embed.set_footer(text="Warning: This isn't realtime!, The info is taken from the website.")
        embed.add_field(name='Members Online: ',value=soup.find("table").find(class_='stat').text,inline=False)
        embed.add_field(name='Players:',value=','.join([i.text.replace('\n','') for i in soup.find_all(class_="mbl-user")]),inline=False)
        #await ctx.send("```Players Online: "+soup.find("table").find(class_='stat').text+"\n"+','.join([i.text.replace('\n','') for i in soup.find_all(class_="mbl-user")])+"```")
        await ctx.send(embed=embed)
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.command(help="Get's a random joke")
    async def joke(self,ctx):
        r=json.loads(requests.get("https://official-joke-api.appspot.com/random_joke").text)
        await  ctx.send('```'+r["setup"]+'\n'+r["punchline"]+'```')

    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.command(help="Get's a random quote/big brain from the internet")
    async def quote(self,ctx):
        a=random.choice([stormconsultancy, quotesondesign])
        #print("getting stuff from:"+str(a))
        if a==quotesondesign:
            await  ctx.send(unescape(random.choice(a(1))).replace('<p>','').replace('</p>',''))
        else:
             await  ctx.send(unescape(a()))

    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.command(help='Throws random wiki articles \n if argument is given, tries to get the specified page \n [Very unreliable] ')
    async def wiki(self,ctx,*arg):
        if not arg:
            await ctx.send(random_page())
        else:
            await ctx.send(specific_page(' '.join(arg)))
    
    @wiki.error
    @ping.error
    @joke.error
    @quote.error
    async def cool_dude(self,ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg = 'UwU Don\'t abuse me senpai,try again in {:.2f}s'.format(error.retry_after)
            await ctx.send(msg)
        else:
            raise error

def setup(bot):
    bot.add_cog(Information())
