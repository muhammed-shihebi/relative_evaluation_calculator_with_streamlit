import math
import numpy as np

def get_limit(m, s, t, v):
    return round(m + (s * (v + ((5.7-t) * math.exp(-m/100)))), 3)

def cal_letter(my_grade, m, s, t):
    if my_grade >= get_limit(m, s, t, -2.0):
        return 'AA'
    elif my_grade >= get_limit(m, s, t, -2.3):
        return 'AB'
    elif my_grade >= get_limit(m, s, t, -2.7): 
        return 'BA'
    elif my_grade >= get_limit(m, s, t, -3.0): 
        return 'BB'
    elif my_grade >= get_limit(m, s, t, -3.3): 
        return 'BC'
    elif my_grade >= get_limit(m, s, t, -3.7): 
        return 'CB'
    elif my_grade >= get_limit(m, s, t, -4.0): 
        return 'CC'
    elif my_grade >= get_limit(m, s, t, -4.3): 
        return 'DC'
    elif my_grade >= get_limit(m, s, t, -4.7): 
        return 'DD'
    elif my_grade >= get_limit(m, s, t, -5.0): 
        return 'DF'
    elif my_grade >= get_limit(m, s, t, -5.1): 
        return 'FD'
    else: 
        return 'FF'

def get_letters(m, s, t):

    limits = np.array([
        get_limit(m, s, t, -2.0),
        get_limit(m, s, t, -2.3),
        get_limit(m, s, t, -2.7),
        get_limit(m, s, t, -3.0),
        get_limit(m, s, t, -3.3),
        get_limit(m, s, t, -3.7),
        get_limit(m, s, t, -4.0),
        get_limit(m, s, t, -4.3),
        get_limit(m, s, t, -4.7),
        get_limit(m, s, t, -5.0),
        get_limit(m, s, t, -5.1),
        0
    ])
    letters = np.array([
        "AA",
        "AB",
        "BA",
        "BB",
        "BC",
        "CB",
        "CC",
        "DC",
        "DD",
        "DF",
        "FD",
        "FF"
    ])

    grades = np.array([
        4.0,
        3.7,
        3.3,
        3.0,
        2.7,
        2.3,
        2.0,
        1.7,
        1.3,
        1.0,
        0.5,
        0.0
    ])

    return (letters, limits, grades)