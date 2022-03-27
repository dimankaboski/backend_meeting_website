import logging
import math


def coord_range(coordinates, dist) -> list:
    """
    Вычисляет допустимый диапазон точек широты и долготы, 
    возвращает список мин. и макс. широты и
    мин. и макс. долготы
    """
    one_minute_lat = math.cos(math.radians(coordinates[0])) * 111.321377778 / 60 #км в минуте широты
    one_minute_lon = 40008.55 / 360 / 60 #км в минуте долготы
    minutes_range = [dist / one_minute_lat / 60, dist / one_minute_lon / 60] #дельта в координатах
    coords_range = [coordinates[0] - minutes_range[0], coordinates[0] + minutes_range[0], coordinates[1] - minutes_range[1], coordinates[1] + minutes_range[1]] #допустимый диапазон координат
    return coords_range
