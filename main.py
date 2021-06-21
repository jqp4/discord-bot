
import discord
from discord.ext import commands
from config import Settings
from bot_commands import bot


settings = Settings()

#print(settings.invite_link())

print('\n'*43)

bot.run(settings.token)


