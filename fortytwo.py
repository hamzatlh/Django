
from requests_oauthlib import OAuth2Session

# GOOGLE_OAUTH2_KEY='922319468084-nq7dm8cvet3imfm923idht837viuj38g.apps.googleusercontent.com'
# GOOGLE_OAUTH2_SECRET='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'
REDIRECT_URLS= 'https://isawi.tech'

client_id = 'u-s4t2ud-31a6f97b7d236cee545a64cc5bead01fc949922f335932f10c3ec638e6e5ce77'

client_secret = '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'

redirect_uri = REDIRECT_URLS


# Note that these are Google specific scopes

scope = [
    'public',
    'profile',
    ]

# "openid https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"

oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)

authorization_url, state = oauth.authorization_url('https://api.intra.42.fr/oauth/authorize')

print(f'Please go to  and authorize access:\n{authorization_url}')

authorization_response = input('Enter the full callback URL: ')


token = oauth.fetch_token(
        'https://api.intra.42.fr/oauth/token',
        authorization_response=authorization_response,
        client_secret=client_secret)


r = oauth.get('https://api.intra.42.fr/v2/me')

print(r.content)

