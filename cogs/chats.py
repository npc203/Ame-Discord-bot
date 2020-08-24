import discord
from discord.ext import commands
from discord.ext.commands import Cog
import random
import asyncio
class Chats(Cog):
    """Weeby commands"""
    def __init__(self, bot):
        self.owo="""OwO 
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
        self.uwu="""UwU
                    Uwu
                    uwU
                    ÚwÚ
                    uwu
                    ☆w☆
                    ✧w✧
                    ♥w♥
                    ︠uw ︠u
                    (uwu)
                    (ᵘʷᵘ)
                    (ᵘﻌᵘ) 
                    ˯˽˯ 
                    (◡ ω ◡) 
                    (◡ ꒳ ◡) 
                    (◡ w ◡) 
                    (◡ ሠ ◡) 
                    (˘ω˘) 
                    (⑅˘꒳˘) 
                    (˘ᵕ˘) 
                    (˘ሠ˘) 
                    (˘³˘) 
                    (˘ε˘) 
                    (´˘`) 
                    (´꒳`) 
                    (˘ ˘ ˘)⭜ 
                    ( ᴜ ω ᴜ ) 
                    ( ´ω` )۶ 
                    („ᵕᴗᵕ„) 
                    (*ฅ́˘ฅ̀*) 
                    (ㅅꈍ ˘ ꈍ) 
                    (⑅˘꒳˘) 
                    ( ｡ᵘ ᵕ ᵘ ｡) 
                    ( ᵘ ꒳ ᵘ ✼) 
                    ( ˘ᴗ˘ ) 
                    ˬ ͜   ˬ 
                    ᐡ꒳ᐡ 
                    (˯ ᵘ ꒳ ᵘ ˯) 
                    (ᵘᆸᵘ)⭜ 
                    (ᵕᴗ ᵕ⁎) 
                    *:･ﾟ✧(ꈍᴗꈍ)✧･ﾟ:* 
                    *˚*(ꈍ ω ꈍ).₊̣̇. 
                    (。U ω U。) 
                    (。U⁄ ⁄ω⁄ ⁄ U。) 
                    (U ᵕ U❁) 
                    (U ﹏ U) 
                    (◦ ᵕ ˘ ᵕ ◦) 
                    ღ(U꒳Uღ) 
                    ♥(。U ω U。) 
                    – ̗̀ (ᵕ꒳ᵕ) ̖́ – 
                    ಇ( ꈍᴗꈍ)ಇ 
                    ᕦ( ˘ᴗ˘ )ᕤ 
                    (⁄˘⁄ ⁄ ω⁄ ⁄ ˘⁄)♡ 
                    ( ͡U ω ͡U ) 
                    ( ͡o ᵕ ͡o ) 
                    ( ͡o ꒳ ͡o )  
                    ( ˊ.ᴗˋ ) 
                    (灬´ᴗ`灬) 
                    [̲̅$̲̅(̲̅ ᵕ꒳ᵕ)̲̅$̲̅]
                    ( ˶˘ ³˘(ᵕ꒳ᵕ)*₊˚♡
                    ⋆⛧*﹤ಇ( ᵕ꒳ᵕ)ಇ﹥*⛧⋆
                    ✧･ﾟ: *✧･ﾟ♡*(ᵘʷᵘ)*♡･ﾟ✧*:･ﾟ✧
                    ଘ(੭ ˘ ᵕ˘)━☆ﾟ.*･｡ﾟᵕ꒳ᵕ~""".split("\n")
        self.xwx="""(　◕‿◕✿)
                    (◕ᴗ◕✿)
                    (◕ ﺮ ◕✿) 
                    (◕ ˬ ◕✿) 
                    (◕ˇ ◕✿) 
                    (◕◡◕✿) 
                    (◔◡◔✿) 
                    (◡‿◡✿) 
                    (◠‿◠✿) 
                    (◕ ω ◕✿) 
                    (◕ܫ◕✿) 
                    (◕▿◕✿) 
                    (◕ ワ ◕✿) 
                    (◕▽◕✿) 
                    (◕ ɔ ◕✿)
                    (ʘ‿ʘ✿) 
                    (⓪__⓪ ✿) 
                    ♡  (ʘ ꒳ ʘ✿) 
                    (✧ᴗ✧✿) 
                    (✿◉‿◉)🗡 
                    (✿˶◉⚰︎◉˶)🗡 
                    (✿ ︣⓪ ‸ ︣⓪)っ🗡 
                    🗡⊂(ʘ‿ʘ✿) 
                    ミ=͟͟͞͞(✿ʘ ᴗʘ)っ🗡 
                    =͟͟͞͞(✿⓪ ڡ ⓪ )🔪 
                    (✿ʘ‿ʘ)✂╰⋃╯
                    Huuu━━(◕言 ◕✿)━━uuh?
                    (≖ ︿ ≖ ✿) 
                    (≖ ︿ ≖ ✿)ꐦꐦ 
                    (≖ ‸ ≖ ✿) 
                    (≖ ˆ ≖ ✿) 
                    (≖ Δ ≖ ✿) 
                    ꉂ `≖ o ≖´ ✿ ) 
                    (ಸ ︿ ಸ ✿)
                    +ﾟ*｡:ﾟ+凸(◕‿◕✿)+ﾟ*｡:ﾟ+
                    (╯✿◕益◕）╯︵ ┻━┻""".split("\n")

        
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

def setup(bot):
    bot.add_cog(Chats(bot))