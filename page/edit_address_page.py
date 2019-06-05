from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class EditAddressPage(BaseAction):

    # 收件人 输入框
    name_edit_text = By.ID, "com.yunmall.lc:id/address_receipt_name"

    # 手机号 输入框
    phone_edit_text = By.ID, "com.yunmall.lc:id/address_add_phone"

    # 详细地址 输入框
    info_edit_text = By.ID, "com.yunmall.lc:id/address_detail_addr_info"

    # 邮编 输入框
    postal_code_edit_text = By.ID, "com.yunmall.lc:id/address_post_code"

    # 设为默认地址 按钮
    default_address_button = By.ID, "com.yunmall.lc:id/address_default"

    # 输入 收件人
    def input_name(self, value):
        self.input(self.name_edit_text, value)

    # 输入 手机号
    def input_phone(self, value):
        self.input(self.phone_edit_text, value)

    # 输入 详细地址
    def input_info(self, value):
        self.input(self.info_edit_text, value)

    # 输入 邮编
    def input_postal_code(self, value):
        self.input(self.postal_code_edit_text, value)

    # 点击 设为默认地址
    def click_default_address(self):
        self.click(self.default_address_button)