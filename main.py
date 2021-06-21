
import discord
from discord.ext import commands
from config import Settings

settings = Settings()

#bot = commands.Bot(command_prefix = settings['prefix'])
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








#print(settings.invite_link())
#bot.run(settings['token'])
bot.run(settings.token)










