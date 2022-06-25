import math


def filter_odd_num(in_num):
    if (in_num % 2) == 0:
        return True
    else:
        return False

def test_filter_numbers():
    assert list(filter(filter_odd_num, [1, 2, 3, 4, 5, 6])) == [2, 4, 6]

def test_map_str():
    numbers = [1, 2, 3, 4, 5, 6]
    assert list(map(str, numbers)) == ['1', '2', '3', '4', '5', '6']

def test_sorted():
    actors = ['Harrison', 'Rutger', 'Shon', 'Daryl', 'James']
    assert sorted(actors) == ['Daryl', 'Harrison', 'James', 'Rutger', 'Shon']


def circumference(d):
    c = d * math.pi
    return math.ceil(c)

def test_with_math_pi():
    assert circumference(4) == 13

def test_math_sqrt():
    assert math.sqrt(9) == 3

def test_math_hypot():
    assert math.ceil(math.hypot(10, 5)) == 12

def test_math_pow():
    assert math.pow(2, 4) == 16