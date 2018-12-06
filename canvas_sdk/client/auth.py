from __future__ import unicode_literals
from requests.auth import AuthBase


class OAuth2Bearer(AuthBase):

    """ Attached Oauth2 HTTP Bearer Authentication to the given Request object """

    def __init__(self, oauth2_token):
        if not oauth2_token:
            raise AttributeError("OAuth2 token must be a non-empty string value.")
        self.oauth2_token = oauth2_token

    def __call__(self, r):
        # Modify and return the request
        r.headers['Authorization'] = 'Bearer ' + self.oauth2_token
        return r
