from time import sleep

import allure
import pytest

from utils.JsonReader import JsonReader
data=JsonReader().read_json("test_data/role_based_login_flow/role_based_login.json")
search=data['SEARCH']

@allure.epic("Challenge")
@allure.feature("Role-Based Login Flow")
@allure.story("LF_001 - Empty fields validation")
@allure.description("Attempt login with empty username and password")
@allure.severity(allure.severity_level.CRITICAL)

@pytest.mark.regression
@pytest.mark.order(1)
@pytest.mark.usefixtures("browser_setup")
class TestLF001:

    # def setup_method(self):
    #     self.common_page = self.objects.common_page
    #     self.login_page = self.objects.role_based_login_flow

    @allure.title("Navigate to login page")
    @pytest.mark.order(1)
    def test_navigate_to_login_page(self,pages):
        common_page = pages["common"]
        with allure.step(f"Search for {search['SEARCH_CHALLENGE']} and click on View Challenge button"):
            common_page.search_and_view_challenge(search['SEARCH_CHALLENGE'])

    @allure.title("Click on login button")
    @pytest.mark.order(2)
    def test_click_on_login(self,pages):
        login_page = pages["login"]
        with allure.step("Leave username and password empty then click on login button"):
            login_page.click_login_button()

    @allure.title("Verify error message is displayed")
    @pytest.mark.order(3)
    def test_verify_error_message(self,pages):
        common_page = pages["common"]
        with allure.step("Verify alert message for empty fields"):
            assert_error=common_page.verify_alert_message("Both fields are required.")
            assert assert_error.is_displayed()

