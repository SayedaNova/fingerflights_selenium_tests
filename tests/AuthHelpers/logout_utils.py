import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def logout_user(driver, email):
    # email = "trendssaas24@gmail.com"
    try:
        wait = WebDriverWait(driver, 10)

        time.sleep(5)
        # profile_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='S']]")))
        profile_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@aria-haspopup='menu' and contains(@class, 'rounded-full')]"
        )))

        profile_button.click()
        time.sleep(5)
        logout_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='menuitem' and normalize-space()='Sign out']")
        ))
        logout_button.click()
        time.sleep(5)

        if "login" in driver.current_url:
            print(f"✅ Logged out {email}")
            return True
        else:
            print(f"❌ Still logged in after logout attempt: {email}")
            return False

    except Exception as e:
        print(f"❌ Error during logout for {email}: {e}")
        return False

    finally:
        return driver
        # driver.quit()
