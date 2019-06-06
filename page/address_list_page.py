from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):

    # 新增地址 按钮
    add_address_button = By.ID, "com.yunmall.lc:id/address_add_new_btn"

    # 地址的 收件人和电话组成的标题 的特征
    receipt_name_text_view = By.ID, "com.yunmall.lc:id/receipt_name"

    # 默认 标记
    default_address_tag = By.ID, "com.yunmall.lc:id/address_is_default"

    # 点击 新增地址
    def click_add_address(self):
        self.find_element_with_scroll(self.add_address_button).click()

    # 获取 地址的 收件人和电话组成的标题 的文字内容
    # 使用的是 find_element 的方法，第一个也就是默认的地址的信息
    def get_receipt_name_text(self):
        return self.get_feature_text(self.receipt_name_text_view)

    # 默认标记是否存在
    def is_default_address_tag_exist(self):
        return self.is_feature_exist(self.default_address_tag)

    # 点击 默认标记
    def click_default_address(self):
        self.click(self.default_address_tag)
