from pages.ElementActions import ElementActions


class BaseClass:
    def __init__(self,driver):
        self.driver = driver
        self.element_actions=ElementActions(driver)