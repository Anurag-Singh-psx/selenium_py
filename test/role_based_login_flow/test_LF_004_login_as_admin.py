from time import sleep

import allure
import pytest

from utils.JsonReader import JsonReader
data=JsonReader().read_json("test_data/role_based_login_flow/role_based_login.json")
search=data['SEARCH']
login_details=data['ADMIN']

@allure.epic("Challenge")
@allure.feature("Role-Based Login Flow")
@allure.story("LF_004 - Login as Admin")
@allure.description("Login with valid Admin credentials and verify Admin dashboard")
@allure.severity(allure.severity_level.CRITICAL)

@pytest.mark.regression
@pytest.mark.order(4)
@pytest.mark.usefixtures("browser_setup")
class TestLF004:

    @allure.title("Navigate to login page")
    @pytest.mark.order(1)
    def test_navigate_to_login_page(self,pages):
        common_page = pages["common"]
        with allure.step(f"Search for {search['SEARCH_CHALLENGE']} and click on View Challenge button"):
            common_page.search_and_view_challenge(search['SEARCH_CHALLENGE'])

    @allure.title("Enter login details")
    @pytest.mark.order(2)
    def test_click_on_login(self,pages):
        login_page = pages["login"]
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

