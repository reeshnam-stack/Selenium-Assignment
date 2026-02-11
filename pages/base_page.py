# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def visit(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        """Wait until the element is present and return it."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            return None

    def click(self, locator, timeout=10):
        """Wait until element is clickable and click."""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def send_keys(self, locator, text, timeout=10):
        """Wait until element is visible and send keys."""
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def wait_for_title(self, title, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.title_contains(title)
        )

    def take_screenshot(self, name="screenshot.png"):
        screenshot_path = os.path.join(os.getcwd(), "reports", name)
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path
