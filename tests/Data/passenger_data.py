import string
from faker import Faker
import random
from datetime import datetime, timedelta, date
fake = Faker()
genders = ["Male", "Female", "Other"]

def random_date(start_date, end_date):
    """Generate a random date between start_date and end_date"""
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

def generate_fake_passengers(n):

    passengers = []
    today = date.today()
    for _ in range(n):
        # date_of_birth = date.today() + timedelta(days=random.randint(1, 60))
        # passport_issue_date = date.today() + timedelta(days=random.randint(1, 60))
        # passport_expiry_date = date.today() + timedelta(days=random.randint(1, 60))

        # Date of birth: between 18 and 60 years ago
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
        passenger = {
            "first_name": fake.name(),
            "last_name": fake.name(),
            "passport_number": passport_number,
            "date_of_birth": date_of_birth.strftime('%B %d, %Y'),
            "passport_issue_date": passport_issue_date.strftime('%B %d, %Y'),
            "passport_expiry_date": passport_expiry_date.strftime('%B %d, %Y'),
            "email": fake.unique.email(),
            "contact_number": "01" + str(random.randint(300000000, 999999999)),
            "nationality": random.randint(1, 225),
            "gender": random.choice(genders),
        }
        passengers.append(passenger)

    return passengers
# Example usage
passengers_to_create = generate_fake_passengers(n=1)