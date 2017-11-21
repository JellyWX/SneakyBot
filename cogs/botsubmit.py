import discord
from discord.ext import commands
import list
from list import admin_ids


class BotSubmit:
    def __init__(self, bot):
        self.bot = bot



        @commands.command()
        @commands.cooldown(1, 30, commands.BucketType.user)
        async def submit(self, ctx, link : str = None, *, Type: str = None):
            ctx.send("By submitting your bot you understand and agree to the following :")
            ctx.send("""1. No bot's breaking discord Tos \n2. No spam bots or auto invite bots \n3. To not use this bot in programming and only in bot-tests""")
            
