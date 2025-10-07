from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.Keys import Keys
from pages.BaseClass import BaseClass
from utils.JsonReader import JsonReader

class JobApplicationForm(BaseClass):
    def __init__(self, request):
        super().__init__(request)
        self.salutation_input=(By.NAME, "salutation")
        self.first_name_input=(By.NAME, "firstName")
        self.last_name_input=(By.NAME, "lastName")
        self.email_input=(By.NAME, "email")
        self.mobile_input=(By.NAME, "mobile")
        self.add_skills_input=(By.XPATH, "//span[contains(text(),'Add a Skill')]/ancestor::div[1]/input")
        self.job_roles=(By.ID, "mui-component-select-jobRoles")
        self.slider=(By.CSS_SELECTOR, ".MuiSlider-thumb")
        self.upload_file=(By.XPATH,"//input[@type='file']")
        self.date=(By.NAME, "availableDate")
        self.time=(By.NAME, "availableTime")
        self.submit_button=(By.XPATH, "//button[@type='button'][contains(text(),'Submit')]")

    def enter_personal_details(self, data: dict[str, object]):

        if data.get(Keys.FIRST_NAME.value):
            self.element_actions.input_text(self.first_name_input, data.get(Keys.FIRST_NAME.value))

        if data.get(Keys.LAST_NAME.value):
            self.element_actions.input_text(self.last_name_input, data.get(Keys.LAST_NAME.value))

        if data.get(Keys.EMAIL.value):
            self.element_actions.input_text(self.email_input, data.get(Keys.EMAIL.value))

        if data.get(Keys.MOBILE.value):
            self.element_actions.input_text(self.mobile_input, data.get(Keys.MOBILE.value))

        if data.get(Keys.SALUTATION.value):
            self.element_actions.input_text(self.salutation_input, data.get(Keys.SALUTATION.value))

    def select_gender(self, data: dict[str, object]):
        if data.get(Keys.GENDER.value):
            self.element_actions.select_radio_element_by_value((By.XPATH,f"//*[contains(@class,'MuiFormControlLabel-root')]//input[@type='radio' and @value='{data.get(Keys.GENDER.value)}']/.."))

    def select_language(self, data: dict[str, object]):
        if data.get(Keys.LANGUAGE.value):
            self.element_actions.select_checkbox_element_by_label((By.XPATH,f"//label[.//span[text()='{data.get(Keys.LANGUAGE.value)}']]//input[@type='checkbox']/.."))

    def add_skills(self, data: dict[str, object]):
        if data.get(Keys.SKILLS.value):
            self.element_actions.input_text_with_enter(self.add_skills_input, data.get(Keys.SKILLS.value))

    def add_job_roles(self, data: dict[str, object]):
        if data.get(Keys.JOB_ROLES.value):
            self.element_actions.click_element(self.job_roles)

            menu_locator = (By.XPATH, "//ul[contains(@class,'MuiMenu-list')]")
            self.element_actions.wait_for_element(menu_locator)

            option_locator = (By.XPATH,f"//ul[contains(@class,'MuiMenu-list')]//li[@data-value='{data.get(Keys.JOB_ROLES.value)}']")
            self.element_actions.select_checkbox_element_by_label(option_locator)

            self.element_actions.perform_keyboard_tab()

    def delete_skills(self, data: dict[str, object]):
        if data.get(Keys.SKILLS.value):
            key = self.element_actions.wait_for_element(
                (By.XPATH, f"//*[contains(@class, 'MuiChip-label') and contains(normalize-space(.),'{data.get(Keys.SKILLS.value)}')]/following-sibling::*[contains(@class,'MuiChip-deleteIcon')]"))
            key.click()


    def self_rating(self,rating):
        self.element_actions.perform_sliding(self.slider,rating)

    def upload_resume(self,path,common_page):
        common_page.file_upload(path)

    def add_date_time(self,date,time):
        self.element_actions.input_text(self.date,date)
        self.element_actions.input_text(self.time,time)

    def accept_term(self,data:dict[str, object]):
        if data.get(Keys.TERMS.value):
            self.element_actions.select_checkbox_element_by_label(
                (By.XPATH, f"//label[.//span[text()='{data.get(Keys.TERMS.value)}']]//input[@type='checkbox']/.."))

    def submit(self):
        self.element_actions.click_element(self.submit_button)
