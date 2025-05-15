# from tests.AuthHelpers.driver_utils import get_driver
# from tests.AuthHelpers.login_utils import login_with_otp
# from tests.AuthHelpers.logout_utils import logout_user
# from tests.Data.user_data import Data
#
# def test_login_logout_all_users_in_one_window():
#     driver = get_driver()
#     try:
#         for email, password in Data:
#             print(f"\n▶️ Logging in as {email}")
#             login_with_otp(email, password, driver=driver)
#
#             print(f"▶️ Logging out {email}")
#             success = logout_user(driver, email)
#             assert success, f"❌ Logout failed for {email}"
#
#         print("✅ All Data logged in and out in one window successfully.")
#     finally:
#         driver.quit()
#
#
#
