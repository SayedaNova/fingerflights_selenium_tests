import json
import time
from datetime import datetime

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def update_lead(driver, lead_data):

    my_lead_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@href='/lead/mylist']//li")
    ))
    my_lead_link.click()


    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "table")))

    time.sleep(3)

    # Find the row containing the user by email
    rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'hover:shadow-md')]")
    for row in rows:
        if lead_data["name"] in row.text:
            edit_button = row.find_element(By.XPATH, ".//a[contains(@href, '/update/')]")
            edit_button.click()
            WebDriverWait(driver, 10).until(EC.url_contains("/lead/update"))
            break
    else:
        raise Exception(f"❌ Could not find lead with name: {lead_data["name"]}")

    # --- ✅ Update Name, Phone, Email
    name_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "name")))
    name_input.clear()
    name_input.send_keys(lead_data["name"])

    phone_input = driver.find_element(By.NAME, "phone")
    phone_input.clear()
    phone_input.send_keys(lead_data["phone"])

    email_input = driver.find_element(By.NAME, "email")
    email_input.clear()
    email_input.send_keys(lead_data["email"])

    # --- ✅ Update Star rating
    stars = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.flex.gap-2.text-yellow-500 svg')))
    stars[lead_data["potentiality"] - 1].click()

    # --- ✅ Update Address
    address_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "address")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", address_field)
    time.sleep(1)
    address_field.clear()
    address_field.send_keys(lead_data["address"])

    # --- ✅ Update Description
    description_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((
        By.CSS_SELECTOR, 'textarea[placeholder="Type ..."][name="description"]'
    )))
    description_input.clear()
    description_input.send_keys(lead_data["description"])

    # --- ✅ Update Closing Date
    # label = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
    #     (By.XPATH, "//label[text()='Possible Closing Date']")
    # ))
    # container = label.find_element(By.XPATH, "./ancestor::div[contains(@class, 'space-y-2')]")
    # date_button = container.find_element(By.XPATH, ".//button")
    # date_button.click()
    #
    # calendar_popup = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "react-calendar")))
    #
    # closing_date = datetime.strptime(lead_data["closing_date"], '%B %d, %Y')
    # day = closing_date.day
    # month = closing_date.strftime('%B')
    # year = closing_date.year
    #
    # while True:
    #     current_month_year = calendar_popup.find_element(
    #         By.CLASS_NAME, "react-calendar__navigation__label"
    #     ).text
    #
    #     current_date = datetime.strptime(current_month_year + " 1", "%B %Y %d")
    #     target_date = datetime.strptime(f"{month} {year} 1", "%B %Y %d")
    #
    #     if current_date < target_date:
    #         calendar_popup.find_element(By.CLASS_NAME, "react-calendar__navigation__next-button").click()
    #     elif current_date > target_date:
    #         calendar_popup.find_element(By.CLASS_NAME, "react-calendar__navigation__prev-button").click()
    #     else:
    #         break
    #
    # for button in calendar_popup.find_elements(By.CLASS_NAME, "react-calendar__month-view__days__day"):
    #     if button.text == str(day) and "--neighboringMonth" not in button.get_attribute("class"):
    #         button.click()
    #         break

    # --- ✅ Update Closing Date (with safe parsing)
    label = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, "//label[text()='Possible Closing Date']"))
    )
    container = label.find_element(By.XPATH, "./ancestor::div[contains(@class, 'space-y-2')]")
    date_button = container.find_element(By.XPATH, ".//button")
    date_button.click()

    calendar_popup = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.CLASS_NAME, "react-calendar"))
    )

    # Parse target closing date from data
    closing_date = datetime.strptime(lead_data["closing_date"], '%B %d, %Y')
    target_day = closing_date.day
    target_month = closing_date.strftime('%B')
    target_year = closing_date.year

    # Navigate to the correct month and year
    while True:
        current_month_year = calendar_popup.find_element(
            By.CLASS_NAME, "react-calendar__navigation__label"
        ).text.strip()

        print(f"📆 Current calendar label: '{current_month_year}'")  # Debug info

        if not current_month_year:
            raise ValueError("❌ Calendar label is empty — cannot navigate date picker.")

        try:
            current_date = datetime.strptime(current_month_year + " 1", "%B %Y %d")
            target_date = datetime.strptime(f"{target_month} {target_year} 1", "%B %Y %d")
        except ValueError as e:
            raise ValueError(f"❌ Could not parse calendar label '{current_month_year}': {e}")

        if current_date < target_date:
            calendar_popup.find_element(By.CLASS_NAME, "react-calendar__navigation__next-button").click()
        elif current_date > target_date:
            calendar_popup.find_element(By.CLASS_NAME, "react-calendar__navigation__prev-button").click()
        else:
            break

    # Select the correct day
    day_buttons = calendar_popup.find_elements(By.CLASS_NAME, "react-calendar__month-view__days__day")
    for button in day_buttons:
        if button.text.strip() == str(target_day) and "--neighboringMonth" not in button.get_attribute("class"):
            button.click()
            print(f"✅ Selected closing date: {lead_data['closing_date']}")
            break
    else:
        print(f"⚠️ Could not find day {target_day} in calendar.")

    # --- ✅ Submit the updated form
    try:
        submit_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, "//button[@type='submit' and contains(text(), 'Submit')]"
        )))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", submit_button)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", submit_button)
        WebDriverWait(driver, 20).until(EC.url_contains("/lead/list"))
        print("✅ Lead updated successfully and redirected to list.")
        # print(json.dumps(lead_data, indent=2))
    except Exception as e:
        print(f"❌ Could not update lead: {e}")