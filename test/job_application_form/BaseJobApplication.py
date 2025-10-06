import allure
from utils.DataGenerator import DataGenerator
from pages.Keys import Keys

class BaseJobApplicationTest:

    @staticmethod
    def navigate_to_login_page(pages, search):
        common_page = pages["common"]
        with allure.step(f"Search for {search[1]} and click on View Challenge button"):
            common_page.search_and_view_challenge(search[1])

    @staticmethod
    def enter_personal_details(pages, personal_details,email):
        with allure.step("Enter valid salutation, first name, last name, email, and mobile"):
            job_application = pages["job_application"]
            personal_details_data = {
                Keys.FIRST_NAME.value: DataGenerator.generate_random_string(5),
                Keys.LAST_NAME.value: DataGenerator.generate_random_string(5),
                Keys.MOBILE.value: DataGenerator.generate_random_number(10),
                Keys.EMAIL.value: email,
                Keys.SALUTATION.value: personal_details["SALUTATION"][0],
            }
            job_application.enter_personal_details(personal_details_data)

    @staticmethod
    def select_gender_and_language(pages, personal_details):
        with allure.step("Select gender and languages"):
            job_application = pages["job_application"]
            job_application.select_gender({Keys.GENDER.value: personal_details["GENDER"]})
            job_application.select_language({Keys.LANGUAGE.value: personal_details["LANGUAGE"]})

    @staticmethod
    def add_skills(pages, personal_details):
        with allure.step("Add skills using Enter key"):
            job_application = pages["job_application"]
            for skill in personal_details["SKILLS"]:
                job_application.add_skills({Keys.SKILLS.value: skill})

    @staticmethod
    def add_job_roles( pages, personal_details):
        with allure.step("Select multiple job roles"):
            job_application = pages["job_application"]
            for role in personal_details["JOB_ROLES"]:
                job_application.add_job_roles({Keys.JOB_ROLES.value: role})

    @staticmethod
    def self_rating( pages, personal_details):
        with allure.step("Set rating slider to 7"):
            job_application = pages["job_application"]
            job_application.self_rating(personal_details["SELF_RATING"])

    @staticmethod
    def upload_resume(pages, personal_details):
        with allure.step("Upload a valid .pdf resume"):
            job_application = pages["job_application"]
            common = pages["common"]
            job_application.upload_resume(personal_details["FILE_NAME"], common)

    @staticmethod
    def add_date_time( pages):
        with allure.step("Pick valid date and time"):
            job_application = pages["job_application"]
            job_application.add_date_time("15-10-2025", "14:30")
