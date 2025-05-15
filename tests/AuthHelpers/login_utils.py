import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.AuthHelpers.otp_utils import get_latest_email_id, wait_for_new_otp


#will store the cookies of one user in session directory.
# SESSION_DIR = "tests/AuthHelpers/sessions"
#
# def save_cookies(driver, email):
#     os.makedirs(SESSION_DIR, exist_ok=True) #create session directory if it doesnt exist
#     cookie_file = os.path.join(SESSION_DIR, f"{email}.json") #make full path to the cookie file using the user's email.
#     with open(cookie_file, "w") as f:
#         json.dump(driver.get_cookies(), f)
#
# def load_cookies(driver, url, email):
#     cookie_file = os.path.join(SESSION_DIR, f"{email}.json")
#     if not os.path.exists(cookie_file):
#         raise FileNotFoundError(f"❌ Cookie file for {email} not found.")
#
#     with open(cookie_file, "r") as f:
#         cookies = json.load(f)
#
#     driver.get(url)  # Must visit domain before adding cookies
#     for cookie in cookies:
#         cookie.pop("expiry", None)  # Remove expiry to avoid issues
#         driver.add_cookie(cookie)
#     driver.refresh()

def login_with_otp(email, password,  driver=None):
    if driver is None:
        from tests.Driver.driver_utils import get_driver
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