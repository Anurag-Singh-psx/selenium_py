from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


class ElementActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)
        self.actions = ActionChains(driver)

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def input_text_with_enter(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text.strip()

    def wait_for_element(self, locator):
        wait=WebDriverWait(self.driver,10)
        return wait.until(EC.visibility_of_element_located(locator))

    def presence_of_element_located(self, locator):
        wait=WebDriverWait(self.driver,10)
        return wait.until(EC.presence_of_element_located(locator))

    def get_input_text(self, locator):
        return self.driver.find_element(*locator).get_attribute("value")

    def select_radio_element_by_value(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def select_checkbox_element_by_label(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def perform_keyboard_tab(self):
        self.actions.send_keys(Keys.TAB).perform()

    def perform_sliding(self,locator,value):
        thumb = self.driver.find_element(*locator)
        input_elem = thumb.find_element(By.TAG_NAME, "input")

        # Get slider min, max, current value
        min_val = float(input_elem.get_attribute("min") or 0)
        max_val = float(input_elem.get_attribute("max") or 10)
        current_val = float(input_elem.get_attribute("value") or min_val)

        # Find root to measure width
        slider_root = thumb.find_element(By.XPATH, "./ancestor::span[contains(@class,'MuiSlider-root')]")
        slider_width = slider_root.size['width']

        # Calculate pixel offset            Fraction
        offset = int(slider_width * (value - current_val) / (max_val - min_val))

        # Drag the thumb, not the root
        self.actions.click_and_hold(thumb).move_by_offset(offset, 0).release().perform()
