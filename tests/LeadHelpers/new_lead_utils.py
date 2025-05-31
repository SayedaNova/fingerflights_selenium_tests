import time
from datetime import datetime

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

def fill_and_submit_lead_form(driver, lead_data):
    wait = WebDriverWait(driver, 20)

    driver.find_element(By.NAME, "name").send_keys(lead_data["name"])
    driver.find_element(By.NAME, "phone").send_keys(lead_data["phone"])
    driver.find_element(By.NAME, "email").send_keys(lead_data["email"])

    # Star rating (click N stars based on potentiality)
    stars = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.flex.gap-2.text-yellow-500 svg')))
    stars[lead_data["potentiality"] - 1].click()

    # --- ✅ Handle Source Dropdown
    source_mapping = {
        "Phone Call": "1",
        "Facebook": "2",
        "Reference": "3",
        "Repeat Customer": "4",
        "Walking": "5",
        "Friends & Family": "6",
        "B2B": "7",
        "Man Power": "8"
    }

    source_value = source_mapping.get(lead_data["source"])
    if not source_value:
        raise ValueError(f"❌ Unknown source '{lead_data['source']}' provided!")

    # Select the correct combobox button (e.g. first of multiple)
    source_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, "(//button[@role='combobox' and contains(@class, 'rounded-md')])[1]"
    )))
    source_button.click()

    # Set source via JS
    driver.execute_script("""
        const select = document.querySelectorAll('select[aria-hidden="true"]')[0];
        if (select) {
            select.value = arguments[0];
            select.dispatchEvent(new Event('change', { bubbles: true }));
        }
    """, source_value)

    print(f"✅ Set source to: {lead_data['source']} (value='{source_value}')")

    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.ESCAPE)
    time.sleep(2)

    # --- ✅ Handle Status Dropdown
    status_mapping = {
        "Lead": "4",
        "Ongoing": "5",
        "Negotiating": "6",
        "Booking Done": "9",
        "Wating For Final Confirmation": "10",
        "Won": "7",
        "Closed": "8"
    }

    status_value = status_mapping.get(lead_data["status"])
    if not status_value:
        raise ValueError(f"❌ Unknown status '{lead_data['status']}' provided!")

    # Get and click the status combobox
    status_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, "(//button[@role='combobox' and contains(@class, 'rounded-md')])[2]"
    )))

    # Scroll into view and click via JS to avoid overlay interception
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", status_button)
    time.sleep(3)  # Optional but helps with animations
    driver.execute_script("arguments[0].click();", status_button)

    # Set status using JS
    driver.execute_script("""
        const select = document.querySelectorAll('select[aria-hidden="true"]')[1];
        if (select) {
            select.value = arguments[0];
            select.dispatchEvent(new Event('change', { bubbles: true }));
        }
    """, status_value)

    print(f"✅ Set status to: {lead_data['status']} (value='{status_value}')")

    # try:
    #     time.sleep(1)
    #
    #     division_dropdown = wait.until(EC.element_to_be_clickable((
    #         By.XPATH, '//button[@role="combobox" and @type="button"]'
    #     )))
    #     division_dropdown.click()
    #
    #     # Wait for options to appear (adjust XPath if needed)
    #     wait.until(EC.presence_of_all_elements_located((By.XPATH, '//button[@role="option"]')))
    #
    #     options = driver.find_elements(By.XPATH, '//button[@role="option"]')
    #     print(f"Found {len(options)} dropdown options:")
    #     for opt in options:
    #         print(f"- '{opt.text}'")
    #
    #     division_text = lead_data["division"].strip()
    #     division_option = wait.until(EC.element_to_be_clickable((
    #         By.XPATH, f'//button[@role="option" and contains(text(), "{division_text}")]'
    #     )))
    #     division_option.click()
    #
    # except Exception as e:
    #     raise Exception(f"Failed to select division '{lead_data['division']}': {e}")
    #
    # # --- Select District (search + button)
    # district_input = wait.until(EC.element_to_be_clickable((
    #     By.CSS_SELECTOR, 'input[placeholder="Search District"]'
    # )))
    # district_input.clear()
    # district_input.send_keys(lead_data["district"])
    #
    # district_option = wait.until(EC.element_to_be_clickable((
    #     By.XPATH, f'//button[text()="{lead_data["district"]}"]'
    # )))
    # district_option.click()
    #
    # # --- Select Upazila (search + button)
    # upazila_input = wait.until(EC.element_to_be_clickable((
    #     By.CSS_SELECTOR, 'input[placeholder="Search Upazila"]'
    # )))
    # upazila_input.clear()
    # upazila_input.send_keys(lead_data["upazila"])
    #
    # upazila_option = wait.until(EC.element_to_be_clickable((
    #     By.XPATH, f'//button[text()="{lead_data["upazila"]}"]'
    # )))
    # upazila_option.click()

    # --- ✅ Close dropdown (ESCAPE or click elsewhere)
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.ESCAPE)
    time.sleep(2)

    # time.sleep(2)

    address_field = wait.until(EC.presence_of_element_located((By.ID, "address")))

    # Scroll to address field to ensure visibility
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", address_field)
    time.sleep(2)  # Optional pause for UI stability

    address_field.send_keys(lead_data["address"])

    # Repeat ESC to ensure dropdowns are closed
    body.send_keys(Keys.ESCAPE)
    time.sleep(1)

    description_input = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, 'textarea[placeholder="Type ..."][name="description"]'
    )))
    description_input.clear()
    description_input.send_keys(lead_data["description"])

    # Step 1: Get day from closing_date
    label = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//label[text()='Possible Closing Date']")
    ))
    # Step 2: Navigate up to the container and then down to the associated "Pick a date" button
    # This assumes the button is within the same parent div as the label
    container = label.find_element(By.XPATH, "./ancestor::div[contains(@class, 'space-y-2')]")
    date_button = container.find_element(By.XPATH, ".//button[.//span[text()='Pick a date']]")
    # Step 3: Click the date picker button
    date_button.click()

    # Wait for the calendar popup to appear
    calendar_popup = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "react-calendar")
    ))

    # Get the fake closing date from our generated data
    closing_date_str = lead_data["closing_date"]  # Format: "May 28, 2025"

    # Parse the date to get day, month, and year
    closing_date = datetime.strptime(closing_date_str, '%B %d, %Y')
    day = closing_date.day
    month = closing_date.strftime('%B')  # Full month name
    year = closing_date.year

    # First check if we need to navigate to a different month/year
    current_month_year = calendar_popup.find_element(
        By.CLASS_NAME, "react-calendar__navigation__label"
    ).text

    if f"{month} {year}" not in current_month_year:
        # Navigate to the correct month/year
        while True:
            current_month_year = calendar_popup.find_element(
                By.CLASS_NAME, "react-calendar__navigation__label"
            ).text

            current_date = datetime.strptime(current_month_year + " 1", "%B %Y %d")
            target_date = datetime.strptime(f"{month} {year} 1", "%B %Y %d")

            if current_date < target_date:
                # Click next button
                next_btn = calendar_popup.find_element(
                    By.CLASS_NAME, "react-calendar__navigation__next-button"
                )
                next_btn.click()
            elif current_date > target_date:
                # Click previous button
                prev_btn = calendar_popup.find_element(
                    By.CLASS_NAME, "react-calendar__navigation__prev-button"
                )
                prev_btn.click()
            else:
                break

    # Now select the day
    day_buttons = calendar_popup.find_elements(
        By.CLASS_NAME, "react-calendar__month-view__days__day"
    )

    for button in day_buttons:
        if button.text == str(
                day) and "react-calendar__month-view__days__day--neighboringMonth" not in button.get_attribute("class"):
            button.click()
            break

    try:
        submit_button = wait.until(EC.presence_of_element_located((
            By.XPATH, "//button[@type='submit' and contains(text(), 'Submit')]"
        )))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", submit_button)
        time.sleep(0.5)

        if submit_button.is_displayed() and submit_button.is_enabled():
            driver.execute_script("arguments[0].click();", submit_button)
            print("✅ Form submitted via JavaScript click.")
        else:
            print("⚠️ Submit button found but not interactable. Trying JS click directly.")
            driver.execute_script("arguments[0].click();", submit_button)

        wait.until(EC.url_contains("/lead/list"))
        print("✅ Redirected to Lead List after submission.")
    except Exception as e:
        print(f"❌ Could not submit form or redirect failed: {e}")
