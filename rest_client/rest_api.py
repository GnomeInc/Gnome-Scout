import requests

PATH = "http://127.0.0.1:8000/"


def _url(path):
    return PATH + path


def get_auth_token(username, password):
    payload = {'username': username, 'password': password}
    return requests.post(_url('api-token-auth/'), data=payload)


def get_data():
    return requests.get(_url('tracker/rest_index/'))


def add_data(token, user, gnome, date, time, temperature, humidity, light_level, soil_moisture, soil_nutrients):
    pass


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