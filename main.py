'''
https://discordapp.com/oauth2/authorize?&client_id=855554239991906335&scope=bot&permissions=67584

https://stackoverflow.com/questions/55012726/discord-py-unable-to-get-certificate

Install Certificates.command

'''

import discord
from discord.ext import commands


settings = {
    'token': 'ODU1NTU0MjM5OTkxOTA2MzM1.YM0K-g.54Oh2uTawJ85Iu5IGJQZhV6F8JE',
    'bot': 'важный хуй',
    'id': 855554239991906335,
    'prefix': '::'
}

def get_name(ctx):
    #author = ctx.message.author 
    #name = str(author)[:-5]
    return str(ctx.message.author)[:-5]


bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.

async def hello_(ctx): 
    author = ctx.message.author 
    name = str(author)[:-5]
    #print(author, name)
    prio = ['PopkaMorzha', 'анти-дрейн', 'Kellon']
    if name in prio:
        await ctx.send(f'{author.mention} скинь жопу')
    elif name == 'Glelg':
        await ctx.send(f'{author.mention} люблю тебя <3')
    else:
        await ctx.send(f'прив, {author.mention}')

@bot.command()
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Hello, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.


@bot.command()
async def test(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

@bot.command()
async def test2(ctx, *, arg):
    await ctx.send(arg)









bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена









