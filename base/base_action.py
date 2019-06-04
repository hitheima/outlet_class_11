from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*feature))

    def find_elements(self, feature, timeout=10, poll=1):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*feature))

    def click(self, feature):
        self.find_element(feature).click()

    def clear(self, feature):
        self.find_element(feature).clear()

    def input(self, feature, value):
        self.clear(feature)
        self.find_element(feature).send_keys(value)