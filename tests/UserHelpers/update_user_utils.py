# tests/UserHelpers/update_user_utils.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.Data.user_info_data import users_to_create

def update_user_info(driver, user):
        # driver.get("http://178.128.114.165:73/user/list")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))

        time.sleep(3)

        # Find the row containing the user by email
        rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'hover:shadow-md')]")
        for row in rows:
            if user["email"] in row.text:
                edit_button = row.find_element(By.XPATH, ".//a[contains(@href, '/update/')]")
                edit_button.click()
                WebDriverWait(driver, 10).until(EC.url_contains("/user/update"))
                break
        else:
            raise Exception(f"❌ Could not find user with email: {user['email']}")

        # Update the name field to append " Updated"
        name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
        name_field.clear()
        updated_name = user["name"] + " Updated"
        name_field.send_keys(updated_name)

        time.sleep(2)

        try:
            # Try all common variations of submit buttons
            submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//button[@type='submit' and contains(text(), 'Submit')]"
            )))

            # Scroll to it and ensure it's visible
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", submit_button)
            time.sleep(0.5)

            # Confirm it's interactable
            if submit_button.is_displayed() and submit_button.is_enabled():
                driver.execute_script("arguments[0].click();", submit_button)
                print("✅ Form submitted via JavaScript click.")
            else:
                print("⚠️ Submit button found but not interactable. Trying JS click directly.")
                driver.execute_script("arguments[0].click();", submit_button)

            # Wait for redirect to the user list page
            WebDriverWait(driver, 10).until(EC.url_contains("/user/list"))
            print(f"✅ Updated user: {updated_name}")
            print("✅ Redirected to User List after submission.")

        except Exception as e:
            print(f"❌ Could not submit form or redirect failed: {e}")


