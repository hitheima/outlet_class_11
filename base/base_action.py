from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1.0):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*feature))

    def find_elements(self, feature, timeout=10, poll=1.0):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*feature))

    def click(self, feature):
        self.find_element(feature).click()

    def clear(self, feature):
        self.find_element(feature).clear()

    def input(self, feature, value):
        self.clear(feature)
        self.find_element(feature).send_keys(value)

    def get_feature_text(self, feature):
        return self.find_element(feature).text

    def is_toast_exist(self, message):
        """
        判断 界面上是否有 toast 的内容包含 message
        :param message: toast的部分信息
        :return:
        """
        toast_feature = By.XPATH, "//*[contains(@text, '%s')]" % message
        try:
            self.find_element(toast_feature, 5, 0.1)
            return True
        except TimeoutException:
            return False

    def get_toast_text(self, message):
        """
        根据 toast 的部分的 message 消息，获取所有的toast内容
        :param message: toast的部分信息
        :return:
        """
        if self.is_toast_exist(message):
            toast_feature = By.XPATH, "//*[contains(@text, '%s')]" % message
            return self.find_element(toast_feature, 5, 0.1).text
        else:
            raise Exception("没有找到 对应的toast")
