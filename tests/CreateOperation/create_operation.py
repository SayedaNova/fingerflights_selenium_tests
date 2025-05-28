from tests.UserHelpers.create_utils import navigate_to_create_user_page, create_users
from tests.B2BUserHelpers.b2b_create_utils import navigate_to_b2b_user_page, create_b2b_users
from tests.LeadHelpers.create_lead_utils import navigate_to_lead_page, create_lead
from tests.VendorHelpers.create_vendor_utils import navigate_to_vendor_page, create_vendor
from tests.PassengerHelpers.create_passenger_utils import navigate_to_passenger_page, create_passenger

def create(email, password):
    driver = navigate_to_create_user_page(email, password)
    create_users(driver)

    # Use same driver to continue to B2B
    driver = navigate_to_b2b_user_page(driver=driver)
    create_b2b_users(driver)

    driver=navigate_to_lead_page(email, password, driver=driver)
    create_lead(driver)

    driver=navigate_to_vendor_page(email, password, driver=driver)
    create_vendor(driver)

    driver=navigate_to_passenger_page(email, password, driver=driver)
    create_passenger(driver)

    return driver  # Optional: in case you want to use it for logout or further steps
