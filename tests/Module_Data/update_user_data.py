# tests/Module_Data/update_user_data.py

import random
from faker import Faker

fake = Faker()

roles = ["Admin", "Reservation Officer", "Manager", "Travel Consultant"]
genders = ["Male", "Female", "Other"]
statuses = ["Active", "Disable"]

def generate_updated_user(original_user):
    return {
        "name": original_user["name"] + " Updated",
        "phone": "+8801" + str(random.randint(300000000, 999999999)),
        "email": fake.unique.email(),
        "password": "newpassword123",
        "confirm_password": "newpassword123",
        "role": random.choice(roles),
        "gender": random.choice(genders),
        "status": random.choice(statuses),
    }
