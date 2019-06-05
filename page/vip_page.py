import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class VipPage(BaseAction):

    # 邀请码 输入框
    invite_code_edit_text = By.XPATH, "//input[@type='tel']"

    # 成为会员 按钮
    be_vip_button = By.XPATH, "//input[@value='立即成为会员']"

    # 输入 邀请码
    def input_invite_code(self, value):
        self.input(self.invite_code_edit_text, value)

    # 点击 成为会员
    def click_be_vip(self):
        self.click(self.be_vip_button)


    def is_can_not_be_vip(self, cond, timeout=3, poll=0.1):
        """
        判断 网页的 div 是不是包含 cond 内容
        :param cond:
        :param timeout:
        :param poll:
        :return:
        """

        start_time = time.time()
        end_time = start_time + timeout

        while True:

            if time.time() > end_time:
                print("最终 没有找到")
                return False

            if cond in self.driver.page_source:
                print("找到")
                return True
            else:
                print("正在找，没有找到")

            time.sleep(poll)

