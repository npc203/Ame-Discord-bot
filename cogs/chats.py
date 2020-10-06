import discord
from discord import Webhook
from discord.ext import commands
from discord.ext.commands import Cog
import random
import asyncio,io 
import utils
class Chats(Cog):
    """Weeby commands"""
    def __init__(self, bot):
        self.bot = bot
        self.words = ('insult','sadme')
        with open('data/owo.txt','r',encoding="utf8") as f:
            self.owo=f.readlines()
        with open('data/uwu.txt','r',encoding="utf8") as f:
            self.uwu=f.readlines()
        with open('data/xwx.txt','r',encoding="utf8") as f:
            self.xwx=f.readlines()
        self.cache={}

        
    @commands.command(aliases=['uWu', 'uwu','UWU'],help="Replies with OwO")
    async def UwU(self,ctx,*args):
        if args:
            if args[0]=='c':
                await ctx.message.delete()
        await ctx.send(random.choice(self.owo))  

    @commands.command(aliases=['oWo', 'owo','OWO'],help='Replies with UwU')
    async def OwO(self,ctx,*args):
        if args:
            if args[0]=='c':
                await ctx.message.delete()
        await ctx.send(random.choice(self.uwu))  

    @commands.command(help='Replies with flower girl/yandere girl')
    async def xwx(self,ctx,*args):
        if args:
            if args[0]=='c':
                await ctx.message.delete()
        await ctx.send(random.choice(self.xwx))

    @commands.command(help='Gives a random number within the given range')
    async def random(self,ctx,low:int,high:int):
        await ctx.send(random.randint(low,high))

    @commands.command(help='Says Stuff for the user:\n --say insult\n --say sadme',aliases=['s'])
    async def say(self,ctx,word,*args):
        if args and args[0]=='c':
            await ctx.message.delete()
        if word not in self.words:
            await ctx.send("```Not the right argument```")
            return
        else:
            for i in await ctx.channel.webhooks():
                if i.user.id == self.bot.user.id:
                    hook = i
                    break
            else:
                hook = await ctx.channel.create_webhook(name='bot_hook_'+str(ctx.channel))
            
            await hook.send(username=ctx.message.author.display_name,avatar_url=ctx.message.author.avatar_url,content=self.helper(word))
    
    def helper(self,word):
        """returns a random choice"""
        if word not in self.words:
            raise "Not a correct word"
        if not word in self.cache:
                with open(f'data/{word}.txt','r',encoding="utf-8") as f:
                    self.cache[word]=f.readlines()
        return random.choice(self.cache[word])

    @commands.command(help='Get\'s the meaning of the word using the Owl Dictionary api',aliases=['w'])
    async def word(self,ctx,word):
        #[{'message': 'No definition :('}]
        headers = {"Authorization":utils.auth["owl_auth"]}
        async with self.bot.session.get(f"https://owlbot.info/api/v4/dictionary/{word}",headers=headers) as f:
            resp = await f.json()
        #print(resp)
        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) in ['⬅️', '➡️'] and reaction.message.id == show.id
        page= 1
        size = len(resp["definitions"])
        show = await ctx.send(embed = await self.disp_embed(ctx,resp,page,size))
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
                await show.edit(embed = await self.disp_embed(ctx,resp,page,size)) 
            except asyncio.TimeoutError:
                await show.clear_reactions()
                break
        
    async def disp_embed(self,ctx,resp,page,size):
        #print(resp)
        show = resp["definitions"][page-1]
        embed = discord.Embed(title=resp["word"].capitalize(),color = discord.Color.green())
        embed.add_field(name='Definition:',value=utils.html_parse(show["definition"]),inline=False)
        if show["image_url"]:
            embed.set_thumbnail(url=show["image_url"])    
        if show["example"]:
            text = utils.html_parse(show["example"])
            embed.add_field(name='Example:',value=text,inline=True)
        if show["type"]:
            embed.add_field(name='Type:',value=show["type"],inline=True)
        embed.set_footer(text=f"page: {page}/{size}")
        return embed

def setup(bot):
    bot.add_cog(Chats(bot))