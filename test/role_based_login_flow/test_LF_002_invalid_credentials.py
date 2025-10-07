from time import sleep

import allure
import pytest

from utils.JsonReader import JsonReader
data=JsonReader().read_json("test_data/role_based_login_flow/role_based_login.json")
search=data['SEARCH']
wrong_login_details=data['WRONG_LOGIN_DETAILS']

@allure.epic("Challenge")
@allure.feature("Role-Based Login Flow")
@allure.story("LF_002 - Invalid credentials")
@allure.description("Enter invalid username/password combination")
@allure.severity(allure.severity_level.CRITICAL)

@pytest.mark.regression
@pytest.mark.order(2)
@pytest.mark.usefixtures("browser_setup")
class TestLF002:


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
        with allure.step("Enter username 'wrongUser' and password 'wrongPass'"):
            login_page.enter_login_details(wrong_login_details["USERNAME"],wrong_login_details["PASSWORD"])
            login_page.click_login_button()

    @allure.title("Verify error message is displayed")
    @pytest.mark.order(3)
    def test_verify_error_message(self,pages):
        common_page = pages["common"]
        with allure.step("Verify alert message for wrong username and password fields"):
            assert_error=common_page.verify_alert_message("Invalid username or password.")
            assert assert_error.is_displayed()

