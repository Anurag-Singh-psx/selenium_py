import json
import os

from pages.CommonPage import CommonPage
from pages.ValidationPage import ValidationPage
from pages.job_application_form.job_application_form import JobApplicationForm
from pages.role_based_login_flow.role_based_login_flow_page import LoginFlowPage


class ObjectManager:
    def __init__(self,driver):
        self.driver = driver
        self.login_flow_page=None
        self._common_page=None
        self._validation_page=None
        self._job_application_page=None

    @property
    def role_based_login_flow(self):
        if self.login_flow_page is None:
            self.login_flow_page = LoginFlowPage(self.driver)

        return self.login_flow_page

    @property
    def common_page(self):
        if self._common_page is None:
            self._common_page = CommonPage(self.driver)
        return self._common_page

    @property
    def validation_page(self):
        if self._validation_page is None:
            self._validation_page = ValidationPage(self.driver)
        return self._validation_page

    @property
    def job_application_page(self):
        if self._job_application_page is None:
            self._job_application_page = JobApplicationForm(self.driver)
        return self._job_application_page

