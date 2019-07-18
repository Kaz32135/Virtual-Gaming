import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio

bot = commands.Bot(command_prefix= '#')

@bot.event
async def on_ready():
print ("VG Bot a mers")
print ("Virtual-Gaming Bot#1")

bot.run('NjAxMjg5MzA5MDM0NjQzNDU3.XTAKQQ.jnw7t4ogGPOg4nUuVKFxyHFVLW8')