from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.Demo_Data import profile_data
from tests.Demo_Data.profile_data import profile_to_update


def update_profile(driver, profile):
    wait = WebDriverWait(driver, 10)

    # Update name
    name_input = wait.until(EC.visibility_of_element_located((By.NAME, "name")))
    name_input.clear()
    name_input.send_keys(profile["name"])

    # Update phone
    # phone_input = wait.until(EC.visibility_of_element_located((By.NAME, "phone")))
    # phone_input.clear()
    # phone_input.send_keys(profile["phone"])

    # --- Select gender via JavaScript (bypass overlay issues)
    gender_value = profile["gender"].lower()
    gender_button = driver.find_element(By.XPATH, f"//button[@role='radio' and @value='{gender_value}']")
    driver.execute_script("arguments[0].click();", gender_button)
    print(f"✅ Gender set to: {profile['gender']}")

    submit_button = wait.until(EC.presence_of_element_located((
        By.XPATH, "//button[contains(@class, 'bg-ffblue') and normalize-space(text())='Submit']"
    )))

    wait.until(EC.element_to_be_clickable(submit_button))

    submit_button.click()
    print("✅ Form submitted via direct click")

    print(f"✅ Updated profile with: {profile}")
    return profile


