from requests.auth import AuthBase


class OAuth2Bearer(AuthBase):
    """ Attached Oauth2 HTTP Bearer Authentication to the given Request object """
    def __init__(self, oauth2_token):
        if oauth2_token is None:
            raise AttributeError("OAuth2 token must be set to a value other than None.")
        self.oauth2_token = oauth2_token

    def __call__(self, r):
        # Modify and return the request
        r.headers['Authorization'] = 'Bearer ' + self.oauth2_token
        return r
