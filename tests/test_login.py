import pytest
import os
import time
from pages.login_page import LoginPage


@pytest.mark.parametrize("username,password,expected_result", [
    ("standard_user", "secret_sauce", True),      # Valid user
    ("locked_out_user", "secret_sauce", False),   # Invalid user
])
def test_login_parameterized(driver, username, password, expected_result):
    try:
        login_page = LoginPage(driver)
        login_page.visit("https://www.saucedemo.com/")

        login_page.login(username, password)

        if expected_result:
            assert login_page.is_logged_in(), "Valid user login failed"
        else:
            assert not login_page.is_logged_in(), "Invalid user login should fail"

    except Exception as e:
        # ---------- SCREENSHOT ON FAILURE ----------
        os.makedirs("reports", exist_ok=True)
        screenshot_file = f"reports/login_failure_{username}_{int(time.time())}.png"
        driver.save_screenshot(screenshot_file)
        print(f"\nScreenshot saved at: {screenshot_file}")

        raise e
