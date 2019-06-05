import time

from base.base_driver import init_driver
from page.page import Page


class TestVip:


    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_vip(self):
        # 在首页判断登录状态，如果没有登录则登录
        self.page.home.login_if_not(self.page)
        # 我 点击 加入vip
        self.page.me.click_vip()
        print(self.driver.contexts)
        # 切换到对应的 webview
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        # vip 输入 邀请码
        self.page.vip.input_invite_code("hello")
        # vip 点击 成为vip
        self.page.vip.click_be_vip()


        assert self.is_can_not_be_vip("邀请码输入不正确")

        # 切换到原生的环境
        self.driver.switch_to.context("NATIVE_APP")



    def is_can_not_be_vip(self, cond):
        while True:
            if cond in self.driver.page_source:
                return True
