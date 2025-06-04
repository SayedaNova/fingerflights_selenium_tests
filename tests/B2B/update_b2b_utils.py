# # tests/Users/update_user_utils.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.Demo_Data.update_b2b_data import generate_updated_b2b
from tests.Demo_Data.update_b2b_data import generate_updated_b2b


def update_b2b(driver, original_b2b):
    updated_b2b = generate_updated_b2b(original_b2b)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
    time.sleep(3)

    # Find the row containing the original user by original email
    rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'hover:shadow-md')]")
    for row in rows:
        if original_b2b["email"] in row.text:
            edit_button = row.find_element(By.XPATH, ".//a[contains(@href, '/update/')]")
            edit_button.click()
            WebDriverWait(driver, 10).until(EC.url_contains("/b2b/update"))
            break
    else:
        raise Exception(f"❌ Could not find b2b with email: {original_b2b['email']}")

    # --- Update input fields ---
    name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
    name_field.clear()
    name_field.send_keys(updated_b2b["name"])

    email_field = driver.find_element(By.NAME, "email")
    email_field.clear()
    email_field.send_keys(updated_b2b["email"])

    phone_field = driver.find_element(By.NAME, "phone")
    phone_field.clear()
    phone_field.send_keys(updated_b2b["phone"])

    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys(updated_b2b["password"])

    password_confirmation_field = driver.find_element(By.NAME, "password_confirmation")
    password_confirmation_field.clear()
    password_confirmation_field.send_keys(updated_b2b["confirm_password"])

    # --- GENDER ---
    current_gender = driver.execute_script("""
        const selected = document.querySelector("button[role='radio'][aria-checked='true']");
        return selected ? selected.value : null;
    """)
    desired_gender = updated_b2b["gender"].lower()
    if current_gender != desired_gender:
        gender_button = driver.find_element(By.XPATH, f"//button[@role='radio' and @value='{desired_gender}']")
        driver.execute_script("arguments[0].click();", gender_button)
        print(f"✅ Updated gender to: {updated_b2b['gender']}")
    else:
        print(f"ℹ️ Gender already set to '{updated_b2b['gender']}', no change made.")

    # --- STATUS ---
    current_status = driver.execute_script("""
        const selected = document.querySelectorAll("button[role='radio'][name='status']");
        for (let btn of selected) {
            if (btn.getAttribute('aria-checked') === 'true') return btn.value;
        }
        return null;
    """)
    desired_status = "1" if updated_b2b["status"].lower() == "active" else "0"
    if current_status != desired_status:
        status_button = driver.find_element(By.XPATH, f"//button[@role='radio' and @value='{desired_status}']")
        driver.execute_script("arguments[0].click();", status_button)
        print(f"✅ Updated status to: {updated_b2b['status']}")
    else:
        print(f"ℹ️ Status already set to '{updated_b2b['status']}', no change made.")

    # --- Submit ---
    try:
        submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, "//button[@type='submit' and contains(text(), 'Submit')]"
        )))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", submit_button)
        time.sleep(0.5)

        if submit_button.is_displayed() and submit_button.is_enabled():
            driver.execute_script("arguments[0].click();", submit_button)
        else:
            print("⚠️ Submit button found but not interactable. Trying JS click directly.")
            driver.execute_script("arguments[0].click();", submit_button)

        WebDriverWait(driver, 10).until(EC.url_contains("/b2b/list"))
        print(f"✅ Updated b2b to: {updated_b2b['name']}")
        print("✅ Redirected to B2b List after submission.")
        print(updated_b2b)
    except Exception as e:
        print(f"❌ Could not submit form or redirect failed: {e}")

    return updated_b2b
