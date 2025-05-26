from tests.UserHelpers.create_utils import navigate_to_create_user_page, create_users
from tests.B2BUserHelpers.b2b_create_utils import navigate_to_b2b_user_page, create_b2b_users

def create(email, password):
    driver = navigate_to_create_user_page(email, password)
    create_users(driver)

    # Use same driver to continue to B2B
    driver = navigate_to_b2b_user_page(driver=driver)
    create_b2b_users(driver)

    return driver  # Optional: in case you want to use it for logout or further steps
