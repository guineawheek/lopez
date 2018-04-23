import discord
import boiler
from discord.ext import commands

class moderate():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def purge(self, ctx, amount: int):
        if (ctx.message.channel.permissions_for(ctx.message.author).manage_messages):
            i = 0
            j = -1
            while (i < amount + 1):
                print("(i, j): ({}, {})".format(i, j))
                if (list(self.bot.messages)[j].channel.id == ctx.message.channel.id):
                    await self.bot.delete_message(self.bot.messages[j])
                    self.bot.messages.remove(self.bot.messages[j])
                    j = -1
                    i += 1
                else:
                    j -= 1
            em = boiler.embed_template()
            em.title = "Purged {} messages".format(amount)
            em.set_footer(text="Requested by {}".format(ctx.message.author.nick))
            await self.bot.say(None, embed=em)
        else:
            await self.bot.say("Purge not performed because you ain't got the power.")

def setup(bot):
    bot.add_cog(moderate(bot))