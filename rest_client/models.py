"""
    Author: Eric Kuha
    File: views.py
    Project: Gnome Scout

    Copyright: GnomeInc, Some Rights Reserved
"""

from datetime import date


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

    def __init__(self, data_dict = None):
        if data_dict is None:
            pass
        else:
            self.id = data_dict['id']
            self.user = data_dict['user']
            self.gnome = data_dict['gnome']
            self.date = date(data_dict['date'])
            self.time = data_dict['time']
            self.temperature = float(data_dict['temperature'])
            self.humidity = float(data_dict['humidity'])
            self.light_level = int(data_dict['light_level'])
            self.soil_moisture = int(data_dict['soil_moisture'])




