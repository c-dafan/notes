import unittest
from unittest import mock
from datetime import date
import sys


def get_person_from_db(person_id):
    raise RuntimeError("the real 'get_person_from_db' function", 'was called')


def calculate_age_at_wedding(person_id):
    person = get_person_from_db(person_id)
    anniversary = person['anniversary']
    birthday = person['birthday']
    age = anniversary.year - birthday.year
    if birthday.replace(year=anniversary.year) > anniversary:
        age -= 1
    return age


class Tests(unittest.TestCase):
    def test_calculate_age_at_wedding(self):
        module = sys.modules[__name__]
        with mock.patch.object(module, 'get_person_from_db') as m:
            person = {'anniversary': date(2012, 4, 21),
                      'birthday': date(1986, 6, 15)}
            m.return_value = person
            age = calculate_age_at_wedding(52)
            self.assertEqual(age, 24)
