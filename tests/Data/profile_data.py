from faker import Faker
import random

fake = Faker()

def update(n):
    profiles = []
    for _ in range(n):
        profile = {
            "name": fake.name(),
            # "phone": f"+8801{random.randint(5, 9)}{random.randint(10000000, 99999999)}",
            "gender": random.choice(["Male", "Female", "Other"])
        }
        profiles.append(profile)
    return profiles

profile_to_update = update(n=2)

