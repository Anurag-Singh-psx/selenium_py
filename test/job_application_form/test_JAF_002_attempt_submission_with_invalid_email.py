
import allure
import pytest

from test.job_application_form.BaseJobApplication import BaseJobApplicationTest
from utils.JsonReader import JsonReader
from pages.Keys import Keys

data=JsonReader().read_json("test_data/common.json")
search=data['SEARCH_VALUE']

data_1=JsonReader().read_json("test_data/job_application_form/job_application_form.json")
personal_details=data_1['PERSONAL_DETAILS']

@allure.epic("Challenge")
@allure.feature("Job Application Flow")
@allure.story("JAF_002 - Attempt submission with invalid email")
@allure.description("Enter an invalid email and try to submit the form.")
@allure.severity(allure.severity_level.CRITICAL)

@pytest.mark.order(2)
@pytest.mark.usefixtures("browser_setup")
class TestJAF002(BaseJobApplicationTest):

    @allure.title("Validation error should appear for email field.")
    @pytest.mark.order(1)
    def test_submit_with_accept_terms(self, pages):
        email='abc@xyz'

        self.navigate_to_login_page(pages, search)
        self.enter_personal_details(pages, personal_details,email)
        self.select_gender_and_language(pages, personal_details)
        self.add_skills(pages, personal_details)
        self.add_job_roles(pages, personal_details)
        self.self_rating(pages, personal_details)
        self.upload_resume(pages, personal_details)
        self.add_date_time(pages)

        with allure.step("Accept terms and submit"):
            job_application = pages["job_application"]
            job_application.accept_term({Keys.TERMS.value: personal_details["TERMS"]})
            job_application.submit()

        with allure.step("Verify email error helper text is shown"):
            common = pages["common"]
            common.verify_error_message("Enter a valid email")

