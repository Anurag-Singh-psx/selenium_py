
import allure
import pytest

from .BaseJobApplication import BaseJobApplicationTest
from utils.DataGenerator import DataGenerator
from utils.JsonReader import JsonReader
from pages.Keys import Keys

data=JsonReader().read_json("test_data/common.json")
search=data['SEARCH_VALUE']

data_1=JsonReader().read_json("test_data/job_application_form/job_application_form.json")
personal_details=data_1['PERSONAL_DETAILS']


@allure.epic("Challenge")
@allure.feature("Job Application Flow")
@allure.story("JAF_001 - Submit form with valid data")
@allure.description("Fill in all fields correctly, upload a valid resume, and accept terms before submission.")
@allure.severity(allure.severity_level.CRITICAL)

@pytest.mark.smoke
@pytest.mark.order(1)
@pytest.mark.usefixtures("browser_setup")
class TestJAF001(BaseJobApplicationTest):

    @allure.title("Submit form with valid data")
    @pytest.mark.order(1)
    def test_submit_with_accept_terms(self, pages):
        email=f"abc+{DataGenerator.generate_random_number(4)}@gmail.com"
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

        with allure.step("Verify success snackbar message"):
            common = pages["common"]
            common.verify_alert_message("Application Submitted Successfully!")

