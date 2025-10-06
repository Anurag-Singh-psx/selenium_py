import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.BaseClass import BaseClass

class CommonPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_challenge_input=(By.ID,"«r2»")
        self.view_challenge = (By.XPATH, "//button[contains(text(),'View Challenge')]")
        self.challenge_tab=(By.XPATH, "//*[@role='tablist']/button[contains(text(),'Challenge')]")
        self.muli_alert_message=(By.XPATH, "//*[contains(@class, 'MuiAlert-message')]")
        self.resume_locator=(By.CSS_SELECTOR,"input[type='file'][accept]")

    def search_and_view_challenge(self,search_text):
        self.element_actions.input_text(self.search_challenge_input,search_text)
        self.element_actions.click_element(self.view_challenge)
        self.element_actions.click_element(self.challenge_tab)

    def verify_alert_message(self,message):
        alert_message=self.element_actions.wait_for_element((By.XPATH, f"//div[contains(@class, 'MuiAlert-message') and contains(normalize-space(.),'{message}')]"))
        assert alert_message,f"Expected alert message '{message}' not found!"
        return alert_message

    def verify_error_message(self,message):
        alert_message=self.element_actions.wait_for_element((By.XPATH, f"//*[contains(@class, 'Mui-required') and contains(normalize-space(.),'{message}')]"))
        assert alert_message,f"Expected alert message '{message}' not found!"
        return alert_message

    def file_upload(self,file_path,allowed_extension=None):
        file_path=os.path.abspath(file_path)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} not found")

        file_input=self.element_actions.presence_of_element_located(self.resume_locator)

        if allowed_extension is None:
            accept_attr=file_input.get_attribute("accept")
            if accept_attr is None:
                accept_attr=""

            raw_parts=accept_attr.split(",")
            parsed=[]
            for part in raw_parts:
                cleaned=part.strip()
                if cleaned!="":
                    parsed.append(cleaned.lower())

            if len(parsed)>0:
                allowed_extension=parsed
                allowed_extension.append(".txt")
            else:
                allowed_extension=[".pdf", ".docx",".txt"]

        normalized_allowed=[]
        for extension in allowed_extension:
            normalized_allowed.append(extension.lower())

        file_name, file_extension = os.path.splitext(file_path)
        ext = file_extension.lower()

        if ext in normalized_allowed:
            is_ext_allowed = True
        else:
            is_ext_allowed = False

        if not is_ext_allowed:
            raise ValueError(
                "Upload failed — file extension not allowed. "
                f"File extension: '{ext}', Allowed: {allowed_extension}"
            )

        file_input.send_keys(file_path)
