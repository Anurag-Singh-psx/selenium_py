import allure
import pytest

from test.job_application_form.BaseJobApplication import BaseJobApplicationTest
from utils.JsonReader import JsonReader

data=JsonReader().read_json("test_data/common.json")
search=data['SEARCH_VALUE']

data_1=JsonReader().read_json("test_data/job_application_form/job_application_form.json")
personal_details=data_1['PERSONAL_DETAILS']

@allure.epic("Challenge")
@allure.feature("Job Application Flow")
@allure.story("JAF_003 - Upload invalid resume file")
@allure.description("Try uploading a file that is not PDF or DOCX.")
@allure.severity(allure.severity_level.CRITICAL)

@pytest.mark.order(3)
@pytest.mark.usefixtures("browser_setup")
class TestJAF002(BaseJobApplicationTest):

    @allure.title("Error snackbar should display 'Only .pdf or .docx allowed'.")
    @pytest.mark.order(1)
    def test_navigate_to_login_page(self, pages):
        self.navigate_to_login_page(pages, search)



    @allure.title("Upload invalid resume file")
    @pytest.mark.order(2)
    def test_upload_resume(self,pages):
            with allure.step("Upload a invalid resume"):
                job_application = pages["job_application"]
                common = pages["common"]
                job_application.upload_resume(personal_details["INVALID_FILE_NAME"], common)

            with allure.step("Verify snackbar shows error message"):
                common = pages["common"]
                common.verify_alert_message("Only .pdf or .docx allowed")
