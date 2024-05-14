from requests_oauthlib import OAuth2Session

class BaseOAuth:
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.oauth = OAuth2Session(self.client_id, redirect_uri=self.redirect_uri, scope=self.scope)

    def get_authorize_url(self, authorization_url):
        return self.oauth.authorization_url(authorization_url)


    def get_access_token(self, token_url, auth_response):
        print(self.client_secret)
        token = self.oauth.fetch_token(
            token_url,
            authorization_response=auth_response,
            client_secret=self.client_secret)
        return token

    def get_user_info(self, access_token):
        return self.oauth.get(access_token)
    
    # def do_oauth(self):
    #     authorization_url, state = self.get_authorize_url() # autherization url
    #     # redirect to authorization_url
    #     authorization_response = input('Enter the full callback URL: ') # change with callback view in django
    #     token = self.get_access_token(authorization_response)
    #     r = self.get_user_info(token)
    #     return r
    
# http://localhost:8000/api/oauth/42?