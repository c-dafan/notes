
from datetime import date


def calculate_age_at_wedding(person):
    anniversary = person['anniversary']
    birthday = person['birthday']
    age = anniversary.year - birthday.year
    if birthday.replace(year=anniversary.year) > anniversary:
        age -= 1
    return age

