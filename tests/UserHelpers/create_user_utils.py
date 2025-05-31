# tests/UserHelpers/create_user_utils.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fill_and_submit_user_form(driver, user_info_data):
    wait = WebDriverWait(driver, 10)

    # Fill in basic fields
    driver.find_element(By.NAME, "name").send_keys(user_info_data["name"])
    driver.find_element(By.NAME, "phone").send_keys(user_info_data["phone"])
    driver.find_element(By.NAME, "email").send_keys(user_info_data["email"])
    driver.find_element(By.NAME, "password").send_keys(user_info_data["password"])
    driver.find_element(By.NAME, "password_confirmation").send_keys(user_info_data["confirm_password"])

    # Select dropdowns
    # 👉 Select custom role dropdown (click button, then select text)
    role_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//button[@role='combobox' and contains(@class, 'rounded-md')]"
    )))
    role_button.click()

    # --- ✅ Set the role using JS on the hidden <select>
    role_mapping = {
        "Admin": "admin",
        "Manager": "manager",
        "Travel Consultant": "travel consultant",
        "Reservation Officer": "reservation officer",
        "Accountant": "accountant"
    }

    role_value = role_mapping.get(user_info_data["role"])
    if not role_value:
        raise ValueError(f"❌ Unknown role '{user_info_data['role']}' provided!")

    select_script = """
           const select = document.querySelector('select[aria-hidden="true"]');
           if (select) {
               select.value = arguments[0];
               select.dispatchEvent(new Event('change', { bubbles: true }));
           }
       """
    driver.execute_script(select_script, role_value)
    print(f"✅ Set role to: {user_info_data['role']} (value='{role_value}')")

    # --- Select gender via JavaScript (bypass overlay issues)
    gender_value = user_info_data["gender"].lower()
    gender_button = driver.find_element(By.XPATH, f"//button[@role='radio' and @value='{gender_value}']")
    driver.execute_script("arguments[0].click();", gender_button)
    print(f"✅ Gender set to: {user_info_data['gender']}")

    # --- Select status via JavaScript
    status_value = "1" if user_info_data["status"].lower() == "active" else "0"
    status_button = driver.find_element(By.XPATH, f"//button[@role='radio' and @value='{status_value}']")
    driver.execute_script("arguments[0].click();", status_button)
    print(f"✅ Status set to: {user_info_data['status']}")

    # Fill permissions (assuming checkboxes with name
    # s like Dashboard_Create, Dashboard_Read, etc.)
    # for module, actions in user_info_data.get("permissions", {}).items():
    #     for action, enabled in actions.items():
    #         checkbox_name = f"{module}_{action}"
    #         try:
    #             checkbox = driver.find_element(By.NAME, checkbox_name)
    #             if checkbox.is_selected() != enabled:
    #                 checkbox.click()
    #         except:
    #             print(f"⚠️ Checkbox {checkbox_name} not found or not interactable.")

    # --- Toggle permission section open (if collapsed)
    # try:
    #     toggle_button = wait.until(EC.element_to_be_clickable(
    #         (By.CSS_SELECTOR, "div.flex.justify-between.items-center.py-2.bg-slate-100.px-2.rounded > button")))
    #     driver.execute_script("arguments[0].click();", toggle_button)
    #     time.sleep(1)
    #     print("✅ Permissions section expanded.")
    # except Exception as e:
    #     print(f"⚠️ Could not expand permissions section: {e}")
    #
    #     # --- Set permissions
    # for module, actions in user_info_data.get("permissions", {}).items():
    #     for action, should_check in actions.items():
    #         if should_check:
    #             try:
    #                 checkbox = driver.find_element(By.XPATH,
    #                                                f"//input[@type='checkbox' and contains(@value, '{module}.{action}')]")
    #                 if not checkbox.is_selected():
    #                     driver.execute_script("arguments[0].click();", checkbox)
    #                 print(f"✅ Permission: {module}.{action}")
    #             except Exception as e:
    #                 print(f"⚠️ Could not set permission {module}.{action}: {e}")

        # --- Submit form


    try:
        # Try all common variations of submit buttons
        submit_button = wait.until(EC.presence_of_element_located((
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
        wait.until(EC.url_contains("/user/list"))
        print("✅ Redirected to User List after submission.")

    except Exception as e:
        print(f"❌ Could not submit form or redirect failed: {e}")



