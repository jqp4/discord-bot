
import discord
from discord.ext import commands
from config import Settings
from random import randint

settings = Settings()

bot = commands.Bot(command_prefix = settings.prefix)







@bot.command()
async def hello(ctx): 
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


@bot.command(name='createrole')
async def createrole(ctx, *, content):
    guild = ctx.guild
    role = await guild.create_role(name=content)  
    roleid = role.id
    description = f'''
    **Id:** <@{roleid}>
    **Created by:** {ctx.author.mention}
    '''
    embed = discord.Embed(name='New role created', description=description)
    await ctx.send(content=None, embed=embed)


@bot.command()
async def show_roles_id(ctx):
    info = ['']
    j = 0
    for role in ctx.guild.roles[::-1]:
        nr = f'<@&{role.id}> — id:{role.id}\n'
        # dl = 12 - len(role.name)
        # dl = '· '*(dl if dl > 0 else 1)
        # nr = f'<@&{role.id}> {dl}id:{role.id}\n'
        if len(info[j]) + len(nr) < 1024:
            info[j] += nr
        else:
            info.append(nr)
            j += 1

    n = len(info)
    for i in range(n):
        embed = discord.Embed(title='Идентификаторы ролей', color=settings.color)
        embed.add_field(name=f'стр. {i+1} из {n}:', value=info[i], inline=False)
        await ctx.send(embed=embed)


@bot.command()
async def d(ctx):
    ''' Информация о ролях:
        Админские:

        @✦ Administrator — Главная администрация.
        @✦ Moderator — Старшая модерация.

        Служебные:

        @✦ Developer — Обслуживание и настройка серверных ботов.
        @✦ Curator — Лучшие представители своей ветки.
        @✦ Control и @✦ — Младшая модерация.
        @✦ Eventsmod — Организаторы мероприятий.
        @✦ Manager — Взаимодействие с аудиторией сервера.
        @✦ Support — Экскурсия новичков по серверу.
        @✦ Creative Control — Организация творческой деятельности.
        @✦ Redactor — В ответе за #┌🌚・mood и #├🎬・webm.'''

    #admins = '@✦ Administrator — Главная администрация.\n@✦ Moderator — Старшая модерация.'
    #admins = '{} — Главная администрация.\n — Старшая модерация.'.format(discord.role.SUS)
    server_id = ctx.message.guild.id
    info = f'id сервера - {server_id}.'



    role_id = 856144602855112734
    admins = f'<@&{role_id}> — Главная администрация.'

    embed = discord.Embed(title="Информация о сервере:", color=0xff6699)

    embed.add_field(name='*Идентификаторы:*', value=info, inline=False)

    embed.add_field(name='*Роли:*', value=admins, inline=False)

    await ctx.send(embed=embed)
















@bot.command()
async def test_args(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))


@bot.command(name='say')
async def test_908h98(ctx, *, arg):
    await ctx.send(arg)


@bot.command(name='simple_embed')
async def d1239vub1vv31v(ctx, title:str, *, text:str=''):
    if title in ['help', '-help', '--h']:
        msg = f'```{settings.prefix}simple_embed <title in one word> <text>```'
        await ctx.send(msg)
    else:
        embed = discord.Embed(title=title, description=text, color=settings.color)
        await ctx.send(embed=embed)


@bot.command(name='embed')
async def d12391dwibe4g02v(ctx, *args):
    descr_key = f'{settings.cmd_key}description'
    field_key = f'{settings.cmd_key}field'
    text_key = f'{settings.cmd_key}text'
    LF_key = '\\n'
    if args[0] in ['help', '-help', '--help', '--h']:
        msg = f'```{settings.prefix}embed <title>\n{descr_key} <description, optional>\n\tBlocks of text, optional:\n{field_key} <field name>\n{text_key} <text>\n\t*Use {LF_key} to line feed.```'
        await ctx.send(msg)
    else:
        N = len(args)
        title = ''
        i = 0
        while i < N and args[i] != descr_key and args[i] != field_key:
            title += f'{args[i]} '
            i += 1
        embed = discord.Embed(title=title, color=settings.color)

        if i < N and args[i] == descr_key:
            descr = ''
            i += 1
            while i < N and args[i] != field_key:
                descr += f'{args[i]} '
                i += 1
            embed = discord.Embed(title=title, description=descr, color=settings.color)
        
        i += 1
        while i < N:
            field_name = ''
            while i < N and args[i] != text_key:
                field_name += f'{args[i]} '
                i += 1
            i += 1
            text = ''
            while i < N and args[i] != field_key:
                s = args[i]
                if LF_key in s:   
                    x = s.find(LF_key)
                    st = s[x+len(LF_key):]

                    #s = f'{s[:x]}\n'
                    #if len(st):
                    #    s = f'{s}{st} '

                    text += f'{s[:x]}\n{st} ' if len(st) else f'{s[:x]}\n'
                else:
                    text += f'{s} '
                i += 1
            i += 1
            embed.add_field(name=field_name, value=text, inline=False)

        await ctx.send(embed=embed)


@bot.command(name='roll')
async def randint_98cl22fn(ctx, a:int, b:int=None):
    if not b:
        b = a
        a = 1
    r = randint(a, b)
    await ctx.send(f'randint({a}, {b}) = {r}')


@bot.command(name='feed_line_test')
async def wewjbvqlibwev(ctx):
    embed = discord.Embed(title='Test', color=settings.color)

    embed.add_field(name='Server Command', value='`p!ping`>>Check the ping from server to bot.\n`p!list`>>Check the number of users in the server.',  inline=False)
    embed.add_field(name=chr(173), value = chr(173))
    embed.add_field(name='Users Command', value='`!kick`>>Kick the user from server.',  inline=False)

    await ctx.send(embed=embed)


