# pages/form_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FormPage(BasePage):
    # Locators
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MSG = (By.CLASS_NAME, "complete-header")  # "THANK YOU FOR YOUR ORDER"

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def is_successful(self):
        """Check if checkout was successful by verifying success message."""
        element = self.find_element(self.SUCCESS_MSG, timeout=20)
        return element is not None and element.is_displayed()
