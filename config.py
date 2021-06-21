'''
https://discordapp.com/oauth2/authorize?&client_id=855554239991906335&scope=bot&permissions=67584
https://stackoverflow.com/questions/55012726/discord-py-unable-to-get-certificate
https://coderoad.ru/55012726/Discord-py-не-удалось-получить-сертификат
Install Certificates.command


https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html
https://discord.com/developers/applications
https://habr.com/ru/post/494600/
https://habr.com/ru/post/511454/

color https://www.w3schools.com/colors/colors_picker.asp

'''


settings_old = {
    'token': 'ODU1NTU0MjM5OTkxOTA2MzM1.YM0K-g.54Oh2uTawJ85Iu5IGJQZhV6F8JE',
    'bot': 'важный хуй',
    'id': 855554239991906335,
    'prefix': '::',
    'color': 0xff6699
}


class settings_from_1_bot:
    token = 'ODU1NTU0MjM5OTkxOTA2MzM1.YM0K-g.54Oh2uTawJ85Iu5IGJQZhV6F8JE'
    bot_name = 'важный хуй'
    bot_id = 855554239991906335
    prefix = '::'
    color = 0xff6699


class Settings:
    def __init__(self):
        self.token = 'ODU2NTU4ODY5MzMzNjcxOTY2.YNCynA.2WGUEIkR3FBLry3n2sVAd27z3O8'
        self.public_key = 'fd18bf047935c1ca367347ceedc05b856f3fa501b44f4c1c25c346bb7ca73515'
        self.app_id = 856558869333671966
        self.rights = 335629377
        self.prefix = '::'
        self.cmd_key = '--'
        self.color = 0xff6699
        #invite_link = f'https://discordapp.com/oauth2/authorize?&client_id={app_id}&scope=bot&permissions={rights}'
        #bot_name = 'важный хуй'

    def invite_link(self, r=None):
        #if not r:
        #    r = self.rights

        r = r if r else self.rights
        return f'https://discordapp.com/oauth2/authorize?&client_id={self.app_id}&scope=bot&permissions={r}'

    
