import string
from faker import Faker
import random
from datetime import datetime, timedelta, date
fake = Faker()
genders = ["Male", "Female", "Other"]
def generate_fake_passengers(n):

    passengers = []
    for _ in range(n):
        date_of_birth = date.today() + timedelta(days=random.randint(1, 60))
        passport_issue_date = date.today() + timedelta(days=random.randint(1, 60))
        passport_expiry_date = date.today() + timedelta(days=random.randint(1, 60))
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