import discord
from discord import Webhook, RequestsWebhookAdapter
from discord.ext import commands
from discord.ext.commands import Cog
import random,requests
import asyncio,io
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

    @commands.command(help='Says Stuff for the user:\n --say insult\n --say sadme',aliases=['s'])
    async def say(self,ctx,word,*args):
        if args and args[0]=='c':
            await ctx.message.delete()
        if word not in self.words:
            await ctx.send("```Not the right argument```")
            return
        else:
            hooks = await ctx.channel.webhooks()
            if hooks:
                hook = hooks[0]
            else:
                hook = await ctx.channel.create_webhook(name='bot_hook_'+str(ctx.channel))
            
            await hook.send(username=ctx.message.author.display_name,avatar_url=ctx.message.author.avatar_url,content=self.helper(word))
    @commands.command(help='Tells whatever is given as the sentence, mimicing user\'s identity and name',aliases=['t'])
    async def tell(self,ctx,*sentence):
        await ctx.message.delete()
        hooks = await ctx.channel.webhooks()
        if hooks:
            hook = hooks[0]
        else:
            hook = await ctx.channel.create_webhook(name='bot_hook_'+str(ctx.channel)) 
        await hook.send(username=ctx.message.author.display_name,avatar_url=ctx.message.author.avatar_url,content=' '.join(sentence))
    
    def helper(self,word):
        """returns a random choice"""
        if word not in self.words:
            raise "Not a correct word"
        if not word in self.cache:
                with open(f'data/{word}.txt','r',encoding="utf-8") as f:
                    self.cache[word]=f.readlines()
        return random.choice(self.cache[word])

def setup(bot):
    bot.add_cog(Chats(bot))