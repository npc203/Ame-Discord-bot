import discord
from discord.ext import commands
from discord.ext.commands import Cog
import random
import asyncio
class Chats(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.perms=("Admin","Owner","Co-Owner")
    
    @commands.cooldown(1, 7, commands.BucketType.user)
    @commands.command(help='facts module:\n1.add\n2.list\n4.no argument = random fact')
    async def facts(self,ctx,*args):   
        self.db = self.bot.get_channel(743058819545956384)
        try:
            a=(await self.db.history(limit=200).flatten())
            size = len(a)//10+1
        except IndexError:
            pass    
        if not args:
            await ctx.send('```'+random.choice([i.content for i in a])+'```')
        elif len([x for x in [str(i.name) for i in ctx.message.author.roles] if x in self.perms])>0:
            await ctx.message.delete() 
            def check(reaction, user):
                return str(reaction.emoji) in ['⬅️', '➡️']
                #return user == ctx.message.author and str(reaction.emoji) in ['⬅️', '➡️']  
            if args[0]=='list':       
                if str(ctx.message.author) in ("epic guy#0715","Remichaan#6626"):
                    page= 1
                    actual=[str(i)+'. '+a for i,a in enumerate([i.content for i in a],1)]
                    show = await ctx.send('```'+'Facts List:\n\n'+'\n'.join(actual[:10])+f'\n\n\npage {page}/{size}'+'```')
                    await show.add_reaction( '⬅️')
                    await show.add_reaction('➡️')                  
                    while True:
                        try:
                            reaction, user = await self.bot.wait_for('reaction_add', timeout=60,check = check)
                            #print(reaction.emoji)
                            if  page>size:
                                page-=1
                            elif page<1:
                                page+=1
                            else:
                                if reaction.emoji == '⬅️':
                                    page -= 1
                                elif reaction.emoji == '➡️':
                                    page += 1
                                await show.edit(content='```'+'Facts List:\n\n'+'\n'.join(actual[(page-1)*10:page*10])+f'\n\npage {page}/{size}'+'```')
                            
                        except asyncio.TimeoutError:
                            await show.edit(content='Timeout, facts closed uwu')
                            break
                else:
                    await ctx.send('```'+"Why are you gay?"+'```')
            elif args[0]=='add':
                msg=' '.join(args[1:])
                await self.db.send(msg)
                await ctx.send("```yaml\nfact added: "+msg+"\nby: "+str(ctx.message.author)+"```")
            elif args[0]=='fill':
                with open('backup.txt','r') as f:
                    for i in f.readlines():
                        await self.db.send(' '.join(i.split()[1:]))
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