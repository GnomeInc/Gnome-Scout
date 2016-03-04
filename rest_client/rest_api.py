import requests

# PATH = "http://127.0.0.1:8000/"
PATH = "https://secure-earth-85725.herokuapp.com/"


def _url(path):
    return PATH + path


def get_auth_token(username, password):
    payload = {'username': username, 'password': password}
    return requests.post(_url('api-token-auth/'), data=payload)


def get_data():
    return requests.get(_url('tracker/rest_index/'))


def add_data(token, data):
    return requests.post(_url('tracker/rest_index/'),
                         headers={'Authorization': "Token " + token},
                         json=data)


def get_datum(datum_id):
    pass


def get_users():
    pass


def get_user(user_id):
    pass


def get_gnomes():
    pass


def get_gnome(gnome_id):
    pass
