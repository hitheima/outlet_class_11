from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):

    # 登录的用户的特征
    username_feature = By.ID, "com.yunmall.lc:id/tv_user_nikename"

    # 获取 登录的用户名
    def get_username_text(self):
        return self.get_feature_text(self.username_feature)



# ""