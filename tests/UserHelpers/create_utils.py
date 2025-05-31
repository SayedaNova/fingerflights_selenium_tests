# create_utils.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.AuthHelpers.login_utils import login_with_otp
from tests.UserHelpers.create_user_utils import fill_and_submit_user_form
from tests.Data.user_info_data import users_to_create

# # ✅ Define these at the top-level so other modules (like main.py) can import them
# email = "trendssaas24@gmail.com"
# password = "password"

def navigate_to_create_user_page(email, password):
    driver = login_with_otp(email, password)
    wait = WebDriverWait(driver, 15)

    user_menu_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='User']/ancestor::a")
    ))
    user_menu_button.click()

    create_user_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@href='/user/create']//li")
    ))
    create_user_link.click()

    wait.until(EC.url_contains("/user/create"))
    wait.until(EC.visibility_of_element_located((By.NAME, "name")))  # e.g. the Name input field

    print("✅ Fully loaded Create User page.")
    return driver

def create_users(driver):
    for idx, user in enumerate(users_to_create):
        #add fake data for user
        fill_and_submit_user_form(driver, user)
        print(user)

        # After form submission, wait for redirection to user list
        WebDriverWait(driver, 10).until(EC.url_contains("/user/list"))
        time.sleep(5)

        # If there are more users to create, go back to /user/create
        if idx < len(users_to_create) - 1:
            driver.get("http://178.128.114.165:73/user/create")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))

# # You can keep this optional block for direct testing
# if __name__ == "__main__":
#     navigate_to_create_user_page(email, password)
