from faker import Faker

fake = Faker()

# Function to generate a single permission with all CRUD
def get_permission_entry(name):
    return {
        "name": name,
        "create": True,
        "read": True,
        "update": True,
        "delete": True
    }

# Function to generate fake roles with only "Dashboard" permission
def generate_fake_roles(n):
    roles = []
    for _ in range(n):
        role = {
            "role_name": fake.name(),
            "permissions": [get_permission_entry("Dashboard")]
        }
        roles.append(role)
    return roles

# Generate fake roles
roles_to_create = generate_fake_roles(n=1)



# fake = Faker()
#
# # Full list of permission names
# all_permissions = [
#     "Dashboard",  # Always included
#     # "Profile",  # Always included
#     # "Vendor",
#     # "Lead",
#     # "Lead_statistics",
#     # "Passenger",
# ]
#
# # Function to generate a single permission with all CRUD
# def get_permission_entry(name):
#     return {
#         "name": name,
#         # "create": True,
#         "read": True,
#         # "update": True,
#         # "delete": True
#     }
#
# # Function to generate fake roles
# # def generate_fake_roles(n):
# #     roles = []
# #     for _ in range(n):
# #         role_name = fake.name()
# #         # Ensure "Dashboard" and "Profile" are always included
# #         required = {"Dashboard", "Profile"}
# #         optional = list(set(all_permissions) - required)
# #         selected = random.sample(optional, random.randint(3, 6))
# #         permission_names = list(required) + selected
# #         permissions = [get_permission_entry(name) for name in permission_names]
# #
# #         role = {
# #             "role_name": role_name,
# #             "permissions": permissions
# #         }
# #         roles.append(role)
# #     return roles
#
# # Function to generate fake roles
# def generate_fake_roles(n):
#     roles = []
#     for _ in range(n):
#         role_name = fake.name()
#         # required = {"Dashboard", "Profile"}
#         required = {"Dashboard"}
#         optional = list(set(all_permissions) - required)
#
#         # Safe sample size: between 0 and len(optional)
#         sample_size = min(len(optional), random.randint(1, 3))  # Adjust range as needed
#         selected = random.sample(optional, sample_size)
#
#         permission_names = list(required) + selected
#         permissions = [get_permission_entry(name) for name in permission_names]
#
#         role = {
#             "role_name": role_name,
#             "permissions": permissions
#         }
#         roles.append(role)
#     return roles
#
#
# # Generate fake roles
# roles_to_create = generate_fake_roles(n=1)
