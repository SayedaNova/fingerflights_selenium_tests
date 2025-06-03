from faker import Faker
import random

fake = Faker()

roles = ["Admin", "Reservation Officer", "Manager", "Travel Consultant"]
genders = ["Male", "Female", "Other"]
statuses = ["Active", "Disable"]

def generate_fake_users(n):
    users = []
    for _ in range(n):
        name = fake.name()
        phone = "+8801" + str(random.randint(300000000, 999999999))
        email = fake.unique.email()
        password = "password"  # You can randomize this too
        role = random.choice(roles)
        gender = random.choice(genders)
        status = random.choice(statuses)

        user = {
            "name": name,
            "phone": phone,
            "email": email,
            "password": password,
            "confirm_password": password,
            "role": role,
            "gender": gender,
            "status": status,
            # Optionally add permissions here
        }
        users.append(user)
    return users

# Generate fake users
users_to_create = generate_fake_users(n=1)