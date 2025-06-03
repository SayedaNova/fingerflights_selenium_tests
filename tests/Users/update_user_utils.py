import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.Module_Data.update_user_data import generate_updated_user

def update_user(driver, original_user):
    updated_user = generate_updated_user(original_user)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
    time.sleep(3)

    # Find the row containing the original user by original email
    rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'hover:shadow-md')]")
    for row in rows:
        if original_user["email"] in row.text:
            edit_button = row.find_element(By.XPATH, ".//a[contains(@href, '/update/')]")
            edit_button.click()
            WebDriverWait(driver, 10).until(EC.url_contains("/user/update"))
            break
    else:
        raise Exception(f"❌ Could not find user with email: {original_user['email']}")

    # --- Update input fields ---
    name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
    name_field.clear()
    name_field.send_keys(updated_user["name"])

    email_field = driver.find_element(By.NAME, "email")
    email_field.clear()
    email_field.send_keys(updated_user["email"])

    phone_field = driver.find_element(By.NAME, "phone")
    phone_field.clear()
    phone_field.send_keys(updated_user["phone"])

    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys(updated_user["password"])

    password_confirmation_field = driver.find_element(By.NAME, "password_confirmation")
    password_confirmation_field.clear()
    password_confirmation_field.send_keys(updated_user["confirm_password"])

    # --- ROLE ---
    current_role = driver.execute_script("""
        const select = document.querySelector('select[aria-hidden="true"]');
        return select ? select.value : null;
    """)

    role_mapping = {
        "Admin": "admin",
        "Manager": "manager",
        "Travel Consultant": "travel consultant",
        "Reservation Officer": "reservation officer",
        "Accountant": "accountant"
    }
    desired_role = role_mapping.get(updated_user["role"])
    if not desired_role:
        raise ValueError(f"❌ Unknown role '{updated_user['role']}' provided!")

    if current_role != desired_role:
        role_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']")))
        role_button.click()

        driver.execute_script("""
            const select = document.querySelector('select[aria-hidden="true"]');
            if (select) {
                select.value = arguments[0];
                select.dispatchEvent(new Event('change', { bubbles: true }));
            }
        """, desired_role)
        print(f"✅ Updated role to: {updated_user['role']}")
    else:
        print(f"ℹ️ Role already set to '{updated_user['role']}', no change made.")

    # --- GENDER ---
    current_gender = driver.execute_script("""
        const selected = document.querySelector("button[role='radio'][aria-checked='true']");
        return selected ? selected.value : null;
    """)
    desired_gender = updated_user["gender"].lower()
    if current_gender != desired_gender:
        gender_button = driver.find_element(By.XPATH, f"//button[@role='radio' and @value='{desired_gender}']")
        driver.execute_script("arguments[0].click();", gender_button)
        print(f"✅ Updated gender to: {updated_user['gender']}")
    else:
        print(f"ℹ️ Gender already set to '{updated_user['gender']}', no change made.")

    # --- STATUS ---
    current_status = driver.execute_script("""
        const selected = document.querySelectorAll("button[role='radio'][name='status']");
        for (let btn of selected) {
            if (btn.getAttribute('aria-checked') === 'true') return btn.value;
        }
        return null;
    """)
    desired_status = "1" if updated_user["status"].lower() == "active" else "0"
    if current_status != desired_status:
        status_button = driver.find_element(By.XPATH, f"//button[@role='radio' and @value='{desired_status}']")
        driver.execute_script("arguments[0].click();", status_button)
        print(f"✅ Updated status to: {updated_user['status']}")
    else:
        print(f"ℹ️ Status already set to '{updated_user['status']}', no change made.")

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

        WebDriverWait(driver, 10).until(EC.url_contains("/user/list"))
        print(f"✅ Updated user to: {updated_user['name']}")
        print("✅ Redirected to User List after submission.")
        print(updated_user)
    except Exception as e:
        print(f"❌ Could not submit form or redirect failed: {e}")

    return updated_user
