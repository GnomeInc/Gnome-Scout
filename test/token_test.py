from rest_client import rest_api as rest


def get_token(username, password):
    token = rest.get_auth_token(username, password)
    # token = rest.get_auth_token('gnome', 'applepie')
    return token.json()['token']


# print(get_token('gnome', 'applepie'))
