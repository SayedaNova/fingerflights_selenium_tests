import time
from datetime import datetime

from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_date_button_by_label(wait, label_text):
    label = wait.until(EC.presence_of_element_located((By.XPATH, f"//label[contains(text(), '{label_text}')]")))
    # This assumes the button is the first sibling after the label
    button = label.find_element(By.XPATH, ".//following::button[contains(., 'Pick a date')]")
    wait.until(EC.element_to_be_clickable(button)).click()


def select_date_from_picker(wait, label_text, date_str):

    target_date = datetime.strptime(date_str, '%B %d, %Y')
    target_month_year = target_date.strftime("%B %Y")

    # Step 1: Navigate to correct month/year
    while True:
        calendar_popup = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "react-calendar")))

        # Re-fetch header each iteration
        header = calendar_popup.find_element(By.CLASS_NAME, "react-calendar__navigation__label")
        current_month_year_text = header.text.strip()

        current_date = datetime.strptime(current_month_year_text + " 1", "%B %Y %d")

        if current_date < target_date.replace(day=1):
            next_btn = calendar_popup.find_element(By.CLASS_NAME, "react-calendar__navigation__next-button")
            next_btn.click()
        elif current_date > target_date.replace(day=1):
            prev_btn = calendar_popup.find_element(By.CLASS_NAME, "react-calendar__navigation__prev-button")
            prev_btn.click()
        else:
            break
        time.sleep(0.5)

    # Step 2: Select day
    calendar_popup = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "react-calendar")))
    day_buttons = calendar_popup.find_elements(By.CLASS_NAME, "react-calendar__month-view__days__day")

    for button in day_buttons:
        if button.text == str(target_date.day) and "neighboringMonth" not in button.get_attribute("class"):
            button.click()
            return

    raise Exception(f"Could not select day {target_date.day} for '{label_text}'.")

def fill_and_submit_passenger_form(driver, passenger_data):
    wait = WebDriverWait(driver, 20)

    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.ESCAPE)
    time.sleep(2)

    driver.find_element(By.NAME, "first_name").send_keys(passenger_data["first_name"])
    driver.find_element(By.NAME, "last_name").send_keys(passenger_data["last_name"])
    driver.find_element(By.NAME, "email").send_keys(passenger_data["email"])
    driver.find_element(By.NAME, "passport_number").send_keys(passenger_data["passport_number"])
    driver.find_element(By.NAME, "nationality_id").send_keys(passenger_data["nationality"])
    driver.find_element(By.NAME, "contact_number").send_keys(passenger_data["contact_number"])

    gender_value = passenger_data["gender"].lower()
    gender_button = driver.find_element(By.XPATH, f"//button[@role='radio' and @value='{gender_value}']")
    driver.execute_script("arguments[0].click();", gender_button)
    print(f"✅ Gender set to: {passenger_data['gender']}")

    # Assume passenger_data = generate_fake_passengers(1)[0]
    click_date_button_by_label(wait,"Date of Birth")
    time.sleep(1)
    select_date_from_picker(wait, "Date of Birth", passenger_data["date_of_birth"])
    time.sleep(1)

    click_date_button_by_label(wait, "Passport Issue Date")
    time.sleep(1)
    select_date_from_picker(wait, "Passport Issue Date", passenger_data["passport_issue_date"])
    time.sleep(1)

    click_date_button_by_label(wait, "Passport Expiry Date")
    time.sleep(1)
    select_date_from_picker(wait, "Passport Expiry Date", passenger_data["passport_expiry_date"])
    time.sleep(1)

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

        wait.until(EC.url_contains("/passenger/list"))
        print("✅ Redirected to Passenger List after submission.")
    except Exception as e:
        print(f"❌ Could not submit form or redirect failed: {e}")


# def select_date_from_picker(wait, label_text, date_str):
#     """
#     Selects a date from a calendar popup based on the associated field label and target date.
#     - `wait`: WebDriverWait instance
#     - `label_text`: The exact label text for the date field (e.g., "Date of Birth")
#     - `date_str`: The target date in format "May 28, 2025"
#     """
#     # Step 1: Open the calendar picker button
#     label = wait.until(EC.presence_of_element_located((By.XPATH, f"//label[text()='{label_text}']")))
#     date_button = label.find_element(
#         By.XPATH, ".//following::button[.//span[text()='Pick a date']][1]"
#     )
#     date_button.click()
#
#     # Step 2: Wait for the calendar popup
#     calendar_popup = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "react-calendar")))
#
#     # Step 3: Parse the date
#     target_date = datetime.strptime(date_str, '%B %d, %Y')
#     target_month_year = target_date.strftime("%B %Y")
#
#     # Step 4: Navigate to the correct month/year
#     while True:
#         current_month_year_text = calendar_popup.find_element(
#             By.CLASS_NAME, "react-calendar__navigation__label"
#         ).text.strip()
#
#         current_date = datetime.strptime(current_month_year_text + " 1", "%B %Y %d")
#
#         if current_date < target_date.replace(day=1):
#             calendar_popup.find_element(By.CLASS_NAME, "react-calendar__navigation__next-button").click()
#         elif current_date > target_date.replace(day=1):
#             calendar_popup.find_element(By.CLASS_NAME, "react-calendar__navigation__prev-button").click()
#         else:
#             break
#         time.sleep(0.5)  # Allow animation/rendering
#
#     # Step 5: Click the correct day
#     day_buttons = calendar_popup.find_elements(By.CLASS_NAME, "react-calendar__month-view__days__day")
#     clicked = False
#     for i in range(2):  # Try twice in case of stale elements
#         try:
#             day_buttons = wait.until(EC.presence_of_all_elements_located(
#                 (By.CLASS_NAME, "react-calendar__month-view__days__day")
#             ))
#
#             for button in day_buttons:
#                 if (button.text == str(target_date.day) and
#                         "neighboringMonth" not in button.get_attribute("class")):
#                     wait.until(EC.element_to_be_clickable(button)).click()
#                     clicked = True
#                     break
#             if clicked:
#                 break
#         except StaleElementReferenceException:
#             print("⚠️ Retrying due to stale element...")
#             time.sleep(0.5)
#
#     if not clicked:
#         raise Exception(f"Could not select day {target_date.day} for '{label_text}'.")


# def fill_and_submit_passenger_form(driver, passenger_data):
#     wait = WebDriverWait(driver, 20)
#
#     body = driver.find_element(By.TAG_NAME, 'body')
#     body.send_keys(Keys.ESCAPE)
#     time.sleep(2)
#
#     driver.find_element(By.NAME, "first_name").send_keys(passenger_data["first_name"])
#     driver.find_element(By.NAME, "last_name").send_keys(passenger_data["last_name"])
#     driver.find_element(By.NAME, "email").send_keys(passenger_data["email"])
#     driver.find_element(By.NAME, "passport_number").send_keys(passenger_data["passport_number"])
#     driver.find_element(By.NAME, "nationality_id").send_keys(passenger_data["nationality"])
#     driver.find_element(By.NAME, "contact_number").send_keys(passenger_data["contact_number"])
#
#     gender_value = passenger_data["gender"].lower()
#     gender_button = driver.find_element(By.XPATH, f"//button[@role='radio' and @value='{gender_value}']")
#     driver.execute_script("arguments[0].click();", gender_button)
#     print(f"✅ Gender set to: {passenger_data['gender']}")
#
#     # Assume passenger_data = generate_fake_passengers(1)[0]
#     click_date_button_by_label(wait,"Date of Birth")
#     select_date_from_picker(wait, "Date of Birth", passenger_data["date_of_birth"])
#
#     click_date_button_by_label(wait, "Passport Issue Date")
#     select_date_from_picker(wait, "Passport Issue Date", passenger_data["passport_issue_date"])
#
#     click_date_button_by_label(wait, "Passport Expiry Date")
#     select_date_from_picker(wait, "Passport Expiry Date", passenger_data["passport_expiry_date"])
#
#     try:
#         submit_button = wait.until(EC.presence_of_element_located((
#             By.XPATH, "//button[@type='submit' and contains(text(), 'Submit')]"
#         )))
#         driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", submit_button)
#         time.sleep(0.5)
#
#         if submit_button.is_displayed() and submit_button.is_enabled():
#             driver.execute_script("arguments[0].click();", submit_button)
#             print("✅ Form submitted via JavaScript click.")
#         else:
#             print("⚠️ Submit button found but not interactable. Trying JS click directly.")
#             driver.execute_script("arguments[0].click();", submit_button)
#
#         wait.until(EC.url_contains("/passenger/list"))
#         print("✅ Redirected to Passenger List after submission.")
#     except Exception as e:
#         print(f"❌ Could not submit form or redirect failed: {e}")

    # # Step 1: Get day from closing_date
    # label = wait.until(EC.presence_of_element_located(
    #     (By.XPATH, "//label[text()='Date of Birth']")
    # ))
    # # Step 2: Navigate up to the container and then down to the associated "Pick a date" button
    # # This assumes the button is within the same parent div as the label
    # container = label.find_element(By.XPATH, "./ancestor::div[contains(@class, 'space-y-2')]")
    # date_button = container.find_element(By.XPATH, ".//button[.//span[text()='Pick a date']]")
    # # Step 3: Click the date picker button
    # date_button.click()
    #
    # # Wait for the calendar popup to appear
    # calendar_popup = wait.until(EC.presence_of_element_located(
    #     (By.CLASS_NAME, "react-calendar")
    # ))
    #
    # # Get the fake closing date from our generated data
    # date_of_birth_str = passenger_data["date_of_birth"]  # Format: "May 28, 2025"
    # # passport_issue_date_str = passenger_data["passport_issue_date"]
    #
    # # Parse the date to get day, month, and year
    # date_of_birth = datetime.strptime(date_of_birth_str, '%B %d, %Y')
    # day = date_of_birth.day
    # month = date_of_birth.strftime('%B')  # Full month name
    # year = date_of_birth.year
    #
    # # First check if we need to navigate to a different month/year
    # current_month_year = calendar_popup.find_element(
    #     By.CLASS_NAME, "react-calendar__navigation__label"
    # ).text
    #
    # if f"{month} {year}" not in current_month_year:
    #     # Navigate to the correct month/year
    #     while True:
    #         current_month_year = calendar_popup.find_element(
    #             By.CLASS_NAME, "react-calendar__navigation__label"
    #         ).text
    #
    #         current_date = datetime.strptime(current_month_year + " 1", "%B %Y %d")
    #         target_date = datetime.strptime(f"{month} {year} 1", "%B %Y %d")
    #
    #         if current_date < target_date:
    #             # Click next button
    #             next_btn = calendar_popup.find_element(
    #                 By.CLASS_NAME, "react-calendar__navigation__next-button"
    #             )
    #             next_btn.click()
    #         elif current_date > target_date:
    #             # Click previous button
    #             prev_btn = calendar_popup.find_element(
    #                 By.CLASS_NAME, "react-calendar__navigation__prev-button"
    #             )
    #             prev_btn.click()
    #         else:
    #             break
    #
    # # Now select the day
    # day_buttons = calendar_popup.find_elements(
    #     By.CLASS_NAME, "react-calendar__month-view__days__day"
    # )
    #
    # for button in day_buttons:
    #     if button.text == str(
    #             day) and "react-calendar__month-view__days__day--neighboringMonth" not in button.get_attribute("class"):
    #         button.click()
    #         break


