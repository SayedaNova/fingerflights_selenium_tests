# tests/Demo_Data/update_user_data.py

import random
import string
from datetime import date, timedelta

from faker import Faker

fake = Faker()

genders = ["Male", "Female", "Other"]

def random_date(start_date, end_date):
    """Generate a random date between start_date and end_date"""
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

today = date.today()

def generate_updated_passenger(original_passenger):
    dob_start = today.replace(year=today.year - 60)
    dob_end = today.replace(year=today.year - 18)
    date_of_birth = random_date(dob_start, dob_end)

    # Passport issue date: between 10 years ago and today
    passport_issue_start = today.replace(year=today.year - 10)
    passport_issue_date = random_date(passport_issue_start, today)

    # Passport expiry date: between issue date + 1 year and issue date + 10 years
    expiry_start = passport_issue_date + timedelta(days=365)  # +1 year
    expiry_end = passport_issue_date + timedelta(days=365 * 10)  # +10 years
    passport_expiry_date = random_date(expiry_start, expiry_end)

    passport_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(8, 12)))
    return {
        "first_name": original_passenger["first_name"] + " Updated",
        "last_name": fake.last_name(),
        "passport_number": passport_number,
        "date_of_birth": date_of_birth.strftime('%B %d, %Y'),
        "passport_issue_date": passport_issue_date.strftime('%B %d, %Y'),
        "passport_expiry_date": passport_expiry_date.strftime('%B %d, %Y'),
        "email": fake.unique.email(),
        "contact_number": "01" + str(random.randint(300000000, 999999999)),
        "gender": random.choice(genders),
    }
