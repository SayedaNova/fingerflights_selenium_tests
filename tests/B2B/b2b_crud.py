# user_crud.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.B2B.create_b2b_utils import fill_and_submit_b2b_form
from tests.B2B.delete_b2b_utils import delete_b2b
from tests.B2B.update_b2b_utils import update_b2b
from tests.Demo_Data.create_b2b_data import b2b_to_create

# ✅ Define these at the top-level so other modules (like main.py) can import them
email = "trendssaas24@gmail.com"
password = "password"

def navigate_to_b2b_user_page(email=None, password=None, driver=None):
    if driver is None:
        raise ValueError("Driver must be passed to navigate_to_b2b_user_page")

    wait = WebDriverWait(driver, 15)

    # Click on B2B in sidebar
    user_menu_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='B2B']/ancestor::a")
    ))
    user_menu_button.click()

    # Click on Create B2B user
    create_user_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@href='/b2b/create']//li")
    ))
    create_user_link.click()

    # Wait until B2B Create form is fully loaded
    wait.until(EC.url_contains("/b2b/create"))
    wait.until(EC.visibility_of_element_located((By.NAME, "name")))

    print("✅ Fully loaded Create B2B User page.")
    return driver

def create_b2b_users(driver):
    # for idx, b2b in enumerate(b2b_to_create):
    #     fill_and_submit_b2b_form(driver, b2b)
    #     print(idx, b2b)
    #
    #     # After form submission, wait for redirection to user list
    #     WebDriverWait(driver, 10).until(EC.url_contains("/b2b/list"))
    #     time.sleep(5)
    #
    #     # If there are more users to create, go back to /user/create
    #     if idx < len(b2b_to_create) - 1:
    #         driver.get("http://178.128.114.165:73/b2b/create")
    #         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
    #
    #         # --- Update
    #     updated_b2b = update_b2b(driver, b2b)
    #     time.sleep(2)
    #     print(f"✅ Updated user: {b2b['email']}")
    #
    #         # --- Delete
    #     delete_b2b(driver, updated_b2b)
    #     time.sleep(2)
        # print(f"✅ Deleted user: {b2b['email']}")

    for idx, b2b in enumerate(b2b_to_create):
        # --- Create user
        fill_and_submit_b2b_form(driver, b2b)
        print(f"✅ Created b2b: {b2b['email']}")

        # Wait for redirection to user list after creation
        WebDriverWait(driver, 10).until(EC.url_contains("/b2b/list"))
        time.sleep(3)

        # --- Update user
        updated_b2b = update_b2b(driver, b2b)
        print(f"✅ Updated b2b: {updated_b2b['email']}")
        time.sleep(3)

        # --- Delete user
        delete_b2b(driver, updated_b2b)
        print(f"🗑️ Deleted b2b: {updated_b2b['email']}")
        time.sleep(3)

        # Now redirect to user create page again for next iteration (if more users)
        if idx < len(b2b_to_create) - 1:
            driver.get("http://178.128.114.165:73/b2b/create")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
            print("➡️ Ready for next b2b user creation\n")
            time.sleep(3)

# # You can keep this optional block for direct testing
# if __name__ == "__main__":
#     navigate_to_create_user_page(email, password)
