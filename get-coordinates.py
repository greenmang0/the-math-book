#!/usr/bin/env python3

import math


def get_coordinates(angle_deg, distance):
    angle_rad = math.radians(angle_deg)
    x = distance * math.cos(angle_rad)
    y = distance * math.sin(angle_rad)
    return x, y


def get_coordinates2(angle_deg, x):
    angle_rad = math.radians(angle_deg)
    distance = x / math.cos(angle_rad)
    y = distance * math.sin(angle_rad)
    return distance, y


def calc_angle(angle1, angle2):
    return 180 - (angle1 + angle2)


def calc_triangle_side(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))
