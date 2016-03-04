from rest_client import rest_api as rest, models, rest_errors
from test.token_test import get_token
import datetime
import random


def make_data(gnome):
    return {
        'id': 0,
        'user': 1,
        'gnome': gnome,
        'date': datetime.datetime.now().date().strftime("%Y-%m-%d"),
        'time': datetime.datetime.now().time().strftime("%H:%M:%S"),
        'temperature': random.randint(1, 100),
        'humidity': random.randint(1, 100),
        'light_level': random.randint(1, 100),
        'soil_moisture': random.randint(1, 100),
        'soil_nutrients': random.randint(1, 100),
    }


token = get_token('gnome', '8af3b8180c860161e485479c8b26f353')
data = make_data(1)

ds = models.DataSet(data['id'],
                    data['user'],
                    data['gnome'],
                    data['date'],
                    data['time'],
                    data['temperature'],
                    data['humidity'],
                    data['light_level'],
                    data['soil_moisture'],
                    data['soil_nutrients'])

ds_dict = ds.__dict__

resp = rest.add_data(token, ds_dict)

if resp.status_code != 201:
    raise rest_errors.ApiError(resp.status_code, "Unable to post data")

print(resp.json())

mod = models.make_data_set(resp.json())

print(mod.light_level)