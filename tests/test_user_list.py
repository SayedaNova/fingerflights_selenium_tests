import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Assuming test_login_and_verify_otp(driver) returns a logged-in driver
from tests.test_login_with_otp import test_login_and_verify_otp

@pytest.mark.userlist
def test_user_list_access(driver):
    driver = test_login_and_verify_otp(driver)

    wait = WebDriverWait(driver, 10)

    # Step 1: Click on sidebar "User" main menu (expands submenu)
    try:
        user_menu_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='http://178.128.114.165:73']//span[text()='User']")
        ))
        user_menu_button.click()
    except Exception as e:
        pytest.fail(f"❌ Failed to click User menu button: {e}")

    # Step 2: Click "All" under "User" submenu
    try:
        user_list_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='http://178.128.114.165:73']//span[text()='All']")
        ))
        user_list_link.click()
    except Exception as e:
        pytest.fail(f"❌ Failed to click User List submenu item: {e}")

    # Step 3: Assert we're on the user list page (you may need to adjust this)
    try:
        wait.until(EC.url_contains("http://178.128.114.165:73/user/list?per_page=50"))
        assert "http://178.128.114.165:73/user/list?per_page=50" in driver.current_url
    except Exception:
        pytest.fail("❌ Did not land on /user/list page.")
