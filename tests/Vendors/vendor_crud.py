# user_crud.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.Demo_Data.create_vendor_data import vendors_to_create
from tests.Vendors.create_vendor_utils import fill_and_submit_vendor_form
from tests.Vendors.update_vendor_utils import update_vendor

# ✅ Define these at the top-level so other modules (like main.py) can import them
email = "trendssaas24@gmail.com"
password = "password"

def navigate_to_vendor_page(email=None, password=None, driver=None):
    if driver is None:
        raise ValueError("Driver must be passed to navigate_to_vendor_page")

    wait = WebDriverWait(driver, 15)

    # Click on Leads in sidebar
    vendor_menu_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='Vendor']/ancestor::a")
    ))
    vendor_menu_button.click()

    # Click on New Lead
    new_vendor_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@href='/vendor/create']//li")
    ))
    new_vendor_link.click()

    # Wait until Lead Create form is fully loaded
    wait.until(EC.url_contains("/vendor/create"))
    wait.until(EC.visibility_of_element_located((By.NAME, "name")))

    print("✅ Fully loaded New Vendor page.")
    return driver

def create_vendor(driver):
    for idx, vendor in enumerate(vendors_to_create):
        fill_and_submit_vendor_form(driver, vendor)
        print(idx, vendor)

        WebDriverWait(driver, 10).until(EC.url_contains("/vendor/list"))
        time.sleep(3)

        update_vendor(driver, vendor)
        time.sleep(3)

        if idx < len(vendors_to_create) - 1:
            driver.get("http://178.128.114.165:73/vendor/create")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
            print("➡️ Ready for next vendor creation\n")
            time.sleep(3)

# # You can keep this optional block for direct testing
# if __name__ == "__main__":
#     navigate_to_create_user_page(email, password)
