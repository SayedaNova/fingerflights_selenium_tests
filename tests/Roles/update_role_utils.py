# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from tests.Module_Data import role_data
#
#
# def update_role(driver, role):
#     wait = WebDriverWait(driver, 10)
#
#     # Wait for roles table to load
#     wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
#     time.sleep(2)  # small delay to ensure full rendering
#
#     # Find the row containing the role by name
#     rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'hover:shadow-md')]")
#     role_name_lower = role["role_name"].strip().lower()
#     for row in rows:
#         row_text = row.text.strip().lower()
#         if role_name_lower in row_text:
#             edit_button = row.find_element(By.XPATH, ".//a[contains(@href, '/update/')]")
#             edit_button.click()
#             wait.until(EC.url_contains("/roles/update"))
#             print(f"Navigated to update page for role: {role['role_name']}")
#             break
#     else:
#         raise Exception(f"❌ Could not find role with name: {role['role_name']}")
#
#     # Fill and submit the update form
#     role_input = wait.until(EC.presence_of_element_located((
#             By.XPATH, "//input[@placeholder='Role name']"
#         )))
#     role_input.clear()
#     role_input.send_keys(role["role_name"])
#     print(f"Role name input filled with: {role['role_name']}")
#
#     try:
#         # Scroll to bottom of page to ensure submit button is visible
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
#         print("✅ Form submitted successfully")
#
#         wait.until(EC.url_contains("/roles/list"))
#         print("✅ Redirected to Role List after submission.")
#
#     except Exception as e:
#         print(f"❌ Could not submit form or redirect failed: {e}")
#
#
#
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# def update_role(driver, role):
#     wait = WebDriverWait(driver, 10)
#
#     # Wait for roles table to load
#     wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
#     time.sleep(2)  # small delay to ensure full rendering
#
#     # Find the row containing the role by name
#     rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'hover:shadow-md')]")
#     role_name_lower = role["role_name"].strip().lower()
#     for row in rows:
#         row_text = row.text.strip().lower()
#         if role_name_lower in row_text:
#             edit_button = row.find_element(By.XPATH, ".//a[contains(@href, '/update/')]")
#             edit_button.click()
#             wait.until(EC.url_contains("/roles/update"))
#             print(f"Navigated to update page for role: {role['role_name']}")
#             break
#     else:
#         raise Exception(f"❌ Could not find role with name: {role['role_name']}")
#
#     # Fill permissions - now we can add all permissions
#     for permission in role["permissions"]:
#         perm_name = permission["name"].lower()
#
#         for action in ["create", "read", "update", "delete"]:
#             if not permission.get(action, False):
#                 continue
#
#             checkbox_id = f"{action}_{perm_name}"
#             try:
#                 checkbox = wait.until(EC.presence_of_element_located((By.ID, checkbox_id)))
#                 driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", checkbox)
#                 time.sleep(0.2)
#
#                 aria_checked = checkbox.get_attribute("aria-checked")
#                 if aria_checked != "true":
#                     checkbox.click()
#                     print(f"✅ Clicked {action} for {perm_name}")
#             except Exception as e:
#                 print(f"❌ Error locating or clicking {action} for {perm_name}: {e}")
#
#     # Submit form
#     try:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(0.5)
#
#         submit_button = wait.until(EC.presence_of_element_located((
#             By.XPATH, "//button[contains(@class, 'bg-ffblue') and normalize-space(text())='Submit']"
#         )))
#
#         wait.until(EC.element_to_be_clickable(submit_button))
#         submit_button.click()
#         print("✅ Form submitted successfully")
#
#         wait.until(EC.url_contains("/roles/list"))
#         print("✅ Redirected to Role List after submission.")
#
#     except Exception as e:
#         print(f"❌ Could not submit form or redirect failed: {e}")


# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# def update_role(driver, role):
#     wait = WebDriverWait(driver, 10)
#
#     # Wait for roles table to load
#     wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
#     time.sleep(2)  # small delay to ensure full rendering
#
#     # Find the row containing the role by name
#     rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'hover:shadow-md')]")
#     role_name_lower = role["role_name"].strip().lower()
#     for row in rows:
#         row_text = row.text.strip().lower()
#         if role_name_lower in row_text:
#             edit_button = row.find_element(By.XPATH, ".//a[contains(@href, '/update/')]")
#             edit_button.click()
#             wait.until(EC.url_contains("/roles/update"))
#             print(f"Navigated to update page for role: {role['role_name']}")
#             break
#     else:
#         raise Exception(f"❌ Could not find role with name: {role['role_name']}")
#
#     # Fill permissions - skip Dashboard since it's already set
#     for permission in role["permissions"]:
#         if permission["name"] == "Dashboard":
#             continue  # Skip Dashboard permissions during update
#
#         perm_name = permission["name"].lower()
#
#         for action in ["create", "read", "update", "delete"]:
#             if not permission.get(action, False):
#                 continue
#
#             checkbox_id = f"{action}_{perm_name}"
#             try:
#                 checkbox = wait.until(EC.presence_of_element_located((By.ID, checkbox_id)))
#                 driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", checkbox)
#                 time.sleep(0.2)
#
#                 aria_checked = checkbox.get_attribute("aria-checked")
#                 if aria_checked != "true":
#                     checkbox.click()
#                     print(f"✅ Clicked {action} for {perm_name}")
#             except Exception as e:
#                 print(f"❌ Error locating or clicking {action} for {perm_name}: {e}")
#
#     # Submit form
#     try:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(0.5)
#
#         submit_button = wait.until(EC.presence_of_element_located((
#             By.XPATH, "//button[contains(@class, 'bg-ffblue') and normalize-space(text())='Submit']"
#         )))
#
#         wait.until(EC.element_to_be_clickable(submit_button))
#         submit_button.click()
#         print("✅ Form submitted successfully")
#
#         wait.until(EC.url_contains("/roles/list"))
#         print("✅ Redirected to Role List after submission.")
#
#     except Exception as e:
#         print(f"❌ Could not submit form or redirect failed: {e}")

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# def update_role(driver, role):
#     wait = WebDriverWait(driver, 15)  # Increased timeout
#
#     # Wait for roles table to load
#     wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
#     time.sleep(2)
#
#     # Find the role row
#     role_name_lower = role["role_name"].strip().lower()
#     rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'hover:shadow-md')]")
#     for row in rows:
#         if role_name_lower in row.text.strip().lower():
#             edit_button = row.find_element(By.XPATH, ".//a[contains(@href, '/update/')]")
#             edit_button.click()
#             break
#     else:
#         raise Exception(f"❌ Could not find role with name: {role['role_name']}")
#
#     # Wait for update page to load
#     wait.until(EC.url_contains("/roles/update"))
#     print(f"Navigated to update page for role: {role['role_name']}")
#
#     # Handle permissions - skip Dashboard
#     for permission in role["permissions"]:
#         if permission["name"] == "Dashboard":
#             continue
#
#         perm_name = permission["name"].lower()
#         print(f"Processing permissions for: {perm_name}")
#
#         for action in ["create", "read", "update", "delete"]:
#             if not permission.get(action, False):
#                 continue
#
#             # Try multiple locator strategies
#             locators = [
#                 (By.ID, f"{action}_{perm_name}"),
#                 (By.XPATH, f"//input[@id='{action}_{perm_name}']"),
#                 (By.XPATH, f"//label[contains(., '{action}')]/input[@type='checkbox']"),
#                 (By.CSS_SELECTOR, f"input[id*='{action}_{perm_name}']")
#             ]
#
#             clicked = False
#             for locator in locators:
#                 try:
#                     checkbox = wait.until(EC.presence_of_element_located(locator))
#                     driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
#                     time.sleep(0.3)
#
#                     # Ensure element is clickable
#                     wait.until(EC.element_to_be_clickable(checkbox))
#
#                     # Check if needs to be checked
#                     if not checkbox.is_selected():
#                         driver.execute_script("arguments[0].click();", checkbox)
#                         print(f"✅ Checked {action} for {perm_name} using {locator[0]}")
#                         clicked = True
#                         break
#                 except Exception as e:
#                     print(f"⚠️ Failed with locator {locator[0]}: {str(e)[:100]}...")
#                     continue
#
#             if not clicked:
#                 print(f"❌ Could not check {action} for {perm_name} after trying all locators")
#
#     # Submit form
#     try:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(0.5)
#
#         submit_button = wait.until(EC.element_to_be_clickable(
#             (By.XPATH, "//button[contains(@class, 'bg-ffblue') and normalize-space(text())='Submit']")
#         ))
#         submit_button.click()
#         print("✅ Form submitted successfully")
#
#         wait.until(EC.url_contains("/roles/list"))
#         print("✅ Redirected to Role List after submission.")
#     except Exception as e:
#         print(f"❌ Could not submit form or redirect failed: {e}")

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# def update_role(driver, role):
#     wait = WebDriverWait(driver, 15)
#
#     # Wait for roles table to load
#     wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
#     time.sleep(2)
#
#     # Find the role row
#     role_name_lower = role["role_name"].strip().lower()
#     rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'hover:shadow-md')]")
#     for row in rows:
#         if role_name_lower in row.text.strip().lower():
#             edit_button = row.find_element(By.XPATH, ".//a[contains(@href, '/update/')]")
#             edit_button.click()
#             break
#     else:
#         raise Exception(f"❌ Could not find role with name: {role['role_name']}")
#
#     # Wait for update page to load
#     wait.until(EC.url_contains("/roles/update"))
#     print(f"Navigated to update page for role: {role['role_name']}")
#
#     # Handle permissions - skip Dashboard
#     for permission in role["permissions"]:
#         if permission["name"] == "Dashboard":
#             continue
#
#         perm_name = permission["name"].lower().replace('_', '-')  # Convert to HTML-friendly format
#         print(f"Processing permissions for: {perm_name}")
#
#         for action in ["create", "read", "update", "delete"]:
#             if not permission.get(action, False):
#                 continue
#
#             # Build the button ID pattern we see in the HTML
#             button_id = f"permission-{perm_name}-{action}"
#
#             try:
#                 # First try to find by exact ID
#                 checkbox = wait.until(EC.presence_of_element_located(
#                     (By.XPATH,
#                      f"//button[@role='checkbox' and contains(@id, '{action}') and contains(@id, '{perm_name}')]")
#                 ))
#
#                 # Scroll into view
#                 driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
#                 time.sleep(0.3)
#
#                 # Check current state
#                 current_state = checkbox.get_attribute("data-state")
#                 if current_state == "unchecked":
#                     # Click the button to check it
#                     checkbox.click()
#                     print(f"✅ Checked {action} for {perm_name}")
#                     time.sleep(0.2)  # Small delay for UI to update
#
#                     # Verify it's now checked
#                     updated_state = checkbox.get_attribute("data-state")
#                     if updated_state != "checked":
#                         print(f"⚠️ Failed to verify {action} for {perm_name} is checked")
#             except Exception as e:
#                 print(f"❌ Error handling {action} for {perm_name}: {str(e)[:100]}...")
#
#     # Submit form
#     try:
#         submit_button = wait.until(EC.element_to_be_clickable(
#             (By.XPATH, "//button[contains(@class, 'bg-ffblue') and contains(text(), 'Submit')]")
#         ))
#         driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
#         time.sleep(0.5)
#         submit_button.click()
#         print("✅ Form submitted successfully")
#
#         wait.until(EC.url_contains("/roles/list"))
#         print("✅ Redirected to Role List after submission.")
#     except Exception as e:
#         print(f"❌ Could not submit form or redirect failed: {e}")



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def update_role(driver, role):
    wait = WebDriverWait(driver, 15)

    # Wait for roles table to load
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
    time.sleep(2)

    # Find the role row
    role_name_lower = role["role_name"].strip().lower()
    rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'hover:shadow-md')]")
    for row in rows:
        if role_name_lower in row.text.strip().lower():
            edit_button = row.find_element(By.XPATH, ".//a[contains(@href, '/update/')]")
            edit_button.click()
            break
    else:
        raise Exception(f"❌ Could not find role with name: {role['role_name']}")

    # Wait for update page to load
    wait.until(EC.url_contains("/roles/update"))
    print(f"Navigated to update page for role: {role['role_name']}")

    # Handle permissions - skip Dashboard
    for permission in role["permissions"]:
        if permission["name"].lower() == "dashboard":
            continue

        perm_name = permission["name"].lower().replace('_', '-')  # Normalize ID format
        print(f"Processing permissions for: {perm_name}")

        for action in ["create", "read", "update", "delete"]:
            if not permission.get(action, False):
                continue

            try:
                # Construct ID
                button_xpath = f"//button[@role='checkbox' and contains(@id, '{action}') and contains(@id, '{perm_name}')]"

                # Wait until clickable
                checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

                # Scroll into view
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
                time.sleep(0.2)

                # Confirm visibility
                wait.until(EC.visibility_of(checkbox))

                # Check current state
                current_state = checkbox.get_attribute("data-state")
                if current_state == "unchecked":
                    try:
                        checkbox.click()
                    except:
                        # Fallback using ActionChains
                        ActionChains(driver).move_to_element(checkbox).click().perform()

                    print(f"✅ Checked {action} for {perm_name}")
                    time.sleep(0.2)

                    # Verify updated state
                    updated_state = checkbox.get_attribute("data-state")
                    if updated_state != "checked":
                        print(f"⚠️ Failed to verify {action} for {perm_name} is checked")

            except Exception as e:
                print(f"❌ Error handling {action} for {perm_name}: {str(e)[:200]}...")

    # Submit form
    try:
        submit_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@class, 'bg-ffblue') and contains(text(), 'Submit')]")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
        time.sleep(0.5)
        submit_button.click()
        print("✅ Form submitted successfully")

        wait.until(EC.url_contains("/roles/list"))
        print("✅ Redirected to Role List after submission.")
    except Exception as e:
        print(f"❌ Could not submit form or redirect failed: {e}")
