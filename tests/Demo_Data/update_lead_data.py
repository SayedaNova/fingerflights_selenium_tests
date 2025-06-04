# tests/Demo_Data/update_user_data.py

import random
from datetime import date, timedelta

from faker import Faker

fake = Faker()

sources = ["Phone Call", "Facebook", "Reference", "Repeat Customer", "Walking", "Friends & Family", "B2B",
               "Man Power"]
statuses = ["Lead", "Ongoing", "Negotiating", "Booking Done", "Wating For Final Confirmation", "Won", "Closed"]

closing_date = date.today() + timedelta(days=random.randint(1, 60))

def generate_updated_lead(original_lead):
    return {
        "name": original_lead["name"] + " Updated",
        "phone": "01" + str(random.randint(300000000, 999999999)),
        "email": fake.unique.email(),
        "potentiality": random.randint(1, 5),
        "source": random.choice(sources),
        "status": random.choice(statuses),
        # "division": division,
        # "district": district,
        # "upazila": upazila,
        "address": fake.address().replace("\n", ", "),
        "description": fake.text(max_nb_chars=20),
        "closing_date": closing_date.strftime('%B %d, %Y')
    }
