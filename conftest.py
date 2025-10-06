import os
import pytest
import allure
import config

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.ObjectManager import ObjectManager
from utils.FIleReader import FileReader

# Command-line options
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        help="Browser name is required. Pass --browser_name=chrome or firefox."
    )
    parser.addoption(
        "--executor",
        action="store",
        help="Executor is required. Pass --executor=local or remote."
    )


# Session-scoped driver factory
@pytest.fixture(scope="session")
def driver_factory(request):
    browser_name = request.config.getoption("browser_name") or config.BROWSER
    executor = request.config.getoption("executor") or config.EXECUTOR

    if not browser_name:
        raise pytest.UsageError("Browser name is required. Pass --browser_name=chrome or firefox.")
    if not executor:
        raise pytest.UsageError("Executor is required. Pass --executor=local or remote.")

    browser_name = browser_name.lower()
    executor = executor.lower()
    grid_url = config.GRID_URL

    @allure.step(f"Launching browser: {browser_name} ({executor})")
    def create_driver():
        if executor == "local":
            if browser_name == "chrome":
                options = ChromeOptions()
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--start-maximized")
                driver = webdriver.Chrome(options=options)
            elif browser_name == "firefox":
                options = FirefoxOptions()
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--start-maximized")
                driver = webdriver.Firefox(options=options)
            else:
                raise pytest.UsageError(f"Unsupported browser: {browser_name}")
        elif executor == "remote":
            if browser_name == "chrome":
                options = ChromeOptions()
                options.add_argument("--no-sandbox")
                options.add_argument("--ignore-certificate-errors")
                options.add_argument("--ignore-ssl-errors")
                options.add_argument("--disable-dev-shm-usage")
                driver = webdriver.Remote(command_executor=grid_url, options=options)
            elif browser_name == "firefox":
                options = FirefoxOptions()
                options.add_argument("--no-sandbox")
                options.add_argument("--ignore-certificate-errors")
                options.add_argument("--ignore-ssl-errors")
                options.add_argument("--disable-dev-shm-usage")
                driver = webdriver.Remote(command_executor=grid_url, options=options)
            else:
                raise pytest.UsageError(f"Unsupported browser: {browser_name}")
        else:
            raise pytest.UsageError(f"Unsupported executor: {executor}")

        driver.maximize_window()
        driver.implicitly_wait(int(config.DEFAULT_TIMEOUT))
        driver.get(config.BASE_URL)
        return driver

    yield create_driver  # returns a callable to create new driver per class/need


# Class-scoped browser fixture
@pytest.fixture(scope="class")
def browser_setup(request, driver_factory):
    driver = driver_factory()  # Each class gets its own driver
    object_manager = ObjectManager(driver)
    FileReader().set_env()

    request.cls.driver = driver
    request.cls.objects = object_manager

    yield driver
    if driver:
        driver.quit()


# Page-level fixtures
@pytest.fixture
def pages(request):
    """
    Returns all commonly used page objects as a dictionary.
    """
    return {
        "common": request.cls.objects.common_page,
        "login": request.cls.objects.role_based_login_flow,
        "validation": request.cls.objects.validation_page,
        "job_application": request.cls.objects.job_application_page
    }

# Allure screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item.instance, "driver", None)
        if driver:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"{item.name}_failure",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Could not capture screenshot: {e}")
