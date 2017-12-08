import discord
from discord.ext import commands
import list
from list import admin_ids
import traceback
import asyncio


class BotSubmit:
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def submit(self, ctx, link : str = None, *, description: str = None):
        await ctx.send('''By submitting your bot you understand and agree to the following :
1. No bot's breaking discord Tos
2. No spam bots or auto invite bots
3. To not use this bot in programming and only in bot-tests

If you agree to these terms, type "yes". If you type anything else your submission will be canceled.''')

        def check(m):
            return m.channel == ctx.channel and m.author == ctx.author
        try:
            msg = await self.bot.wait_for('message', check = check, timeout = 30)
        except asyncio.TimeoutError:
            return await ctx.send("<:redtick:359040808873099265> | You took too long to respond, your submission was canceled.")

        if msg.content.lower() == 'yes':
            await ctx.send('<:greentick:359040809036677130> | Your bot has been submitted.')
        else:
            await ctx.send('<:redtick:359040808873099265> | Your bot submission was canceled.')

    @submit.error
    async def submit_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send('That command is on cooldown, please try again in {} seconds.'.format(int(error.retry_after)))
        else:
            traceback.print_tb(error.__traceback__)

def setup(bot):
    bot.add_cog(BotSubmit(bot))
