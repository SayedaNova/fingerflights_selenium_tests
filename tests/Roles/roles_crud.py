# user_crud.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.Demo_Data.create_role_data import roles_to_create, roles_to_update, generate_fake_roles
from tests.Roles.delete_role_utils import delete_role
from tests.Roles.create_role_utils import fill_and_submit_role_form
from tests.Roles.update_role_utils import update_role

# ✅ Define these at the top-level so other modules (like main.py) can import them
email = "trendssaas24@gmail.com"
password = "password"

def navigate_to_create_role_page(email=None, password=None, driver=None):
    if driver is None:
        raise ValueError("Driver must be passed to navigate_to_create_role_page")

    wait = WebDriverWait(driver, 15)

    # Click on B2B in sidebar
    role_menu_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='Role']/ancestor::a")
    ))
    role_menu_button.click()

    # Click on Create B2B user
    create_role_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@href='/roles/create']//li")
    ))
    create_role_link.click()

    # Wait until B2B Create form is fully loaded
    wait.until(EC.url_contains("/roles/create"))
    wait.until(EC.visibility_of_element_located((
        By.XPATH, "//input[@placeholder='Role name']"
    )))

    print("✅ Fully loaded Create Role page.")
    return driver

def create_roles(driver):
    for idx, role in enumerate(roles_to_create):
        #add fake data for role
        fill_and_submit_role_form(driver, role)
        print(role)

        # After form submission, wait for redirection to user list
        WebDriverWait(driver, 10).until(EC.url_contains("/roles/list"))
        time.sleep(5)

        # If there are more users to create, go back to /user/create
        if idx < len(roles_to_create) - 1:
            driver.get("http://178.128.114.165:73/roles/create")
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((
                By.XPATH, "//input[@placeholder='Role name']"
            )))


def update_roles(driver):
    for idx, role in enumerate(roles_to_update):
        #add fake data for role
        update_role(driver, role)
        print(role)

        # After form submission, wait for redirection to user list
        WebDriverWait(driver, 10).until(EC.url_contains("/roles/list"))
        time.sleep(5)

        if idx < len(roles_to_update) - 1:
            driver.get("http://178.128.114.165:73/roles/update")
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((
                By.XPATH, "//input[@placeholder='Role name']"
            )))

            # --- Update
        # update_role(driver, role)
        # time.sleep(2)
        # print(f"✅ Updated role: {role['role_name']}")

        #     # --- Delete
        # delete_role(driver, role)
        # time.sleep(2)
        # print(f"✅ Deleted role: {role['role_name']}")