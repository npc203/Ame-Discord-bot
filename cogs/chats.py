import discord
from discord.ext import commands
from discord.ext.commands import Cog
import random
import pickle
class Chats(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.perms=("Admin","Owner","Co-Owner")
    
    @commands.cooldown(1, 7, commands.BucketType.user)
    @commands.command(help='facts module:\n1.add\n2.list\n3.remove\n4.no argument = random fact')
    async def facts(self,ctx,*args):   
        self.db = self.bot.get_channel(743058819545956384)
        try:
            a=(await self.db.history(limit=200).flatten())[0]
        except IndexError:
            await self.db.send("facts:")       
        if not args:
            await ctx.send('```'+random.choice([i for i in a.content.split('\n')][1:])+'```')
        elif len([x for x in [str(i.name) for i in ctx.message.author.roles] if x in self.perms])>0:
            await ctx.message.delete()   
            if args[0]=='list':       
                if str(ctx.message.author) in ("epic guy#0715","Remichaan#6626"):
                    await ctx.send('```'+'Facts List:\n'+'\n'.join([str(i)+'. '+a for i,a in enumerate([i for i in a.content.split('\n')][1:],1)])+'```')
                else:
                    await ctx.send('```'+"Why are you gay?"+'```')
            elif args[0]=='add':
                msg=' '.join(args[1:])
                await a.edit(content=a.content+'\n'+msg)
                await ctx.send("```yaml\nfact added: "+msg+"\nby: "+str(ctx.message.author)+"```")
            elif args[0]=='remove':
                try:
                    if int(args[1])==0:
                        await ctx.send("```Enter valid index pls```")
                    else:
                        msgs=[i for i in a.content.split('\n')]
                        await ctx.send("```yaml\nfact removed: "+msgs.pop(int(args[1]))+"\nby: "+str(ctx.message.author)+"```")
                        await a.edit(content='\n'.join(msgs))
                except IndexError:
                    await ctx.send('Enter valid index pls')
            elif args[0]=='clean':
                try:
                    msgs=[i for i in a.content.split('\n')]
                    del msgs[int(args[1]):int(args[2])+1]
                    await a.edit(content='\n'.join(msgs))
                    await ctx.send("```yaml\nfacts cleaned by: "+str(ctx.message.author)+"```")
                except IndexError:
                    await ctx.send('Enter valid index range pls')
            else:
                await ctx.send('Error, you suck at typing kiddo, '+str(ctx.message.author))
        else:
            await ctx.send('```yaml\nSIKE, Not enough permissions NOOB\nfact failed to add/manipulate: '+' '.join(args[1:])+"\nby: "+str(ctx.message.author)+'```')
        
    @commands.command(aliases=['UwU', 'uwu', 'owo','OWO','UWU'],help="Made for the weebs")
    async def OwO(self,ctx,*args):
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
        if args:
            if args[0]=='c':
                await ctx.message.delete()
        await ctx.send(random.choice(a))     

    @facts.error
    async def cool_dude(self,ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg = 'UwU Don\'t abuse me senpai,try again in {:.2f}s'.format(error.retry_after)
            await ctx.send(msg)
        else:
            raise error       

def setup(bot):
    bot.add_cog(Chats(bot))