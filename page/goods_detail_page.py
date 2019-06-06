from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class GoodsDetailPage(BaseAction):

    # 加入购物车 按钮
    add_shop_cart_button = By.XPATH, "//*[@text='加入购物车']"

    # 点击 加入购物车
    def click_add_shop_cart(self):
        self.click(self.add_shop_cart_button)