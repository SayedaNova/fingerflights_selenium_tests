# user_crud.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.Leads.delete_lead_utils import delete_lead
from tests.Leads.create_lead_utils import fill_and_submit_lead_form
from tests.Module_Data.lead_data import leads_to_create
from tests.Leads.update_lead_utils import update_lead

# ✅ Define these at the top-level so other modules (like main.py) can import them
email = "trendssaas24@gmail.com"
password = "password"

def navigate_to_lead_page(email=None, password=None, driver=None):
    if driver is None:
        raise ValueError("Driver must be passed to navigate_to_lead_page")

    wait = WebDriverWait(driver, 15)

    # Click on Leads in sidebar
    lead_menu_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='Leads']/ancestor::a")
    ))
    lead_menu_button.click()

    # Click on New Lead
    new_lead_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@href='/lead/create']//li")
    ))
    new_lead_link.click()

    # Wait until Lead Create form is fully loaded
    wait.until(EC.url_contains("/lead/create"))
    wait.until(EC.visibility_of_element_located((By.NAME, "name")))

    print("✅ Fully loaded New Lead page.")
    return driver

def create_lead(driver):
    for idx, lead in enumerate(leads_to_create):
        fill_and_submit_lead_form(driver, lead)
        print(idx, lead)

        # After form submission, wait for redirection to user list
        WebDriverWait(driver, 10).until(EC.url_contains("/lead/list"))
        time.sleep(5)

        # If there are more users to create, go back to /user/create
        if idx < len(leads_to_create) - 1:
            driver.get("http://178.128.114.165:73/lead/create")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))

        update_lead(driver, lead)
        time.sleep(2)

        delete_lead(driver, lead)
        time.sleep(2)

# # You can keep this optional block for direct testing
# if __name__ == "__main__":
#     navigate_to_create_user_page(email, password)
