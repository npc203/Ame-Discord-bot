import discord
from discord.ext import commands
from utils import database as db
import utils
import random

class Game(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        with open("data/search.txt",'r') as f:
            self.words = f.read().splitlines() 
        #print(self.words)
        self.items = {}

    
    @commands.cooldown(1, 20, commands.BucketType.user) 
    @commands.command(help='Get\'s your profile',aliases=["pfp"])
    async def profile(self,ctx,*mention):
        async with ctx.typing():
            if mention:
                mention = ' '.join(mention) 
                try:
                    user = ctx.message.mentions[0]
                    #print(user)
                except IndexError:
                    user = ctx.guild.get_member_named(mention)
                    #print("##",user)
                if (not user) and mention.isdigit():
                    user = ctx.guild.get_member(int(mention))
                elif not user:
                    await ctx.send('Could not find user.')
                    return
                data = db.show(user.id)
            else:
                data = db.show(ctx.author.id)
                user = self.bot.get_user(ctx.author.id)
        embed = discord.Embed(colour=discord.Colour.blurple())
        embed.add_field(name="❯ Name",value=f"{user.name}#{user.discriminator}",inline=True)
        embed.add_field(name="❯ ID",value=f"{user.id}",inline=True)
        embed.add_field(name="❯ Discord Join Date",value=f"{user.created_at.strftime('%b %d, %Y')}",inline=True)
        embed.add_field(name="❯ Command Count",value=f"{data['cmd_count']}",inline=True)
        embed.add_field(name="❯ XP",value=f"{data['xp']}",inline=True)
        embed.add_field(name="❯ Level",value=f"{data['cmd_count']//20}",inline=True)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed = embed)
    
    @commands.command(help='Type the common words/objects you see in your daily life and gain xp.\n ngl this is kinda pointless',aliases=["sh"])
    async def search(self,ctx,word):
        if word.lower() in self.words:
            data = utils.Users.find_one({"id":ctx.author.id},{"items":1,'_id':0})
            xp = random.randint(10,29)
            if not data or word not in data["items"]:
                db.update_one({"id":ctx.author.id},{'$push':{'items' : word.lower()}})
                await ctx.send(f"Congrats you found `{word}` and gained `{xp}xp`")
            else:
                await ctx.send(f"You already found this Senpai -_-")
        else:
            await ctx.send("Senpai, It doesn't exist :/")
    




def setup(bot):
    bot.add_cog(Game(bot))