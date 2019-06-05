from base.base_driver import init_driver
from page.page import Page


class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_add_address(self):
        # 在首页判断登录状态，如果没有登录则登录
        self.page.home.login_if_not(self.page)
        # 我 点击 设置
        self.page.me.click_setting()
        # 设置 点击 地址管理
        self.page.setting.click_address_list()
        # 地址列表 点击 新增地址
        self.page.address_list.click_add_address()
        # 新增地址 输入 收件人
        self.page.edit_address.input_name("hello")
        # 新增地址 输入 手机号
        self.page.edit_address.input_phone("18888888888")
        # 新增地址 输入 详细地址
        self.page.edit_address.input_info("二单元 402")
        # 新增地址 输入 邮编
        self.page.edit_address.input_postal_code("100000")
        # 新增地址 点击 设为默认地址
        self.page.edit_address.click_default_address()