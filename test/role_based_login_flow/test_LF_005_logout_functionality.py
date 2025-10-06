from time import sleep

import allure
import pytest

from utils.JsonReader import JsonReader
data=JsonReader().read_json("test_data/role_based_login_flow/role_based_login.json")
search=data['SEARCH']
login_details=data['ADMIN']

@allure.epic("Challenge")
@allure.feature("Role-Based Login Flow")
@allure.story("LF_005 - Logout functionality")
@allure.description("Logout from User/Admin dashboard and verify return to login form")
@allure.severity(allure.severity_level.CRITICAL)

@pytest.mark.order(5)
@pytest.mark.usefixtures("browser_setup")
class TestLF005:

    @allure.title("Navigate to login page")
    @pytest.mark.order(1)
    def test_navigate_to_login_page(self,pages):
        common_page = pages["common"]
        with allure.step(f"Search for {search['SEARCH_CHALLENGE']} and click on View Challenge button"):
            common_page.search_and_view_challenge(search['SEARCH_CHALLENGE'])

    @allure.title("Enter login details")
    @pytest.mark.order(2)
    def test_click_on_login(self,pages):
        common_page = pages["common"]
        login_page = pages["login"]
        validation_page = pages["validation"]
        with allure.step("Enter username and password"):
            login_page.enter_login_details(login_details["USERNAME"],login_details["PASSWORD"])
            login_page.click_login_button()

    @allure.title("Verify Admin login")
    @pytest.mark.order(3)
    def test_verify_error_message(self,pages):
        common_page = pages["common"]
        with allure.step("Admin dashboard is displayed with welcome message and Admin role info"):
            assert_error=common_page.verify_alert_message("You are logged in as ADMIN")
            assert assert_error.is_displayed()

    @allure.title("Verify login form is displayed")
    @pytest.mark.order(4)
    def test_verify_login_form(self, pages):
        login_page = pages["login"]
        validation_page = pages["validation"]
        with allure.step("After logout login form should be displayed"):
            login_page.click_logout_button()
            assert_logout = validation_page.validate_logout()
            assert assert_logout.is_displayed()

    @allure.title("Verify fields are reset to empty")
    @pytest.mark.order(5)
    def test_verify_empty_fields(self, pages):
        validation_page = pages["validation"]
        with allure.step("Verify fields are reset to empty"):
            validation_page.validate_login_empty_fields()



