#Imports
import discord
from discord.ext import commands
import traceback


with open("token.txt", 'r') as f:
    token = f.read().strip('\n')


#Cogs/extensions to load when the script is run (is that proper grammar?)
initial_extensions = ('cogs.Admin', 'cogs.botsubmit')



bot = commands.Bot(command_prefix='!', description='A bot for sneakys help server!')
bot.remove_command("help")

#The first step to a great bot! On ready events!
#Nah

@bot.event
async def on_ready():
    print('\n\nLogged in as: {} - {}\nDiscord Version: {}\n'.format(bot.user.name, bot.user.id, discord.__version__))
    await bot.change_presence(game=discord.Game(name='Moderating the server!'))



#Cog Loader


if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}.'.format(extension))
            traceback.print_exc()
        print('Successfully logged in and booted...!')

#The super super super token that is locked away by ninjas and flying penguins? Quack quack Altarrel is a duck.

bot.run(token)
