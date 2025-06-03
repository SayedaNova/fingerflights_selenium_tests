# tests/Module_Data/update_user_data.py

import random
from faker import Faker

fake = Faker()

genders = ["Male", "Female", "Other"]
statuses = ["Active", "Disable"]

def generate_updated_b2b(original_b2b):
    return {
        "name": original_b2b["name"] + " Updated",
        "phone": "+8801" + str(random.randint(300000000, 999999999)),
        "email": fake.unique.email(),
        "password": "newpassword123",
        "confirm_password": "newpassword123",
        "gender": random.choice(genders),
        "status": random.choice(statuses),
    }
