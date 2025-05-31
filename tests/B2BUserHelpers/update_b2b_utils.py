# tests/UserHelpers/update_user_utils.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.Data.b2b_data import b2b_to_create

def update_b2b_info(driver, b2b):
        # driver.get("http://178.128.114.165:73/user/list")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))

        time.sleep(3)

        # Find the row containing the user by email
        rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'hover:shadow-md')]")
        for row in rows:
            if b2b["email"] in row.text:
                edit_button = row.find_element(By.XPATH, ".//a[contains(@href, '/update/')]")
                edit_button.click()
                WebDriverWait(driver, 10).until(EC.url_contains("/b2b/update"))
                break
        else:
            raise Exception(f"❌ Could not find user with email: {b2b['email']}")

        # Update the name field to append " Updated"
        name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
        name_field.clear()
        updated_name = b2b["name"] + " Updated"
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
            WebDriverWait(driver, 10).until(EC.url_contains("/b2b/list"))
            print(f"✅ Updated b2b user: {updated_name}")
            print("✅ Redirected to B2B List after submission.")

        except Exception as e:
            print(f"❌ Could not submit form or redirect failed: {e}")


