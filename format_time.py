# Code taken from JellyWX's reminder-bot for Discord.
# https://github.com/JellyWX/reminder-bot/blob/master/format_time.py
# Donate to him at https://www.patreon.com/jellywx and add his bot with
# https://discordapp.com/oauth2/authorize?client_id=349920059549941761&scope=bot&permissions=268446820

# I did a little update and its now shorter and slightly faster

def format_time2(text):
  d = {
    's' : 0,
    'm' : 0,
    'h' : 0,
    'd' : 0
  }
  t = {
    's' : 1,
    'm' : 60,
    'h' : 3600,
    'd' : 86400
  }
  current = '0'

  for char in text:
    if char in '0123456789':
      current += char

    elif char in d.keys():
      d[char] = int(current)
      current = '0'

    else:
      return None

  return sum([v * t[k] for k, v in d.items()]) + int(current)
