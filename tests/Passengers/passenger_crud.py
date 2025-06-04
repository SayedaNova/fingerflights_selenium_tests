# user_crud.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.Demo_Data.create_passenger_data import passengers_to_create
from tests.Passengers.create_passenger_utils import fill_and_submit_passenger_form
from tests.Passengers.delete_passenger_utils import delete_passenger
from tests.Passengers.update_passenger_utils import update_passenger

# ✅ Define these at the top-level so other modules (like main.py) can import them
email = "trendssaas24@gmail.com"
password = "password"

def navigate_to_passenger_page(email=None, password=None, driver=None):
    if driver is None:
        raise ValueError("Driver must be passed to navigate_to_passenger_page")

    wait = WebDriverWait(driver, 15)

    # Click on Leads in sidebar
    passenger_menu_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='Passenger']/ancestor::a")
    ))
    passenger_menu_button.click()

    # Click on New Lead
    new_passenger_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@href='/passenger/create']//li")
    ))
    new_passenger_link.click()

    # Wait until Lead Create form is fully loaded
    wait.until(EC.url_contains("/passenger/create"))
    wait.until(EC.visibility_of_element_located((By.NAME, "first_name")))

    print("✅ Fully loaded New Passenger page.")
    return driver

def create_passenger(driver):
    for idx, passenger in enumerate(passengers_to_create):
        fill_and_submit_passenger_form(driver, passenger)
        print(idx, passenger)

        WebDriverWait(driver, 10).until(EC.url_contains("/passenger/list"))
        time.sleep(3)

        updated_passenger = update_passenger(driver, passenger)
        time.sleep(3)
        delete_passenger(driver, updated_passenger)
        time.sleep(3)

        if idx < len(passengers_to_create) - 1:
            driver.get("http://178.128.114.165:73/passenger/create")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "first_name")))
            print("➡️ Ready for next passenger creation\n")
            time.sleep(3)
# # You can keep this optional block for direct testing
# if __name__ == "__main__":
#     navigate_to_create_user_page(email, password)