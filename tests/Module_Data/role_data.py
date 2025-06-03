# # # from faker import Faker
# # #
# # # fake = Faker()
# # #
# # # # Function to generate a single permission with all CRUD
# # # def get_permission_entry(name):
# # #     return {
# # #         "name": name,
# # #         "create": True,
# # #         "read": True,
# # #         "update": True,
# # #         "delete": True
# # #     }
# # #
# # # # Function to generate fake roles with only "Dashboard" permission
# # # def generate_fake_roles(n):
# # #     roles = []
# # #     for _ in range(n):
# # #         role = {
# # #             "role_name": fake.name(),
# # #             "permissions": [get_permission_entry("Dashboard")]
# # #         }
# # #         roles.append(role)
# # #     return roles
# # #
# # # # Generate fake roles
# # # roles_to_create = generate_fake_roles(n=1)
# # #
# # #
# # #
# # # # fake = Faker()
# # # #
# # # # # Full list of permission names
# # # # all_permissions = [
# # # #     "Dashboard",  # Always included
# # # #     # "Profile",  # Always included
# # # #     # "Vendor",
# # # #     # "Lead",
# # # #     # "Lead_statistics",
# # # #     # "Passenger",
# # # # ]
# # # #
# # # # # Function to generate a single permission with all CRUD
# # # # def get_permission_entry(name):
# # # #     return {
# # # #         "name": name,
# # # #         # "create": True,
# # # #         "read": True,
# # # #         # "update": True,
# # # #         # "delete": True
# # # #     }
# # # #
# # # # # Function to generate fake roles
# # # # # def generate_fake_roles(n):
# # # # #     roles = []
# # # # #     for _ in range(n):
# # # # #         role_name = fake.name()
# # # # #         # Ensure "Dashboard" and "Profile" are always included
# # # # #         required = {"Dashboard", "Profile"}
# # # # #         optional = list(set(all_permissions) - required)
# # # # #         selected = random.sample(optional, random.randint(3, 6))
# # # # #         permission_names = list(required) + selected
# # # # #         permissions = [get_permission_entry(name) for name in permission_names]
# # # # #
# # # # #         role = {
# # # # #             "role_name": role_name,
# # # # #             "permissions": permissions
# # # # #         }
# # # # #         roles.append(role)
# # # # #     return roles
# # # #
# # # # # Function to generate fake roles
# # # # def generate_fake_roles(n):
# # # #     roles = []
# # # #     for _ in range(n):
# # # #         role_name = fake.name()
# # # #         # required = {"Dashboard", "Profile"}
# # # #         required = {"Dashboard"}
# # # #         optional = list(set(all_permissions) - required)
# # # #
# # # #         # Safe sample size: between 0 and len(optional)
# # # #         sample_size = min(len(optional), random.randint(1, 3))  # Adjust range as needed
# # # #         selected = random.sample(optional, sample_size)
# # # #
# # # #         permission_names = list(required) + selected
# # # #         permissions = [get_permission_entry(name) for name in permission_names]
# # # #
# # # #         role = {
# # # #             "role_name": role_name,
# # # #             "permissions": permissions
# # # #         }
# # # #         roles.append(role)
# # # #     return roles
# # # #
# # # #
# # # # # Generate fake roles
# # # # roles_to_create = generate_fake_roles(n=1)
# #
# # from faker import Faker
# #
# # fake = Faker()
# #
# # # Full list of permission names (including commented ones)
# # all_permissions = [
# #     "Dashboard",  # Always included for new roles
# #     "Profile",
# #     "Vendor",
# #     "Lead",
# #     "Lead_statistics",
# #     "Passenger",
# # ]
# #
# #
# # def get_permission_entry(name, include_crud=False):
# #     """Generate a permission entry with optional CRUD fields"""
# #     permission = {
# #         "name": name,
# #         "read": True  # Default to True since Dashboard needs at least read
# #     }
# #
# #     if include_crud:
# #         permission.update({
# #             "create": True,
# #             "update": True,
# #             "delete": True
# #         })
# #     return permission
# #
# #
# # def generate_role_data(for_creation=True, include_permissions=None):
# #     """
# #     Generate role data for either creation or updating
# #     Args:
# #         for_creation: If True, generates data for role creation (only Dashboard)
# #         include_permissions: List of additional permissions to include (for updates)
# #     """
# #     role_data = {
# #         "role_name": fake.name(),
# #         "permissions": [get_permission_entry("Dashboard")]
# #     }
# #
# #     # For updates or when specific permissions are requested
# #     if not for_creation and include_permissions:
# #         # Ensure we don't duplicate Dashboard
# #         additional_perms = [p for p in include_permissions if p != "Dashboard"]
# #         for perm_name in additional_perms:
# #             if perm_name in all_permissions:
# #                 role_data["permissions"].append(get_permission_entry(perm_name, include_crud=True))
# #
# #     return role_data
# #
# # # Example usage:
# # # For roles_crud.py:
# # new_role = generate_role_data(for_creation=True)
# #
# # # For update_role_utils.py:
# # updated_role = generate_role_data(
# #     for_creation=False,
# #     include_permissions=["Profile", "Vendor"]  # Add whatever permissions you want
# # )
#
#
# from faker import Faker
#
# fake = Faker()
#
# # Full list of permission names
# all_permissions = [
#     "Dashboard",  # Always included
#     "Profile",
#     "Vendor",
#     "Lead",
#     "Lead_statistics",
#     "Passenger",
# ]
#
#
# # Function to generate a single permission entry
# def get_permission_entry(name, include_crud=True):
#     if name == "Dashboard":
#         # Dashboard always has only read permission
#         return {
#             "name": name,
#             "read": True,
#             "create": False,
#             "update": False,
#             "delete": False
#         }
#     elif not include_crud:
#         # For create role, only Dashboard is allowed
#         return None
#     else:
#         # For update role, all permissions with all CRUD
#         return {
#             "name": name,
#             "create": True,
#             "read": True,
#             "update": True,
#             "delete": True
#         }
#
#
# # Function to generate fake roles
# def generate_fake_roles(n, for_update=False):
#     roles = []
#     for _ in range(n):
#         role = {
#             "role_name": fake.name(),
#             "permissions": []
#         }
#
#         # Always include Dashboard
#         dashboard_perm = get_permission_entry("Dashboard")
#         role["permissions"].append(dashboard_perm)
#
#         # Include other permissions only for update
#         if for_update:
#             for perm in all_permissions[1:]:  # Skip Dashboard
#                 perm_entry = get_permission_entry(perm, include_crud=True)
#                 if perm_entry:
#                     role["permissions"].append(perm_entry)
#
#         roles.append(role)
#     return roles
#
# # # Example usage:
# # # For create role:
# # roles_to_create = generate_fake_roles(1, for_update=False)
# # # For update role:
# # roles_to_update = generate_fake_roles(1, for_update=True)
#
from faker import Faker

fake = Faker()

# Full list of permission names
all_permissions = [
    "Dashboard",  # Always included
    "Profile",
    "Vendor",
    "Lead",
    "Lead_statistics",
    "Passenger",
]

# Store the generated role name so we can use it for both create and update
current_role_name = None


def get_current_role_name():
    global current_role_name
    if current_role_name is None:
        current_role_name = fake.name()
    return current_role_name


def get_permission_entry(name, include_crud=True):
    if name == "Dashboard":
        return {
            "name": name,
            "read": True,
            "create": True,
            "update": True,
            "delete": True
        }
    elif not include_crud:
        return None
    else:
        return {
            "name": name,
            "create": True,
            "read": True,
            "update": True,
            "delete": True
        }


def generate_fake_roles(n, for_update=False):
    global current_role_name
    roles = []

    # Use the same role name for create and update
    role_name = get_current_role_name()

    role = {
        "role_name": role_name,
        "permissions": []
    }

    # Always include Dashboard
    dashboard_perm = get_permission_entry("Dashboard")
    role["permissions"].append(dashboard_perm)

    # Include other permissions only for update
    if for_update:
        for perm in all_permissions[1:]:  # Skip Dashboard
            perm_entry = get_permission_entry(perm, include_crud=True)
            if perm_entry:
                role["permissions"].append(perm_entry)

    roles.append(role)
    return roles


# Initialize with the same role name
roles_to_create = generate_fake_roles(1, for_update=False)
roles_to_update = generate_fake_roles(1, for_update=True)