from requests_oauthlib import OAuth2Session

GOOGLE_OAUTH2_KEY='922319468084-nq7dm8cvet3imfm923idht837viuj38g.apps.googleusercontent.com'
GOOGLE_OAUTH2_SECRET='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'
REDIRECT_URLS= 'https://isawi.tech'

client_id = GOOGLE_OAUTH2_KEY

client_secret = GOOGLE_OAUTH2_SECRET

redirect_uri = REDIRECT_URLS


# Note that these are Google specific scopes

scope = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'openid'
    ]

# "openid https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"

oauth = OAuth2Session(client_id, redirect_uri=redirect_uri,
                          scope=scope)

authorization_url, state = oauth.authorization_url(
        'https://accounts.google.com/o/oauth2/auth',
        # access_type and prompt are Google specific extra
        # parameters.
        access_type="offline", prompt="select_account")

print(f'Please go to  and authorize access:\n{authorization_url}')

authorization_response = input('Enter the full callback URL: ')


token = oauth.fetch_token(
        'https://accounts.google.com/o/oauth2/token',
        authorization_response=authorization_response,
        client_secret=client_secret)


r = oauth.get('https://www.googleapis.com/oauth2/v1/userinfo')

print(r.content)