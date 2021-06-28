
import discord
from discord.ext import commands
from config import Config
from bot_commands import bot


config = Config()


print('\n'*42)
print(config.invite_link())

bot.run(config.token)


