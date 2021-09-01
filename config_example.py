class Config:
    def __init__(self):
        self.token = ''        # insert a token
        self.public_key = ''   # insert a public key
        self.app_id = 0        # insert a app ID
        self.rights = 0        # insert a rights

    def invite_link(self, r=None):
        r = r if r else self.rights
        return f'https://discordapp.com/oauth2/authorize?&client_id={self.app_id}&scope=bot&permissions={r}'

    
