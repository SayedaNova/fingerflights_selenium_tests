#delete_user_utils.py

import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import tests.Demo_Data.create_b2b_data

def delete_passenger(driver, updated_passenger):
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
    time.sleep(2)

    rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'hover:shadow-md')]")
    for row in rows:
        if updated_passenger["email"] in row.text:
            try:
                # Find the delete button inside this specific row
                delete_btn = row.find_element(By.XPATH, ".//button[div[contains(@class, 'hover:bg-red-500')]]")
                driver.execute_script("arguments[0].click();", delete_btn)
                print(f"🗑️ Clicked delete for {updated_passenger['email']}")
            except Exception:
                raise Exception("❌ Delete button not found in the passenger's row.")
            break
    else:
        raise Exception(f"❌ Could not find passenger with email for deletion: {updated_passenger['email']}")

    try:
        # Wait for confirmation dialog
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='alertdialog']"))
        )

        time.sleep(3)

        # Click the 'Continue' button in the modal
        continue_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='alertdialog']//button[normalize-space()='Continue']"))
        )
        continue_btn.click()
        print(f"✅ Successfully deleted passenger {updated_passenger['email']}")

    except Exception as e:
        print(f"❌ Delete process failed for {updated_passenger['email']}: {e}")
        raise