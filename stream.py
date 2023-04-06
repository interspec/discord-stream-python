import discord
from discord.ext import commands

token = "YOUR TOKEN HERE"

bot = commands.Bot(command_prefix = "idshfdlsjdhafkjsdfh")

@bot.event
async def on_connect():
    stream = discord.Streaming(
        name = 'TEXT HERE',
        url = 'TWITCH / YT VIDEO LINK HERE',

        )
    await bot.change_presence(activity=stream)
    print('streaming...')





  
bot.run(token, bot=False)    
