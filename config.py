class Config:
    def __init__(self):
        self.token = 'ODU2NTU4ODY5MzMzNjcxOTY2.YNCynA.2WGUEIkR3FBLry3n2sVAd27z3O8'
        self.public_key = 'fd18bf047935c1ca367347ceedc05b856f3fa501b44f4c1c25c346bb7ca73515'
        self.app_id = 856558869333671966
        self.rights = 335629377

    def invite_link(self, r=None):
        r = r if r else self.rights
        return f'https://discordapp.com/oauth2/authorize?&client_id={self.app_id}&scope=bot&permissions={r}'

    
