import allure
import pytest

from pages.Keys import Keys
from .BaseJobApplication import BaseJobApplicationTest
from utils.JsonReader import JsonReader

data=JsonReader().read_json("test_data/common.json")
search=data['SEARCH_VALUE']

personal_data=JsonReader().read_json("test_data/job_application_form/job_application_form.json")
personal_details=personal_data['PERSONAL_DETAILS']

@allure.epic("Challenge")
@allure.feature("Job Application Flow")
@allure.story("JAF_004 - Add and delete skill chips")
@allure.description("Ensure skills can be added and deleted dynamically.")
@allure.severity(allure.severity_level.CRITICAL)

@pytest.mark.smoke
@pytest.mark.order(4)
@pytest.mark.usefixtures("browser_setup")
class TestJAF002(BaseJobApplicationTest):

    @allure.title("Navigate to login page")
    @pytest.mark.order(1)
    def test_navigate_to_login_page(self, pages):
        self.navigate_to_login_page(pages, search)

    @allure.title("Add skills")
    @pytest.mark.order(2)
    def test_add_skills(self,pages):
            with allure.step("Add skills"):
                self.add_skills(pages, personal_details)

            with allure.step("Verify added skills"):
                common = pages["common"]
                for skill in personal_details["SKILLS"]:
                    key=skill
                    common.verify_chips_added(key)

    @allure.title("Delete skill")
    @pytest.mark.order(3)
    def test_delete_skills(self,pages):
            with allure.step("Delete skills"):
                job_application = pages["job_application"]
                for skill in personal_details["SKILLS"]:
                    job_application.delete_skills({Keys.SKILLS.value: skill})


            with allure.step("Verify deleted skills"):
                common = pages["common"]
                for skill in personal_details["SKILLS"]:
                    key = skill
                    common.verify_chips_deleted(key)
