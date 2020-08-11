import discord
from discord.ext import commands
from discord.ext.commands import Cog
import random
import pickle
class Chats(Cog):

    @commands.command(help='facts module:\n1.add\n2.list\n3.remove\n4.no argument = random fact')
    async def facts(self,ctx,*args):
        try:
            #print('buggy')
            a=pickle.load(open('logs/facts','rb'))
        except:
            pickle.dump([],open('logs/facts','wb'))
        if not args:
             await ctx.send(random.choice(a))
        elif args[0]=='list':
                a=pickle.load(open('logs/facts','rb'))
                print(a)
                await ctx.send('```'+'Facts List:\n'+'\n'.join([str(i)+'. '+a for i,a in enumerate(a,1)])+'```')
        elif args[0]=='add':
            a.append(' '.join(args[1:]))
            pickle.dump(a, open('logs/facts','wb'))
            #a=pickle.load(open('logs/facts','rb'))
            await ctx.send("```fact added```")
        elif args[0]=='remove':
            try:
                a.pop(int(args[1])-1)
                pickle.dump(a, open('logs/facts','wb'))
                #a=pickle.load(open('logs/facts','rb'))
                await ctx.send("```fact removed```")
            except IndexError:
                await ctx.send('Enter index pls')
        else:
            await ctx.send('Error, you suck at typing kiddo')
            

def setup(bot):
    bot.add_cog(Chats(bot))