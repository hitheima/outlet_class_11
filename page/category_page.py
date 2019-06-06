import random

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class CategoryPage(BaseAction):

    # 分类中的进入物品列表的特征
    goods_list_button = By.ID, "com.yunmall.lc:id/iv_img"

    # 随机点击一个物品的分类，进入物品的列表
    def click_goods_list(self):
        buttons = self.find_elements(self.goods_list_button)
        button_index = random.randint(0, len(buttons) - 1)
        buttons[button_index].click()
