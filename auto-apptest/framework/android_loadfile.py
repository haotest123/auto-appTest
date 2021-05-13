from appium import webdriver

import os.path
import yaml
# from selenium import webdriver
from framework.logger import Logger
import os
import time
logger=Logger(logger='appium_desired').getlog()
def appium_desired():
    #  读文件
    with open('../config/android_config.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    base_path = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_path, 'app', data['appname'])
    desired_caps = {}
    desired_caps['app'] = app_path
    desired_caps['platformName'] =data['platformName']  # 设备系统名称
    desired_caps['platformversion']=data['platformVersion']
    desired_caps['deviceName'] =data['deviceName']
    desired_caps['sessionOverride'] =data['sessionOverride']
    desired_caps['noReset'] =data['noReset'] # 不需要每次都安装qpk
    desired_caps['automationName'] =data['automationName']  # 设置V1.5.0以上的appium默认使用UiAutomator2
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    logger.info('======================开始启动APP-todolist==========================')
    #在10秒内等主页面activity出现后，再去页面进行操作
    driver.wait_activity('.LoginActivity',10)

    # ac =driver.current_activity   # 获取当前界面activity
    # print(ac)
    return driver

if __name__ == '__main__':
    appium_desired()

    with open('../config/android_config.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    base_path=os.path.dirname(os.path.dirname(__file__))
    print(os.path.dirname(__file__))
    print(base_path)
    app_path=os.path.join(base_path,'app',data['appname'])
    print(app_path)