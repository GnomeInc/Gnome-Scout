"""
    Author: Eric Kuha
    File: views.py
    Project: Gnome Scout

    Copyright: GnomeInc, Some Rights Reserved
"""

from datetime import date
import json


class DataSet:
    """
    This model represents one point of data, including a date, time, and conditions at that moment.
    :id:                Only necessary when pulling from server.
    :user:              associated with this gnome's data
    :gnome:             gnome that sent this datum
    :date:              date of datum harvest
    :time:              time of datum harvest
    :temperature:       temp at time of datum harvest
    :humidity:          humidity at time of datum harvest
    :light_level:       light level at time of harvest
    :soil_moisture:     soil moisture level normalized to optimal soil moisture for plants
    """

    def __init__(self, id, user, gnome, date, time, temperature, humidity, light_level, soil_moisture, soil_nutrients):
        self.id = id
        self.user = user
        self.gnome = gnome
        self.date = date
        self.time = time
        self.temperature = temperature
        self.humidity = humidity
        self.light_level = light_level
        self.soil_moisture = soil_moisture
        self.soil_nutrients = soil_nutrients
