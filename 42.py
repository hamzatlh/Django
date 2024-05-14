from BaseOAuth import BaseOAuth
import os

class FortyTwoOAuth(BaseOAuth):
    AUTHERIZATION_URL = 'https://api.intra.42.fr/oauth/authorize'
    TOKEN_URL = 'https://api.intra.42.fr/oauth/token'
    INFO_URL = 'https://api.intra.42.fr/v2/me'

    def get_authorize_url(self):
        auth_url, state = super().get_authorize_url(self.AUTHERIZATION_URL)
        os.system(f'open {auth_url}')
        return auth_url
    
    def get_access_token(self, auth_response):
        return super().get_access_token(self.TOKEN_URL, auth_response)
    
    def get_user_info(self, access_token):
        return super().get_user_info(access_token)
    

if __name__ == '__main__':
    client_id = 'u-s4t2ud-31a6f97b7d236cee545a64cc5bead01fc949922f335932f10c3ec638e6e5ce77'
    client_secret = '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'
    redirect_uri = 'https://isawi.tech'

    scope = [
        'public',
        'profile',
    ]

    fortytwo = FortyTwoOAuth(client_id, client_secret, redirect_uri, scope)

    auth_url = fortytwo.get_authorize_url()

    auth_response = input('Enter the full callback URL: ')

    token = fortytwo.get_access_token(auth_response)

    r = fortytwo.get_user_info(token)

    print(r.content)
