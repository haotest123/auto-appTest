from appium import webdriver
from appium.common.exceptions import NoSuchContextException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from framework.logger import Logger



logger=Logger(logger="BasePage").getlog()
class BasePage(object):
    #初始化页面
    def __init__(self,driver):
        self.driver=driver
        # 进行输入内容
     #一个*是元组，两个*是字典
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info('执行成功',loc)
        except:
            logger.error('执行失败%s',(self,loc))

    def sendkeys(self, text, *loc):
        element = self.find_element(*loc)
        try:
            element.send_keys(text)
            logger.info('执行成功')
            # logger.info('执行成功%s',element.text)
            # logger.info('开始进行输入%s',element.text)
        except:
            logger.error('执行失败%s', (self, loc))

    # 清除文本框:
    def clear(self, *loc):
        element = self.find_element(*loc)
        try:
            element.clear()
            logger.info('清除文本框成功')
        except:
            logger.erron('清除元素未找到%s', (self, loc))

    # 点击元素
    def click(self, *loc):
        element = self.find_element(*loc)
        try:
            element.click()
            logger.info('执行成功')
        except  Exception as e:
            logger.error('执行失败', e)

    # 双击元素
    def doubleclick(self, *loc):
        element = self.find_element(*loc)
        try:
            action_chains = ActionChains(self.driver)
            action_chains.double_click(element).perform()
            logger.info('双击正确')
        except Exception as e:
            logger.error('双击失败',e)

    #长按某个元素
    def touch_action(self,*loc):
        element=self.find_element(*loc)
        try:
            TouchAction(self.driver).long_press(element, duration=5).perform()
            logger.info('长按元素成功')
        except Exception as e:
            logger.info('长按元素失败',e)






















