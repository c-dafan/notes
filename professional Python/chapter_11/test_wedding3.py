import unittest
from unittest import mock
from datetime import date
import sys
from wedding2 import calculate_age_at_wedding, get_person_from_db
import wedding2


class Tests(unittest.TestCase):
    def test_calculate_age_at_wedding(self):
        module = sys.modules[wedding2.__name__]
        with mock.patch.object(module, 'get_person_from_db') as m:
            person = {'anniversary': date(2012, 4, 21),
                      'birthday': date(1986, 6, 15)}
            m.return_value = person
            age = calculate_age_at_wedding(52)
            self.assertEqual(age, 25)
