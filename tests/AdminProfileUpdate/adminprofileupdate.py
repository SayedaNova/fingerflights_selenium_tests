from tests.Auth.login_utils import login_with_otp
from tests.Auth.logout_utils import logout_user
# from tests.Demo_Data.user_data import ADMIN_EMAIL, ADMIN_PASSWORD
from tests.Profile.profile_utils import navigate_to_edit_profile_page, profile_update


def admin_profile_update(email, password, driver=None):

    # login_with_otp(ADMIN_EMAIL, ADMIN_PASSWORD, driver=driver)
    driver = login_with_otp(email, password, driver=driver)

    # navigate_to_edit_profile_page(ADMIN_EMAIL, ADMIN_PASSWORD, driver=driver)
    navigate_to_edit_profile_page(email, password, driver=driver)
    profile_update(driver)

    # logout_user(driver, ADMIN_EMAIL)
    logout_user(driver,email)

    return driver