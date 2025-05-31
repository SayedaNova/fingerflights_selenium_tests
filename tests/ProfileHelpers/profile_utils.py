import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.Data.profile_data import profile_to_update
from tests.ProfileHelpers.update_profile import update_profile


def navigate_to_edit_profile_page(email, password, driver):
    wait = WebDriverWait(driver, 15)

    # Step 1: Click "Profile" in sidebar (main sidebar)
    profile_sidebar_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='Profile']/ancestor::a")
    ))
    profile_sidebar_link.click()

    # Step 2: Wait for profile page to fully load
    # wait.until(EC.url_contains("/profile"))

    time.sleep(3)

    # Step 3: Click "Edit Profile" from the right sidebar
    # Step 3: Click "Edit Profile" from the right sidebar
    edit_profile_sidebar_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@href='/profile/edit'][.//span[contains(text(), 'Edit Profile')]]")
    ))
    driver.execute_script("arguments[0].click();", edit_profile_sidebar_link)

    # Step 4: Confirm redirection to /profile/edit
    wait.until(EC.url_contains("/profile/edit"))

    time.sleep(3)

    wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Name')]")))

    print("✅ Navigated to Edit Profile page from right sidebar.")
    return driver

def profile_update(driver):
    if not profile_to_update:
        print("⚠ No profiles to update.")
        return

    for idx, profile in enumerate(profile_to_update):
        # Update profile with fake data
        update_profile(driver, profile)

        # After form submission, wait for redirection to profile view
        WebDriverWait(driver, 10).until(EC.url_contains("/profile"))
        time.sleep(5)

        # If there are more profiles to update, return to edit page
        if idx < len(profile_to_update) - 1:
            driver.get("http://178.128.114.165:73/profile/edit")
            time.sleep(2)
