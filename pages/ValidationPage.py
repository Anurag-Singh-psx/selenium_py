from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.BaseClass import BaseClass

class ValidationPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.XPATH,
                               "//*[contains(@class,'MuiCardContent-root')]//label[contains(text(),'Username')]/following-sibling::div/input")
        self.password_input = (By.XPATH,
                               "//*[contains(@class,'MuiCardContent-root')]//label[contains(text(),'Password')]/following-sibling::div/input")

    def validate_logout(self):
        element=self.element_actions.wait_for_element((By.XPATH, "//*[contains(@class,'MuiCardContent-root')]//*[contains(@class, 'MuiTypography-root') and contains(text(),'Login')]"))
        assert element,f"Logout failed"
        return element

    def validate_login_empty_fields(self):
        username_input_text=self.element_actions.get_input_text(self.username_input)
        password_input_text=self.element_actions.get_input_text(self.password_input)
        assert username_input_text == "" and password_input_text == ""

