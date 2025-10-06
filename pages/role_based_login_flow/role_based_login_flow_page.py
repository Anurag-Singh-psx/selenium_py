from time import sleep

from selenium.webdriver.common.by import By

from pages.BaseClass import BaseClass


class LoginFlowPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.username_input=(By.XPATH,"//*[contains(@class,'MuiCardContent-root')]//label[contains(text(),'Username')]/following-sibling::div/input")
        self.password_input=(By.XPATH,"//*[contains(@class,'MuiCardContent-root')]//label[contains(text(),'Password')]/following-sibling::div/input")
        self.login_button=(By.XPATH,"//button[contains(text(),'Login')]")
        self.logout_button=(By.XPATH,"//button[contains(text(),'Logout')]")

    def enter_login_details(self,username,password) :
        self.element_actions.input_text(self.username_input,username)
        self.element_actions.input_text(self.password_input,password)

    def click_login_button(self):
        self.element_actions.click_element(self.login_button)

    def click_logout_button(self):
        self.element_actions.click_element(self.logout_button)
