
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

translator pip install googletrans==3.1.0a0

vscode venv https://code.visualstudio.com/docs/python/environments

'''







class Settings:
    def __init__(self):
        self.prefix = '::'
        self.cmd_key = '--'
        self.color = 0xffff00 # 0xff6699
        self.help_keys = ['help', '-help', '--help', '--h']
        self.bot_name = 'soft mouse'