users_to_create = [
    {
        "name": "Test User One",
        "phone": "+8801331077973",
        "email": "testuser1@example.com",
        "password": "password123",
        "confirm_password": "password123!",
        "role": "Admin",  # Choose from: Admin, Reservation Officer, Manager, Travel Consultant
        "gender": "Male",  # Male / Female / Other
        "status": "Active",  # Active / Disable
        "permissions": {
            "Dashboard": {"Create": True, "Read": True, "Update": False, "Delete": False},
            # Add more modules as needed...
        }
    },

    {
        "name": "Test User Two",
        "phone": "+8801791234567",
        "email": "testuser2@example.com",
        "password": "password",
        "confirm_password": "password",
        "role": "Travel Consultant",
        "gender": "Female",
        "status": "Disable",
        "permissions": {
            "Dashboard": {"Create": True, "Read": True, "Update": False, "Delete": False},
        }
    }
]
