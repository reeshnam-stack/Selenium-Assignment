import pytest
import os
import time
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.form_page import FormPage

faker = Faker()


@pytest.mark.usefixtures("driver", "config")
def test_add_to_cart_and_checkout(driver, config):
    try:
        # ---------- LOGIN ----------
        login_page = LoginPage(driver)
        login_page.visit(config["base_url"])
        login_page.login(config["username"], config["password"])

        assert login_page.is_logged_in(), "Login failed"

        # ---------- ADD PRODUCT TO CART ----------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".inventory_item button"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

        # ---------- CHECKOUT FORM ----------
        form_page = FormPage(driver)

        first_name = faker.first_name()
        last_name = faker.last_name()
        postal_code = faker.postcode()

        form_page.fill_checkout_form(first_name, last_name, postal_code)
        form_page.finish_checkout()

        # ---------- VERIFY SUCCESS ----------
        # This checks for "THANK YOU FOR YOUR ORDER"
        assert form_page.is_successful(), "Checkout failed"

    except Exception as e:
        # ---------- SCREENSHOT ON FAILURE ----------
        os.makedirs("reports", exist_ok=True)
        screenshot_file = f"reports/checkout_failure_{int(time.time())}.png"
        driver.save_screenshot(screenshot_file)
        print(f"\nScreenshot saved at: {screenshot_file}")

        raise e
