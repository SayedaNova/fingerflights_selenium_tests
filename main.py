from tests.CreateOperation.create_operation import create
from tests.UserHelpers.create_utils import email, password
from tests.AuthHelpers.logout_utils import logout_user
from tests.LeadHelpers.create_lead_utils import navigate_to_lead_page, create_lead
from tests.VendorHelpers.create_vendor_utils import navigate_to_vendor_page, create_vendor
from tests.PassengerHelpers.create_passenger_utils import navigate_to_passenger_page, create_passenger


if __name__ == "__main__":
    driver = create(email, password)
    # create(email, password)
    # navigate_to_lead_page(email, password, driver)
    # create_lead(driver)
    # navigate_to_vendor_page(email, password, driver)
    # create_vendor(driver)
    # navigate_to_passenger_page(email, password, driver)
    # create_passenger(driver)
    logout_user(driver, email)



