import time

from base.base_driver import init_driver
from page.page import Page


class TestShopCartCache:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_add_shop_cart(self):
        # 在首页判断登录状态，如果没有登录则登录
        self.page.home.login_if_not(self.page)
        # 首页 点击 分类
        self.page.home.click_category()
        # 分类 随机点击 物品列表
        self.page.category.click_goods_list()
        # 物品列表 随机点击 物品详情
        self.page.goods_list.click_goods_detail()
        # 物品详情 点击 加入购物车
        self.page.goods_detail.click_add_shop_cart()

        # 选择所有应该选择的规格
        self.page.goods_detail.choose_spec()
