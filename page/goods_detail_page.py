from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class GoodsDetailPage(BaseAction):

    # 加入购物车 按钮
    add_shop_cart_button = By.XPATH, "//*[@text='加入购物车']"

    # 确认 按钮
    commit_button = By.XPATH, "//*[@text='确认']"

    # 点击 加入购物车
    def click_add_shop_cart(self):
        self.click(self.add_shop_cart_button)

    # 点击 确认
    def click_commit(self):
        self.click(self.commit_button)

    def get_spec_name(self):
        return self.get_toast_text("请选择").split(" ")[1]

    def choose_spec(self):
        while True:
            # 点击 确认
            self.click_commit()

            # 有没有 "请选择" 的 toast ，如果有，应该选择对应的规格，如果没有，加入成功
            if self.is_toast_exist("请选择"):
                feature = By.XPATH, "//*[@text='%s']/../*[2]/*[1]" % self.get_spec_name()
                self.click(feature)
            else:
                break