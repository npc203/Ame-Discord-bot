import discord
from discord.ext import commands
from discord.ext.commands import Cog
import random

class Miscellaneous(Cog):

    @commands.command(help='Meant for Pinging the given name on every available text channel \n only epic people can use it')
    async def punish(self,ctx,name,times):
        if str(ctx.message.author) in ("epic guy#0715","Juchetas#3421"):
                await ctx.message.delete()
                for channel in ctx.guild.text_channels:
                    try:
                        for _ in range(int(times)):
                            await channel.send(name)
                        await channel.purge(limit=int(times))
                    except:
                        print("Skipped: #",channel,sep='')
        else:
            print(type(ctx.message.author),ctx.message.author)
            await ctx.send("```***There was an attempt***```")
        print("It is done")
    
    @commands.command(help='Cleans the mess made by punish command \n only epic people can use it')
    async def clean(self,ctx,times):
        if str(ctx.message.author) in ("epic guy#0715","Juchetas#3421"): 
                await ctx.message.delete()        
                for channel in ctx.guild.text_channels:
                    try:
                        await channel.purge(limit=int(times))
                    except:
                        print("Skipped: #",channel,sep='')
        else:
            #print(type(ctx.message.author),ctx.message.author)
            await ctx.send("```***There was an attempt***```")
        print("It is done")

    @commands.command(help='Deletes messages upto the given limit in the present channel \n only epic people can use it')
    async def purge(self,ctx,limit):
        if str(ctx.message.author) in ("epic guy#0715","krsy123#3657"):
            await ctx.message.delete()
            await ctx.channel.purge(limit=int(limit))
        else:
            await ctx.send("***There was an attempt***")
    
    @commands.command(help='SPAMS \n only epic people can use it')
    async def spam(self,ctx,text,limit:int):
        if str(ctx.message.author) =="epic guy#0715":
            for i in range(limit):
                await ctx.send(text)
        else:
            await ctx.send("***There was an attempt***")
        

    @commands.command(aliases=['UwU', 'uwu', 'owo','OWO','UWU'],help="Made for the weebs")
    async def OwO(self,ctx):
        a="""OwO 
            Owo
            owO 
            ÓwÓ 
            ÕwÕ 
            @w@ 
            ØwØ
            øwø
            uwu
            ☆w☆ 
            ✧w✧ 
            ♥w♥ 
            ゜w゜ 
            ◕w◕ 
            ᅌwᅌ 
            ◔w◔ 
            ʘwʘ 
            ⓪w⓪ ︠
            ʘw ︠ʘ 
            (owo) 
            𝕠𝕨𝕠 
            𝕆𝕨𝕆 
            𝔬𝔴𝔬 
            𝖔𝖜𝖔 
            𝓞𝔀𝓞 
            𝒪𝓌𝒪 
            𝐨𝐰𝐨 
            𝐎𝐰𝐎 
            𝘰𝘸𝘰 
            𝙤𝙬𝙤 
            𝙊𝙬𝙊 
            𝚘𝚠𝚘 
            σωσ 
            OɯO 
            oʍo 
            oᗯo 
            ๏w๏ 
            o̲wo̲ 
            ᎧᏇᎧ 
            օաօ 
            (。O ω O。) 
            (。O⁄ ⁄ω⁄ ⁄ O。) 
            (O ᵕ O) 
            (O꒳O) 
            ღ(O꒳Oღ) 
            ♥(。ᅌ ω ᅌ。) 
            (ʘωʘ) 
            ( ʘ ྌ ʘ ) 
            (⁄ʘ⁄ ⁄ ω⁄ ⁄ ʘ⁄)♡ 
            ( ͡o ω ͡o ) 
            ( ͡o ᵕ ͡o ) 
            ( ͡o ꒳ ͡o ) 
            ( o͡ ꒳ o͡ ) 
            ( °꒳° ) 
            ( °ྌ° ) 
            ( °ྌྏ° ) 
            ( °ྌྏྏྏྏྏྏྏ° ) 
            ( °ᵕ° ) 
            ( °   ᳕ °) 
            ( °﹏° )    
            ( °ω° )  ̷
            (ⓞ̷ ̷꒳̷ ̷ⓞ̷) 
            (⍟  ᳕ ⍟) 
            (⦿  ᳕ ⦿) 
            (⦾   ᳕ ⦾) 
            ( ゜ω 。）
            ( 。ω ゜)
            OwO *𝘸𝘩𝘢𝘵’𝘴 𝘵𝘩𝘪𝘴*
            OwO *𝘯𝘰𝘵𝘪𝘤𝘦𝘴 𝘣𝘶𝘭𝘨𝘦*
            𝐎𝐰𝐎 *𝘸𝘩𝘢𝘵’𝘴 𝘵𝘩𝘪𝘴*
            ๏w๏ *𝘯𝘰𝘵𝘪𝘤𝘦𝘴 𝘣𝘶𝘭𝘨𝘦*
            ( ͡o ꒳ ͡o )*𝔫𝔬𝔱𝔦𝔠𝔢𝔰 𝔟𝔲𝔩𝔤𝔢*
            *𝓌𝒶𝓉𝓈 𝒹𝒾𝓈?*ღ(O꒳Oღ)
            *𝓃𝓊𝓏𝓏𝓁𝑒𝓈 𝓎𝑜𝓊*(。O⁄ ⁄ω⁄ ⁄ O。)
            (𝐎𝐰𝐎)<𝕣𝕒𝕨𝕣𝕣𝕣)~
            ‿︵*𝓇𝒶𝓌𝓇*‿︵ ʘwʘ
            ♥ ⑅  𝒘𝒉𝒆𝒓𝒆 (⦿   ᳕ ⦿) 𝒓 𝒖 ? ⑅ ♥
            ✼ ҉ (O꒳O) ҉ ✼
            ✼ ҉♡ (。O⁄ ⁄ω⁄ ⁄ O。) ҉♡ ✼
            ✧･ﾟ: *✧･ﾟ:*(OwO )*:･ﾟ✧*:･ﾟ✧""".split('\n')
        await ctx.send(random.choice(a))

def setup(bot):
    bot.add_cog(Miscellaneous(bot))