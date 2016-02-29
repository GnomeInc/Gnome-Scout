from rest_client import rest_api as rest, models
from .token_test import get_token
import datetime
import random

def make_data(gnome):
    data = {
        'gnome': gnome,
        'date': datetime.datetime.now().date(),
        'time': datetime.datetime.now().time(),
        'temperature': random.randint(1,100),
        'humidity': random.randint(1,100),
        'light_level': random.randint(1,100),
        'soil_moisture': random.randint(1,100),
        'nutrient_level': random.randint(1,100),
    }

token = get_token()
data = make_data(1)
print(data)