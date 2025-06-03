# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# def fill_and_submit_role_form(driver, role_data):
#     wait = WebDriverWait(driver, 10)
#
#     # Fill the role name
#     role_input = wait.until(EC.presence_of_element_located((
#         By.XPATH, "//input[@placeholder='Role name']"
#     )))
#     role_input.clear()
#     role_input.send_keys(role_data["role_name"])
#     print(role_input)
#
#     # Fill permissions
#     for permission in role_data["permissions"]:
#         perm_name = permission["name"].lower()  # Convert to lowercase to match HTML IDs
#
#         for action in ["create", "read", "update", "delete"]:
#             checkbox_id = f"{action}_{perm_name}"
#             try:
#                 checkbox = wait.until(EC.presence_of_element_located((By.ID, checkbox_id)))
#
#                 # Scroll into view before clicking
#                 driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", checkbox)
#                 time.sleep(0.2)
#
#                 # Check if already selected
#                 aria_checked = checkbox.get_attribute("aria-checked")
#                 if aria_checked != "true":
#                     checkbox.click()
#                     print(f"✅ Clicked {action} for {perm_name}")
#             except Exception as e:
#                 print(f"❌ Error locating or clicking {action} for {perm_name}: {e}")
#                 # Try alternative XPath if ID fails
#                 try:
#                     xpath = f"//button[@role='checkbox' and contains(@id, '{action}_{perm_name}')]"
#                     checkbox = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
#
#                     driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", checkbox)
#                     time.sleep(0.2)
#
#                     if checkbox.get_attribute("aria-checked") != "true":
#                         checkbox.click()
#                         print(f"✅ Clicked {action} for {perm_name} (via XPath)")
#                 except Exception as e2:
#                     print(f"❌ Still couldn't locate {action} for {perm_name}: {e2}")
#
#     # Submit form
#     try:
#         # First scroll to bottom of page to ensure footer/submit button area is visible
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(0.5)
#
#         submit_button = wait.until(EC.presence_of_element_located((
#             By.XPATH, "//button[contains(@class, 'bg-ffblue') and normalize-space(text())='Submit']"
#         )))
#
#         wait.until(EC.element_to_be_clickable(submit_button))
#
#         submit_button.click()
#         print("✅ Form submitted via direct click")
#
#         wait.until(EC.url_contains("/roles/list"))
#         print("✅ Redirected to Role List after submission.")
#
#     except Exception as e:
#         print(f"❌ Could not submit form or redirect failed: {e}")

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fill_and_submit_role_form(driver, role_data):
    wait = WebDriverWait(driver, 10)

    # Fill the role name
    role_input = wait.until(EC.presence_of_element_located((
        By.XPATH, "//input[@placeholder='Role name']"
    )))
    role_input.clear()
    role_input.send_keys(role_data["role_name"])
    print(f"Role name input filled with: {role_data['role_name']}")

    # For create role, we only process Dashboard permission
    for permission in role_data["permissions"]:
        if permission["name"] != "Dashboard":
            continue

        perm_name = permission["name"].lower()

        # Only handle read permission for Dashboard
        checkbox_id = f"read_{perm_name}"
        try:
            checkbox = wait.until(EC.presence_of_element_located((By.ID, checkbox_id)))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", checkbox)
            time.sleep(0.2)

            aria_checked = checkbox.get_attribute("aria-checked")
            if aria_checked != "true":
                checkbox.click()
                print(f"✅ Clicked read for {perm_name}")
        except Exception as e:
            print(f"❌ Error locating or clicking read for {perm_name}: {e}")

    # Submit form
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)

        submit_button = wait.until(EC.presence_of_element_located((
            By.XPATH, "//button[contains(@class, 'bg-ffblue') and normalize-space(text())='Submit']"
        )))

        wait.until(EC.element_to_be_clickable(submit_button))
        submit_button.click()
        print("✅ Form submitted via direct click")

        wait.until(EC.url_contains("/roles/list"))
        print("✅ Redirected to Role List after submission.")

    except Exception as e:
        print(f"❌ Could not submit form or redirect failed: {e}")