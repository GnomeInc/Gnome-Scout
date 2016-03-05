"""
    Author: Eric Kuha
    File: views.py
    Project: Gnome Scout

    Copyright: GnomeInc, Some Rights Reserved
"""


def make_data_set(data_dict):
    """
    Helper function to reconstruct the DataSet object from a dictionary.
    :param data_dict: The dictionary
    :return: the DataSet
    """
    return DataSet(
        data_dict['id'],
        data_dict['gnome'],
        data_dict['date'],
        data_dict['time'],
        data_dict['temperature'],
        data_dict['humidity'],
        data_dict['light_level'],
        data_dict['soil_moisture'],
        data_dict['nutrient_level']
    )


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

    def __init__(self, id, gnome, date, time, temperature, humidity, light_level, soil_moisture, nutrient_level):
        self.id = id
        self.gnome = gnome
        self.date = date
        self.time = time
        self.temperature = temperature
        self.humidity = humidity
        self.light_level = light_level
        self.soil_moisture = soil_moisture
        self.nutrient_level = nutrient_level
