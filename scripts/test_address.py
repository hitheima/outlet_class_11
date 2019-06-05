from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page

import pytest

class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("args", analyze_data("address_data", "test_add_address"))
    def test_add_address(self, args):
        name = args["name"]
        phone = args["phone"]
        info = args["info"]
        postal_code = args["postal_code"]
        toast = args["toast"]

        # 在首页判断登录状态，如果没有登录则登录
        self.page.home.login_if_not(self.page)
        # 我 点击 设置
        self.page.me.click_setting()
        # 设置 点击 地址管理
        self.page.setting.click_address_list()
        # 地址列表 点击 新增地址
        self.page.address_list.click_add_address()
        # 新增地址 输入 收件人
        self.page.edit_address.input_name(name)
        # 新增地址 输入 手机号
        self.page.edit_address.input_phone(phone)
        # 新增地址 输入 详细地址
        self.page.edit_address.input_info(info)
        # 新增地址 输入 邮编
        self.page.edit_address.input_postal_code(postal_code)
        # 新增地址 点击 设为默认地址
        self.page.edit_address.click_default_address()
        # 新增地址 选择区域
        self.page.edit_address.choose_region()
        # 新增地址 点击 保存
        self.page.edit_address.click_save()

        if toast is None:
            # 格式：姓名 + 2个空格 + 电话
            assert self.page.address_list.get_receipt_name_text() == "%s  %s" % (name, phone)
        else:
            assert self.page.edit_address.is_toast_exist(toast)

