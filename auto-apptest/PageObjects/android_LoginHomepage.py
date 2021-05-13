from PageObjects.base import BasePage
from selenium.webdriver.common.by import By
import time
from framework.logger import Logger


logger=Logger(logger="android_LoginHomepage").getlog()

class android_LoginHomepage(BasePage):
#==============app首页页面输入用户名和密码，点击登录按钮进行登录========================
    #输入账号：
    android_LoginHomepage_input1_loc=(By.ID,'com.example.todolist:id/nameET')
    #输入密码：
    android_LoginHomepage_input2_loc=(By.ID,'com.example.todolist:id/passwordET')
    #点击登录按钮：
    android_LoginHomepage_button_loc=(By.ID,'com.example.todolist:id/loginBtn')

    def shouye_login(self,account,password):
        time.sleep(5)
        logger.info('在APP登录页面输入用户名')
        self.sendkeys(account,*self.android_LoginHomepage_input1_loc)
        time.sleep(2)
        logger.info('在APP登录页面输入密码')
        self.sendkeys(password,*self.android_LoginHomepage_input2_loc)
        time.sleep(2)
        logger.info('在APP登录页面点击登录按钮')
        self.click(*self.android_LoginHomepage_button_loc)






