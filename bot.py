###############Imports################
import discord
from discord.ext import commands


with open("token.txt", 'r') as f:
    token = f.read().strip('\n')

    
###############Defining the variables################
initial_extensions = ('cogs.Admin')


                      
bot = commands.Bot(command_prefix=';', description='A bot for sneaky's help server!')

##########On ready#######################

@bot.event
async def on_ready():
    print('\n\nLogged in as: {} - {}\nVersion: {}\n'.format(bot.user.name, bot.user.id, discord.__version__))
    await bot.change_presence(game=discord.Game(name=' ;help | Moderating the server!'.))
    
    
    
#########Cog loader###########################


if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}.'.format(extension), file=sys.stderr)
            traceback.print_exc()
        print('Successfully logged in and booted...!')
    
###########Token##############################

bot.run(token, bot=True, reconnect=True)
