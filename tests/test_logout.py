import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.helpers.login_utils import login_with_otp
from tests.users.user_data import users

def test_logout(driver):
    for email, password in users:
        driver = login_with_otp(email, password)  # ✅ Reuse login
        try:
            driver.get("http://178.128.114.165:73")
            wait = WebDriverWait(driver, 10)

            try:
                time.sleep(2)
                profile_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='S']]")))
                profile_button.click()
                time.sleep(2)
                wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitem' and normalize-space()='Sign out']"))).click()
                time.sleep(2)
            except Exception:
                print(f"❌ Logout button not found for user {email}")
        finally:
            driver.quit()