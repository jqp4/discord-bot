
import discord
from discord.ext import commands
from settings import Settings

import json
import requests
import datetime
from random import randint
from googletrans import Translator


settings = Settings()
translator = Translator()
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
        @✦ Control — Младшая модерация.
        @✦ Eventsmod — Организаторы мероприятий.
        @✦ Manager — Взаимодействие с аудиторией сервера.
        @✦ Support — Экскурсия новичков по серверу.
        @✦ Creative Control — Организация творческой деятельности.
        @✦ Redactor — В ответе за #mood и #webm.'''

    #admins = '@✦ Administrator — Главная администрация.\n@✦ Moderator — Старшая модерация.'
    #admins = '{} — Главная администрация.\n — Старшая модерация.'.format(discord.role.SUS)
    server_id = ctx.message.guild.id
    info = f'id сервера - {server_id}.'

    role_id = 856144602855112734
    admins = f'<@&{role_id}> — Главная администрация.'
    embed = discord.Embed(title="Информация о сервере:", color=settings.color)
    embed.add_field(name='*Идентификаторы:*', value=info, inline=False)
    embed.add_field(name='*Роли:*', value=admins, inline=False)
    await ctx.send(embed=embed)


@bot.command(aliases=["mc"])
async def member_count(ctx):
    a = ctx.message.guild.member_count
    c = settings.color
    b = discord.Embed(title=f"Members in {ctx.message.guild.name}", description=a, color=c)
    await ctx.send(embed=b)


@bot.command()
async def info(ctx):
    server_id = ctx.guild.id
    #member_count = len(ctx.message.guild.members) # includes bots
    #true_member_count = len([m for m in ctx.message.guild.members if not m.bot]) # doesn't include bots
    member_count = ctx.guild.member_count

    title = 'Информация о сервере:'
    descr = f'Server id:{server_id}\n'
    descr += f'Колличество участников: {member_count}\n \n'
    #descr += f'Колличество участников (без ботов): {true_member_count}'

    #for member in ctx.guild.members:
    #    descr += f'{member.name} '
    for member in ctx.guild.members():
            descr += f'{member}, {member.id}'

    c = settings.color
    embed = discord.Embed(title=title, description=descr, color=c)
    await ctx.send(embed=embed)









@bot.command()
async def test_args(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))


@bot.command(name='say')
async def test_908h98(ctx, *, arg):
    print(f'\n{arg}\n')
    await ctx.send(arg)


@bot.command(name='simple_embed')
async def d1239vub1vv31v(ctx, title:str, *, text:str=''):
    if title in ['help', '-help', '--h']:
        msg = f'```{settings.prefix}simple_embed <title in one word> <text>```'
        await ctx.send(msg)
    else:
        embed = discord.Embed(title=title, description=text, color=settings.color)
        await ctx.send(embed=embed)


@bot.command(name='embed_old')
async def fd12391d1wibe4g02v(ctx, *args):
    descr_key = f'{settings.cmd_key}description'
    field_key = f'{settings.cmd_key}field'
    text_key = f'{settings.cmd_key}text'
    LF_key = '\\n'
    #TAB_key = '\t'
    if args[0] in settings.help_keys:
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
            descr = ''''''
            i += 1
            while i < N and args[i] != field_key:
                s = args[i]
                if LF_key in s:   
                    x = s.find(LF_key)
                    st = s[x+len(LF_key):]
                    descr += f'''{s[:x]}\n{st} ''' if len(st) else f'''{s[:x]}\n'''
                else:
                    descr += f'''{s} '''
                i += 1
            embed = discord.Embed(title=title, description=descr, color=settings.color)
        
        while i < N:
            field_name = ''
            text = ''

            if args[i] == field_key:
                i += 1
                while i < N and args[i] != text_key:
                    field_name += f'{args[i]} '
                    i += 1
            if args[i] == text_key:
                i += 1
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

            embed.add_field(name=field_name, value=text, inline=False)

        #img_line_url = 'https://media.discordapp.net/attachments/774042908718399509/830485232695115776/1111.png'
        #embed.set_image(url=img_line_url)
        await ctx.send(embed=embed)





@bot.command(name='embed')
async def d1239109j30hfla02v(ctx, *, s_json):
    _json = json.loads(s_json) # <class 'dict'>
    '''_timestamp = None
    if 'timestamp' in _json:
        #_timestamp = _json['timestamp']
        #_timestamp = f'{_timestamp[0:10]} {_timestamp[11:19]}'
        #_timestamp = datetime.datetime.strptime(_timestamp, '%Y-%m-%d %H:%M:%S')
        #_timestamp = _json['timestamp'][:19]
        _timestamp = datetime.datetime.strptime(_json['timestamp'][:19], '%Y-%m-%dT%H:%M:%S')
    #except: pass'''

    get_ts = lambda ts: datetime.datetime.strptime(ts[:19], '%Y-%m-%dT%H:%M:%S')
    _timestamp = get_ts(_json['timestamp']) if 'timestamp' in _json else None
    
    for key in ['color', 'timestamp']:
        _json.pop(key, None)

    embed = discord.Embed.from_dict(_json)
    embed.color = settings.color
    if _timestamp:
        embed.timestamp = _timestamp

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


@bot.command(aliases=["tl", "tr", "translate"])
async def translate_jebrvwev(ctx, lang, *, text):
    #translator = Translator()
    translation = translator.translate(text, dest=lang)
    await ctx.send(translation.text)


@bot.command(name='fox')
async def fox_clkndc2bpioubv(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON
    
    c = settings.color
    embed = discord.Embed(title='Random Fox', color=c)
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed)



@bot.command()
async def sal(ctx):
    guild = ctx.guild
    with open(f'audit_logs_{guild.name}', 'w+') as f:
        async for entry in guild.audit_logs(limit=100):
            f.write('{0.user} did {0.action} to {0.target}'.format(entry))
    await ctx.send('done.')


@bot.command()
async def pal(ctx, lim:int=200):
    info = ['']
    j = 0
    async for entry in ctx.guild.audit_logs(limit=lim):
        #nr = '{0.user} did {0.action} to {0.target}'.format(entry)
        act = entry.action

        if act == discord.AuditLogAction.channel_delete:
            
            diff = entry.before

            target = entry.target
            
            user = f'<@!{entry.user.id}>'
            nr = f'{user} did {act}\t→\t`{target}` {diff}\n'
            
            if len(info[j]) + len(nr) < 1020:
                info[j] += nr
            else:
                info.append(nr)
                j += 1


    n = len(info)
    for i in range(n):
        embed = discord.Embed(title='Журнал аудита', color=settings.color)
        embed.add_field(name=f'стр. {i+1} из {n}', value=info[i], inline=False)
        await ctx.send(embed=embed)

    #async for entry in ctx.guild.audit_logs(limit=100):
    #    await ctx.send('{0.user} did {0.action} to {0.target}'.format(entry))
    await ctx.send('done.')




@bot.command(name='r')
async def wevonwqv(ctx):
    n = 'test2'
    p = discord.Permissions(268435511)
    c = 0xff6699




    role = await ctx.guild.create_role(name=n, permissions=p, color=c)  

    d = f'''
    **Role:** <@&{role.id}>
    **Id:** {role.id}
    **Created by:** {ctx.author.mention}
    '''
    embed = discord.Embed(name='New role created', description=d)
    await ctx.send(embed=embed)
