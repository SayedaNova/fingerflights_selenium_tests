from tests.helpers.login_utils import login_with_otp
from tests.users.user_data import users

def test_login_and_verify_otp(driver):
    for email, password in users:
        driver = login_with_otp(email, password)  # ✅ Reuse login
        driver.quit()
