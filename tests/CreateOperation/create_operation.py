from tests.AuthHelpers.logout_utils import logout_user
from tests.Data.user_data import SUPERADMIN_EMAIL
from tests.UserHelpers.create_utils import navigate_to_create_user_page, create_users
from tests.B2BUserHelpers.b2b_create_utils import navigate_to_b2b_user_page, create_b2b_users
from tests.LeadHelpers.create_lead_utils import navigate_to_lead_page, create_lead
from tests.VendorHelpers.create_vendor_utils import navigate_to_vendor_page, create_vendor
from tests.PassengerHelpers.create_passenger_utils import navigate_to_passenger_page, create_passenger
from tests.RoleHelpers.create_role_utils import navigate_to_create_role_page, create_roles

def create(email, password):

    #login && otp && user creation
    driver = navigate_to_create_user_page(email, password)
    create_users(driver)

    # # Use same driver to continue to B2B
    # driver = navigate_to_b2b_user_page(driver=driver)
    # create_b2b_users(driver)
    #
    # # Use same driver to continue to Leads
    # driver=navigate_to_lead_page(email, password, driver=driver)
    # create_lead(driver)
    #
    # # Use same driver to continue to Vendor
    # driver=navigate_to_vendor_page(email, password, driver=driver)
    # create_vendor(driver)
    #
    # # Use same driver to continue to Passenger
    # driver=navigate_to_passenger_page(email, password, driver=driver)
    # create_passenger(driver)
    #
    # # Use same driver to continue to Role
    driver=navigate_to_create_role_page(email, password, driver=driver)
    create_roles(driver)

    # logout_user(driver, SUPERADMIN_EMAIL)
    # logout_user(driver,email)

    return driver  # Optional: in case you want to use it for logout or further steps
