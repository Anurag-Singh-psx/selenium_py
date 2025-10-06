# Role-Based Login Flow Automation Framework

Overview:
This is a Selenium + Python + Pytest automation framework for validating role-based login flows.

Features:

* Page Object Model (POM) for maintainable page abstractions.
* Pytest for test execution.
* Allure Reports for detailed reporting.
* Selenium Grid via Docker for parallel cross-browser execution.
* JSON-driven test data for easy maintenance.

Project Structure:

pages/                       # Page Object Model classes

* BaseClass.py
* ElementActions.py
* CommonPage.py
* ValidationPage.py
* role_based_login_flow/
  * role_based_login_flow_page.py

tests/                       # Pytest test classes

* test_LF_001_empty_fields.py
* test_LF_002_invalid_login.py
* test_LF_003_user_login.py
* test_LF_004_admin_login.py
* test_LF_005_logout.py

utils/                       # Utility classes

* JsonReader.py
* FIleReader.py

test_data/                   # JSON test data

* role_based_login_flow/LF_001.json

conftest.py                  # Fixtures & driver setup
docker-compose.yml           # Selenium Grid setup
requirements.txt             # Python dependencies
README.txt                   # This readme file

---

Prerequisites / Things to Install:

1. Install Python 3.9 or higher: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Install Google Chrome and/or Firefox browsers.
3. Install Docker & Docker Compose: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
4. Install Python dependencies:

```bash 
  pip install -r requirements.txt
```

`requirements.txt` includes:

```
selenium
pytest
pytest-xdist
pytest-order
allure-pytest
openpyxl
python-dotenv
```

---

Selenium Grid Setup:

* Start grid:
  docker-compose up -d
* Hub URL: [http://localhost:4444](http://localhost:4444)
* Chrome & Firefox nodes ready
* shm_size: 2gb ensures stable browser execution

Running Tests:

Local Execution:
pytest --browser_name=chrome --executor=local --alluredir=allure-results

Parallel Execution:
pytest -n 4 --dist=loadscope --browser_name=chrome --executor=local --alluredir=allure-results

* -n 4: number of parallel workers
* --dist=loadscope: ensures all test methods in the same class run in the same worker

Fixtures:

* browser_setup (class): Initializes WebDriver & ObjectManager.
* driver (function): Creates browser instance (parallel execution).
* objects (function): Returns ObjectManager instance for page objects.
* common_page (function): Returns CommonPage object.
* login_page (function): Returns LoginFlowPage object.
* validation_page (function): Returns ValidationPage object.

Test Data:
Example JSON in test_data/role_based_login_flow/LF_001.json:
{
"ADMIN": {"USERNAME": "admin", "PASSWORD": "admin123"},
"USER": {"USERNAME": "user", "PASSWORD": "user123"},
"SEARCH": {"SEARCH_CHALLENGE": "Role-Based Login Flow"},
"WRONG_LOGIN_DETAILS": {"USERNAME": "adminsample", "PASSWORD": "adminsample"}
}

Allure Reporting:

* After running tests:
  allure serve allure-results
* Includes step-by-step logs, screenshots on failure, environment info.

Best Practices:

* Keep class-scoped browser fixtures for state-dependent tests.
* Use --dist=loadscope for parallel execution.
* Use @pytest.mark.order to enforce method sequence in classes.
* Keep test data JSON-driven for easy maintenance.
* Use ElementActions for Selenium interactions to reduce flakiness.

Troubleshooting:

* Browser crashes in Docker: Increase shm_size in docker-compose.yml.
* Parallel test failures: Ensure --dist=loadscope is used.
* Screenshots not attached: Check driver availability in test instance at failure.

Summary:

* Supports role-based login testing for Admin/User scenarios.
* Works with local and remote execution (Selenium Grid).
* Fully compatible with parallel execution.
* Generates Allure reports with screenshots and environment info.
