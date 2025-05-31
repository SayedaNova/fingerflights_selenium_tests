import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.Data import role_data


def update_role(driver, role):
    wait = WebDriverWait(driver, 10)

    # Wait for roles table to load
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
    time.sleep(2)  # small delay to ensure full rendering

    # Find the row containing the role by name
    rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'hover:shadow-md')]")
    role_name_lower = role["role_name"].strip().lower()
    for row in rows:
        row_text = row.text.strip().lower()
        if role_name_lower in row_text:
            edit_button = row.find_element(By.XPATH, ".//a[contains(@href, '/update/')]")
            edit_button.click()
            wait.until(EC.url_contains("/roles/update"))
            print(f"Navigated to update page for role: {role['role_name']}")
            break
    else:
        raise Exception(f"❌ Could not find role with name: {role['role_name']}")

    # Fill and submit the update form
    role_input = wait.until(EC.presence_of_element_located((
            By.XPATH, "//input[@placeholder='Role name']"
        )))
    role_input.clear()
    role_input.send_keys(role["role_name"])
    print(f"Role name input filled with: {role['role_name']}")

    try:
        # Scroll to bottom of page to ensure submit button is visible
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)

        submit_button = wait.until(EC.presence_of_element_located((
            By.XPATH, "//button[contains(@class, 'bg-ffblue') and normalize-space(text())='Submit']"
        )))

        wait.until(EC.element_to_be_clickable(submit_button))

        submit_button.click()
        print("✅ Form submitted successfully")

        wait.until(EC.url_contains("/roles/list"))
        print("✅ Redirected to Role List after submission.")

    except Exception as e:
        print(f"❌ Could not submit form or redirect failed: {e}")


