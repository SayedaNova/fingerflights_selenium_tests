from tests.Driver.driver_utils import get_driver
from tests.AuthHelpers.login_utils import login_with_otp
from tests.AuthHelpers.logout_utils import logout_user
from tests.users.user_data import users


def run_login_logout_all_in_one_window():
    driver = get_driver()
    try:
        for email, password in users:
            print(f"\n▶️ Logging in as {email}")
            login_with_otp(email, password, driver=driver)

            print(f"▶️ Logging out {email}")
            success = logout_user(driver, email)
            assert success, f"❌ Logout failed for {email}"

        print("✅ All users logged in and out in one window successfully.")
    finally:
        driver.quit()