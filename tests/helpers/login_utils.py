import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.helpers.otp_utils import get_latest_email_id, wait_for_new_otp
from tests.helpers.driver_utils import get_driver

def login_with_otp(email, password):
    driver = get_driver()
    driver.get("http://178.128.114.165:73/admin/login")
    driver.maximize_window()
    time.sleep(1)

    previous_id = get_latest_email_id()

    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password, Keys.RETURN)

    while driver.current_url != "http://178.128.114.165:73/otp":
        time.sleep(0.5)

    otp = wait_for_new_otp(previous_id)
    assert otp is not None, f"Failed to retrieve OTP for {email}"

    wait = WebDriverWait(driver, 10)
    otp_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-input-otp="true"]')))
    otp_input.send_keys(otp)

    time.sleep(5)
    return driver