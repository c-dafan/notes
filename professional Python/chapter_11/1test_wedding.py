import unittest
from datetime import date
from wedding import calculate_age_at_wedding


class Tests(unittest.TestCase):
    def test_calculate_age_at_wedding(self):
        person = {'anniversary': date(2012, 4, 21),
                  'birthday': date(1986, 6, 15)}
        age = calculate_age_at_wedding(person)
        self.assertEqual(age, 25)

        person = {'anniversary': date(1969, 8, 11),
                  'birthday': date(1945, 2, 15)}
        age = calculate_age_at_wedding(person)
        self.assertEqual(age, 24)

    def test_failure_case(self):
        person = {'anniversary': date(2012, 4, 21),
                  'birthday': date(1986, 6, 15)}
        age = calculate_age_at_wedding(person)
        self.assertEqual(age, 99)

    def test_error_case(self):
        person = {}
        age = calculate_age_at_wedding(person)
        self.assertEqual(age, 25)

    @unittest.skipIf(True, 'this test was skip')
    def test_skipped_case(self):
        pass
