from faker import Faker
import random

fake = Faker()

genders = ["Male", "Female", "Other"]
statuses = ["Active", "Disable"]

def generate_fake_b2b_users(n):
    b2b_users = []
    for _ in range(n):
        name = fake.company()
        phone = "+8801" + str(random.randint(300000000, 999999999))
        email = fake.unique.company_email()
        password = "password"
        gender = random.choice(genders)
        status = random.choice(statuses)

        b2b = {
            "name": name,
            "phone": phone,
            "email": email,
            "password": password,
            "confirm_password": password,
            "gender": gender,
            "status": status,
            # Optionally add permissions here
        }
        b2b_users.append(b2b)
    return b2b_users

# Generate fake B2B users
b2b_to_create = generate_fake_b2b_users(n=1)