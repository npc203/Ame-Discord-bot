import discord
from discord.ext import commands
from discord.ext.commands import Cog
import aiohttp,asyncio
from io import BytesIO

class Image(Cog):
    """Funny stuff with images"""
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()
    
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
    
    @commands.cooldown(1, 20, commands.BucketType.user)
    @commands.command(help="Either trigger yourself or make someone get triggered by mentioning them")
    async def trigger(self,ctx,*mentions):
        query="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(ctx.message.mentions[0] if mentions else ctx.author)
        url = "https://some-random-api.ml/canvas/triggered?avatar="+query
        async with self.session.get(url) as resp:
            if resp.status == 200:
                my_bytes = await resp.read()
                buffer = BytesIO(my_bytes)
                await ctx.send(file=discord.File(fp=buffer, filename='image.png'))
            else:
                await ctx.send(f"Somthing went wrong, Error: `{resp.status}`")
    
    @commands.cooldown(1, 20, commands.BucketType.user)
    @commands.command(help="Same as trigger, mention someone else get wasted.")
    async def wasted(self,ctx,*mentions):
        query="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(ctx.message.mentions[0] if mentions else ctx.author)
        url = "https://some-random-api.ml/canvas/wasted?avatar="+query
        async with self.session.get(url) as resp:
            if resp.status == 200:
                my_bytes = await resp.read()
                buffer = BytesIO(my_bytes)
                await ctx.send(file=discord.File(fp=buffer, filename='image.png'))
            else:
                await ctx.send(f"Somthing went wrong, Error: `{resp.status}`")
    
    @commands.cooldown(1, 20, commands.BucketType.user)
    @commands.command(help="Write your own pointless youtube comment")
    async def ytb(self,ctx,*comment):
        await ctx.message.delete()
        query="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(ctx.author)
        url = f"https://some-random-api.ml/canvas/youtube-comment?avatar={query}&username={ctx.author.display_name}&comment={'%20'.join(comment)}"
        async with self.session.get(url) as resp:
            if resp.status == 200:
                my_bytes = await resp.read()
                buffer = BytesIO(my_bytes)
                await ctx.send(file=discord.File(fp=buffer, filename='image.png'))
            else:
                await ctx.send(f"Somthing went wrong, Error: `{resp.status}`")

    @commands.cooldown(1, 7, commands.BucketType.user) 
    @commands.command(help="Typical random dose of internet fun \n use \"--meme v\" for meme with more details about the meme")
    async def meme(self,ctx,*args):
        async with self.session.get("https://meme-api.herokuapp.com/gimme") as resp:
            if resp.status == 200:
                raw = await resp.json()
            else:
                ctx.send(content="Something went wrong")
                return
        if args:
            embed = discord.Embed(title=raw["title"], colour=discord.Colour(0x3AF528), url=raw["postLink"],
            description="Subreddit: {}\nauthor: {} ".format(raw["subreddit"],raw["author"]))
        else:
            embed = discord.Embed(title=raw["title"], colour=discord.Colour(0x3AF528), url=raw["postLink"])
        if not raw["nsfw"] or ctx.channel.is_nsfw():
            embed.set_image(url=raw["url"])
        else:
            embed.add_field(name="Sorry the meme was NSFW", value="Forgive me Senpai, You can click the title to view the post tho")
        embed.set_footer(text="Upvotes: "+str(raw["ups"]))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Image(bot))