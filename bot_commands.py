
import discord
from discord.ext import commands
from settings import Settings

import json
import requests
import datetime
import numpy as np
from random import randint
from colour import hex2hsl, hsl2rgb
from googletrans import Translator
import matplotlib.pyplot as plt



settings = Settings()
translator = Translator()
bot = commands.Bot(command_prefix = settings.prefix)













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
async def roles_old(ctx, *keys):
    fid = '-id' in keys
    fperm = '-perm' in keys
    fcl = '-cl' in keys

    info = ['']
    j = 0
    for role in ctx.guild.roles[::-1]:
        #nr = f'<@&{role.id}> — id:{role.id}\n'
        nr = f'<@&{role.id}> '
        nr += f'id:{role.id} ' if fid else ''
        nr += f'perm:{role.permissions.value} ' if fperm else ''
        nr += f'cl:{role.colour} ' if fcl else ''
        nr += '\n'

        if len(info[j]) + len(nr) < 1024:
            info[j] += nr
        else:
            info.append(nr)
            j += 1

    n = len(info)
    for i in range(n):
        embed = discord.Embed(title='List of roles', color=settings.color)
        embed.add_field(name=f'стр. {i+1} из {n}:', value=info[i], inline=False)
        await ctx.send(embed=embed)


@bot.command()
async def roles(ctx, *keys):
    fid = '-id' in keys
    fperm = '-perm' in keys
    fcl = '-cl' in keys

    info = ['']
    j = 0
    for role in ctx.guild.roles[::-1]:
        #nr = f'<@&{role.id}> — id:{role.id}\n'
        nr = f'<@&{role.id}> '
        nr += f'id:{role.id} ' if fid else ''
        nr += f'perm:{role.permissions.value} ' if fperm else ''
        nr += f'cl:{role.colour} ' if fcl else ''
        nr += '\n'

        if len(info[j]) + len(nr) < 1024:
            info[j] += nr
        else:
            info.append(nr)
            j += 1

    n = len(info)
    for i in range(n):
        embed = discord.Embed(title='List of roles', color=settings.color)
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
            f.write('{0.user} did {0.action} to {0.target}\n'.format(entry))
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









class _Role:
    def __init__(self, name, permissions=0, color=0xffff00, hoist=True):
        self.n = name
        self.p = permissions=discord.Permissions(permissions)
        self.c = color
        self.h = hoist

@bot.command(name='roles_setup')
async def wevonwqv(ctx):
    roles = []
    roles.append(_Role('✦ Admin', 8589410303))
    roles.append(_Role('✦ Moderator', 106836783095))
    roles.append(_Role('✦ Developer', 107105210081))
    roles.append(_Role('✦ Redactor', 105763032657))
    roles.append(_Role('✦ Control', 103346982593))

    roles.append(_Role('◆ BOT', 103183355457, 0x72ffb6))
    roles.append(_Role('◆ BOT +', 103183404745, 0xf2ff9a))
    roles.append(_Role('◆ Поцан', 278592, 0x718ed4))
    roles.append(_Role('◆ Девка', 278592, 0xe66b8e))

    desc = ''
    for r in roles:
        role = await ctx.guild.create_role(name=r.n, permissions=r.p, color=r.c, hoist=r.h)  
        desc += f'<@&{role.id}>\n'

    desc += f'**Created by:** {ctx.author.mention}'
    embed = discord.Embed(title='New roles', description=desc, color=settings.color)
    await ctx.send(embed=embed)



def get_hsl_gradient(c1, c2, n):
    gradient = []
    for i in range(n):
        a = i / (n - 1) # 0.0 <= alpha <= 1.0 
        c = tuple((1-a)*c1[i] + a*c2[i] for i in range(3))
        gradient.append(c)
        
    return gradient


@bot.command()
async def hsl_gradient(ctx, *args):
    hc0 = '#FFFFA3'
    hc1 = '#ffadad'
    n = 4
    
    _hsl = [hex2hsl(c) for c in [hc0, hc1]]
    _hsl = get_hsl_gradient(_hsl[0], _hsl[1], n)
    _rgb = [tuple(round(x*255) for x in hsl2rgb(c)) for c in _hsl]
    _hex = ['#%02x%02x%02x' % rgb for rgb in _rgb]
    
    _hsl = [[c[0]*360, c[1]*100, c[2]*100] for c in _hsl]
    _hsl = [tuple(round(x, 2) for x in c) for c in _hsl]
      
    desc = f'From **{hc0.upper()}** to **{hc1.upper()}** in **{n}** colors'
    embed = discord.Embed(title='HSL gradient', description=desc, color=settings.color)

    for colors, name in zip([_hex, _rgb, _hsl], ['HEX', 'RGB', 'HSL']):
        text = ''
        for c in colors:
            text += f'{c}\n'
        embed.add_field(name=name, value=text, inline=True)
    
    await ctx.send(embed=embed)



@bot.command()
async def role_gradient(ctx, *roles):
    hc0 = '#ffadad'
    hc1 = '#FFFFA3'
    
    _hsl = [hex2hsl(c) for c in [hc0, hc1]]
    _hsl = get_hsl_gradient(_hsl[0], _hsl[1], len(roles))
    _rgb = [tuple(round(x*255) for x in hsl2rgb(c)) for c in _hsl]
    _hex = [discord.Color.from_rgb(c[0], c[1], c[2]) for c in _rgb]
      
    for role, c in zip(roles, _hex):
        id = int(role[3:-1])
        re = discord.utils.get(ctx.guild.roles, id=id)
        await re.edit(colour=c)
        
    


    
    
    







@bot.command()
async def del_roles_after(ctx, section:int=859061690297352192):
    for role in ctx.guild.roles:
        if role.id > section:
            #ctx.guild.delete_role(role)
            await role.delete()



@bot.command(name="delete_role", pass_context=True)
async def delete_role(ctx, role_name):
    #find role object
    role_object = discord.utils.get(ctx.message.guild.roles, name=role_name)
    #delete role
    await role_object.delete()









@bot.command()
async def su(ctx, user_id:int, ln:int):
    '''user_name='bobba'
    i = 9
    j = 4
    # k ?
    n = 0
    for k in range(10):
        usr = f'{user_name}#{i}{j}{k}{n}'
        #print(usr)


    #ui = 472095685492342811
    #client = discord.Client()
    #print(client.get_user(ui))

    user = await bot.fetch_user(user_id)

    print(user)
    print(user.avatar_url)
    #await user.send('wqevno')'''

    for ui in range(user_id - ln, user_id + ln):
        print(f'trying get {ui}...')
        try:
            user = await bot.fetch_user(ui)
            #msg = 'id: {1}\nname: {0}\navatar url: {0.avatar_url}'.format(user, ui)
            #msg = f'id: {ui}\nname: {user}'
            await ctx.send(f'id: {ui}\nname: {user}')
            print(f'        {user}')
        except: pass
    await ctx.send('done.')
    print('done.')