import discord
from discord.ext import commands
import list
from list import admin_ids

class Admin:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def testlog(self, ctx):
        channel = self.bot.get_channel(372116367266152450)
        if ctx.message.author.id in admin_ids:
            await ctx.send('<:greentick:359040809036677130> | Testing Complete!')
        else:
            await channel.send(':eyes: | {} Tried to use testing | ID: {}'.format(ctx.message.author, ctx.message.author.id))
            await ctx.send("<:redtick:359040808873099265> | Staff Only! | Action has been logged!")


    @commands.command()
    async def kick(self, ctx, target : discord.Member = None, *, reason : str = None):
        """kicks a pleb from the server"""
        channel = self.bot.get_channel(372116367266152450)
        if ctx.message.author.id in admin_ids:
            if target is None:
                return await ctx.send("<:redtick:359040808873099265> | Please specify a **member** to **__kick__**")
            if reason is None:
                return await ctx.send("<:redtick:359040808873099265> | You must have a **__reason__** specified")
            else:
                await target.kick(reason=reason)
                embed=discord.Embed(title="Log - Kick!")
                embed.add_field(name="User:", value=target, inline=False)
                embed.add_field(name="UserID:", value=target.id, inline=True)
                embed.add_field(name="Reason:", value=reason, inline=True)
                embed.add_field(name="ModeratorID:", value=ctx.message.author.id, inline=True)
                embed.add_field(name="Moderator:", value=ctx.message.author, inline=True)
                embed.set_footer(text="SneakyModBot  | Made by the SneakyCodeGroup")
                await channel.send(embed=embed)
                await ctx.send("<:greentick:359040809036677130> | Kicked `{}`! for `{}`".format(target, reason))
                embed=discord.Embed(title="Kick!")
                embed.add_field(name="User:", value=target, inline=False)
                embed.add_field(name="Reason:", value=reason, inline=True)
                embed.add_field(name="Moderator:", value=ctx.message.author, inline=True)
                embed.set_footer(text="SneakyModBot  | Made by the SneakyCodeGroup")
                await target.send(embed=embed)
        else:
            await channel.send(':eyes: | {} Tried to use kick | ID: {}'.format(ctx.message.author, ctx.message.author.id))
            await ctx.send("<:redtick:359040808873099265> | Staff Only! | Action has been logged!")

    @commands.command()
    async def warn(self, ctx, user : discord.Member = None, *, reason : str = None):
        channel = self.bot.get_channel(372116367266152450)
        if ctx.message.author.id in admin_ids:
            if user is None:
                return await ctx.send("<:redtick:359040808873099265> | Please specify a **member** to **__warn__**")
            if reason is None:
                return await ctx.send("<:redtick:359040808873099265> | You must have a **reason** specified")
            else:
                embed=discord.Embed(title="Log - Warning")
                embed.add_field(name="User:", value=user, inline=False)
                embed.add_field(name="UserID:", value=user.id, inline=False)
                embed.add_field(name="Reason:", value=reason, inline=False)
                embed.add_field(name="ModeratorID:", value=ctx.message.author.id, inline=False)
                embed.add_field(name="Moderator:", value=ctx.message.author, inline=False)
                embed.set_footer(text="SneakyModBot  | Made by the SneakyCodeGroup")
                await channel.send(embed=embed)
                await ctx.send("<:greentick:359040809036677130> | Warned `{}`!".format(user))
                embed=discord.Embed(title="Warning!")   
                embed.add_field(name="User:", value=user, inline=False)
                embed.add_field(name="UserID:", value=user.id, inline=False)
                embed.add_field(name="Reason:", value=reason, inline=False)
                embed.add_field(name="ModeratorID:", value=ctx.message.author.id, inline=False)
                embed.add_field(name="Moderator:", value=ctx.message.author, inline=False)
                embed.set_footer(text="SneakyModBot  | Made by the SneakyCodeGroup")
                await user.send(user, embed=embed)
        else:
            await channel.send(':eyes: | {} Tried to use warn | ID: {}'.format(ctx.message.author, ctx.message.author.id))
            await ctx.send("<:redtick:359040808873099265> | Staff Only! | Action has been logged!")

    @commands.command()
    async def msg(self, ctx, user : discord.Member = None, *, message : str = None):
        channel = self.bot.get_channel(372116367266152450)
        if ctx.message.author.id in admin_ids:
            if user is None:
                return await ctx.send("<:redtick:359040808873099265> | Please specify a **member** to **__message__**")
            if message is None:
                return await ctx.send("<:redtick:359040808873099265> | You must have a **message**")
            else:
                embed=discord.Embed(title="Moderator Message", description="Do not reply we will not recieve the message")
                embed.set_author(name="Sneaky Help Server Message")
                embed.add_field(name="Message:", value=message, inline=False)
                await user.send(embed=embed)
        else:
            await channel.send(':eyes: | {} Tried to use msg | ID: {}'.format(ctx.message.author, ctx.message.author.id))
            await ctx.send("<:redtick:359040808873099265> | Staff Only! | Action has been logged!")

        
    @commands.command()
    async def help(self, ctx):
        channel = self.bot.get_channel(372116367266152450)
        if ctx.message.author.id in admin_ids:
            embed=discord.Embed(title="Here are the commands only you can use!")
            embed.set_author(name="Help")
            embed.add_field(name="!kick", value="(user) (reason) - Kicks a user must have a reason", inline=False)
            embed.add_field(name="!warn", value="(user) (reason) - Warns a user must have a reason", inline=False)
            embed.add_field(name="!msg", value="(user) (message) - Sends a moderator message", inline=False)
            embed.add_field(name="!log", value="(message) - Add a message in the log example: I updated someones role..", inline=False)
            await ctx.message.author.send(embed=embed)
            await ctx.send("<:greentick:359040809036677130> | Sent you the help message")
        else:
            await channel.send(':eyes: | {} Tried to use help | ID: {}'.format(ctx.message.author, ctx.message.author.id))
            await ctx.send("<:redtick:359040808873099265> | Staff Only! | Action has been logged!")
        
    
    @commands.command()
    async def log(self, ctx, *, log : str = None):
        channel = self.bot.get_channel(372116367266152450)
        if ctx.message.author.id in admin_ids:
            if log is None:
                return await ctx.send("<:redtick:359040808873099265> | You must have a **message to add to the log**")
            else:
                embed=discord.Embed(title="{} logged something..".format(ctx.message.author.name), description="{}".format(log))
                await channel.send(embed=embed)
                await ctx.send("<:greentick:359040809036677130> | Updated the log!")
        else:
            await channel.send(':eyes: | {} Tried to use log | ID: {}'.format(ctx.message.author, ctx.message.author.id))
            await ctx.send("<:redtick:359040808873099265> | Staff Only! | Action has been logged!")
            
def setup(bot):
    bot.add_cog(Admin(bot))
    print('Admin commands is loaded')
