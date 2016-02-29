from rest_client import rest_api as rest


def get_token():
    token = rest.get_auth_token('gnome', 'applepie')
    return token.json()['token']
