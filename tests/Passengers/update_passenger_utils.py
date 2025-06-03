import time
from datetime import datetime
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_date_button_by_label(wait, label_text):
    label = wait.until(EC.presence_of_element_located((By.XPATH, f"//label[contains(text(), '{label_text}')]")))
    button = label.find_element(By.XPATH, ".//following::button")
    wait.until(EC.element_to_be_clickable(button)).click()

def select_date_from_picker(wait, label_text, date_str):
    target_date = datetime.strptime(date_str, '%B %d, %Y')
    target_month_start = target_date.replace(day=1)

    previous_month_year = None

    while True:
        calendar_popup = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "react-calendar")))

        header = calendar_popup.find_element(By.CLASS_NAME, "react-calendar__navigation__label")
        current_month_year_text = header.text.strip()
        current_date = datetime.strptime(current_month_year_text + " 1", "%B %Y %d")

        if current_month_year_text == previous_month_year:
            raise Exception("Calendar is stuck — probably in an infinite loop.")
        previous_month_year = current_month_year_text

        delta_months = (target_month_start.year - current_date.year) * 12 + (target_month_start.month - current_date.month)

        if delta_months > 12:
            next_btn = calendar_popup.find_element(By.CLASS_NAME, "react-calendar__navigation__next2-button")
            next_btn.click()
        elif delta_months < -12:
            prev_btn = calendar_popup.find_element(By.CLASS_NAME, "react-calendar__navigation__prev2-button")
            prev_btn.click()
        elif delta_months > 0:
            next_btn = calendar_popup.find_element(By.CLASS_NAME, "react-calendar__navigation__next-button")
            next_btn.click()
        elif delta_months < 0:
            prev_btn = calendar_popup.find_element(By.CLASS_NAME, "react-calendar__navigation__prev-button")
            prev_btn.click()
        else:
            break

        time.sleep(0.3)

    day_buttons = calendar_popup.find_elements(By.CLASS_NAME, "react-calendar__month-view__days__day")
    for button in day_buttons:
        if button.text == str(target_date.day) and "neighboringMonth" not in button.get_attribute("class"):
            button.click()
            return

    raise Exception(f"Could not select day {target_date.day} for '{label_text}'.")

def update_passenger(driver, passenger_data):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))

    time.sleep(3)

    # Find the row containing the user by email
    rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'hover:shadow-md')]")
    for row in rows:
        if passenger_data["email"] in row.text:
            edit_button = row.find_element(By.XPATH, ".//a[contains(@href, '/update/')]")
            edit_button.click()
            WebDriverWait(driver, 10).until(EC.url_contains("/passenger/update"))
            break
    else:
        raise Exception(f"❌ Could not find user with passenger: {passenger_data['email']}")

    wait = WebDriverWait(driver, 20)

    # body = driver.find_element(By.TAG_NAME, 'body')
    # body.send_keys(Keys.ESCAPE)
    time.sleep(5)

    driver.find_element(By.NAME, "first_name").clear()
    driver.find_element(By.NAME, "first_name").send_keys(passenger_data["first_name"])
    driver.find_element(By.NAME, "last_name").clear()
    driver.find_element(By.NAME, "last_name").send_keys(passenger_data["last_name"])
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(passenger_data["email"])
    driver.find_element(By.NAME, "passport_number").clear()
    driver.find_element(By.NAME, "passport_number").send_keys(passenger_data["passport_number"])
    driver.find_element(By.NAME, "contact_number").clear()
    driver.find_element(By.NAME, "contact_number").send_keys(passenger_data["contact_number"])

    gender_value = passenger_data["gender"].lower()
    gender_button = driver.find_element(By.XPATH, f"//button[@role='radio' and @value='{gender_value}']")
    driver.execute_script("arguments[0].click();", gender_button)
    print(f"✅ Gender updated to: {passenger_data['gender']}")

    click_date_button_by_label(wait,"Date of Birth")
    time.sleep(1)
    select_date_from_picker(wait, "Date of Birth", passenger_data["date_of_birth"])
    time.sleep(1)

    click_date_button_by_label(wait, "Passport Issue Date")
    time.sleep(1)
    select_date_from_picker(wait, "Passport Issue Date", passenger_data["passport_issue_date"])
    time.sleep(1)

    click_date_button_by_label(wait, "Passport Expire Date")
    time.sleep(1)
    select_date_from_picker(wait, "Passport Expire Date", passenger_data["passport_expiry_date"])
    time.sleep(1)

    try:
        submit_button = wait.until(EC.presence_of_element_located((
            By.XPATH, "//button[@type='submit' and contains(text(), 'Submit')]"
        )))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", submit_button)
        time.sleep(0.5)

        if submit_button.is_displayed() and submit_button.is_enabled():
            driver.execute_script("arguments[0].click();", submit_button)
            print("✅ Form updated via JavaScript click.")
        else:
            print("⚠️ Update button found but not interactable. Trying JS click directly.")
            driver.execute_script("arguments[0].click();", submit_button)

        wait.until(EC.url_contains("/passenger/list"))
        print("✅ Redirected to Passenger List after update.")
    except Exception as e:
        print(f"❌ Could not update form or redirect failed: {e}")
