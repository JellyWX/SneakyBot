import discord
from discord.ext import commands
import list
from list import admin_ids
from format_time import format_time
import asyncio

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
                # I'm pretty sure this won't work if you try to message them after kicking them, so I moved kick down.
                # await target.kick(reason=reason)
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
                await target.kick(reason=reason)
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
            embed.add_field(name="!mute", value="(user) (time) (reason) - Gives a user the 'Muted' role for the specified amount of time, or indefinitely if time is 'none'. Ex. !mute Altarrel#1219 30s5m12h7d He's just too awesome!")
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

    @commands.command()
    async def mute(self, ctx, target: discord.Member = None, time: str = None, *, reason: str = None):
        channel = self.bot.get_channel(372116367266152450)
        if ctx.message.author.id in admin_ids:
            if target == None:
                await ctx.send("<:redtick:359040808873099265> | You must have a **member** to mute")
            elif time == None:
                await ctx.send("<:redtick:359040808873099265> | You must have a **time** to mute for. Use 'none' to mute indefinitely.")
            elif reason == None:
                await ctx.send("<:redtick:359040808873099265> | You must have a **reason** specified")
            elif "Muted" in [role.name for role in target.roles]:
                await ctx.send("<:redtick:359040808873099265> | {} is already muted. Remove the role manually or use **!unmute**".format(target))
            else:
                if time != "none" and format_time(time) == None:
                    await ctx.send("<:redtick:359040808873099265> | {} is not a valid time. Please use a time such as **10s5m12h3d** for 10 seconds, 5 minutes, 12 hours, and 3 days. Or use **none** to indefinitely mute.".format(time))
                else:
                    mutedRole = discord.utils.get(ctx.guild.roles, name = "Muted")
                    try:
                        await target.add_roles(mutedRole, reason = reason)
                        await ctx.send("<:greentick:359040809036677130> | Muted {} for time: {}\nreason: {}".format(target, format_time(time), reason))
                    except discord.Forbidden:
                        return await ctx.send("<:redtick:359040808873099265> | I don't have permission to give the Muted role to that member")


                        embed=discord.Embed(title="Log - Mute!")
                        embed.add_field(name="User:", value=target, inline=False)
                        embed.add_field(name="UserID:", value=target.id, inline=True)
                        embed.add_field(name="Reason:", value=reason, inline=True)
                        embed.add_field(name="ModeratorID:", value=ctx.message.author.id, inline=True)
                        embed.add_field(name="Moderator:", value=ctx.message.author, inline=True)
                        embed.set_footer(text="SneakyModBot  | Made by the SneakyCodeGroup")
                        await channel.send(embed=embed)
                    try:
                        embed=discord.Embed(title="Mute!")
                        embed.add_field(name="User:", value=target, inline=False)
                        embed.add_field(name="Reason:", value=reason, inline=True)
                        embed.add_field(name="Moderator:", value=ctx.message.author, inline=True)
                        embed.set_footer(text="SneakyModBot  | Made by the SneakyCodeGroup")
                        await target.send(embed=embed)
                    except discord.Forbidden:
                        await ctx.send("<:redtick:359040808873099265> | I can't send messages to that member, but they have still been muted.")

                        # self.bot.cursor.execute("""INSERT INTO muted(id)
                        # VALUES(?)""", (target.id))
                        # self.bot.db.commit()

                    if time == "none":
                        return
                    else:
                        await asyncio.sleep(format_time(time))
                        await target.remove_roles(mutedRole)
                        # self.bot.cursor.execute("DELETE FROM muted WHERE id = ? ", (target.id))
                        # self.bot.db.commit()

                        embed=discord.Embed(title="Log - Auto-Unmute!")
                        embed.add_field(name="User:", value=target, inline=False)
                        embed.add_field(name="UserID:", value=target.id, inline=True)
                        embed.add_field(name="Reason:", value=reason, inline=True)
                        embed.add_field(name="ModeratorID:", value=ctx.message.author.id, inline=True)
                        embed.add_field(name="Moderator:", value=ctx.message.author, inline=True)
                        embed.add_field(name="Time Set", value="{} or {} seconds".format(time, format_time(time)))
                        embed.set_footer(text="SneakyModBot  | Made by the SneakyCodeGroup")
                        await channel.send(embed=embed)

                        embed=discord.Embed(title="Auto-Unmute!")
                        embed.add_field(name="User:", value=target, inline=False)
                        embed.add_field(name="Reason:", value=reason, inline=True)
                        embed.add_field(name="Moderator:", value=ctx.message.author, inline=True)
                        embed.add_field(name="Time Set", value="{} or {} seconds".format(time, format_time(time)))
                        embed.set_footer(text="SneakyModBot  | Made by the SneakyCodeGroup")
                        await target.send(embed=embed)
        else:
            await channel.send(':eyes: | {} Tried to use mute | ID: {}'.format(ctx.message.author, ctx.message.author.id))
            await ctx.send("<:redtick:359040808873099265> | Staff Only! | Action has been logged!")

def setup(bot):
    bot.add_cog(Admin(bot))
    print('Admin commands is loaded')
