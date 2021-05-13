from appium import webdriver

import unittest
import time
from framework.android_loadfile import appium_desired
import os
import warnings

class base_testcase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.driver=appium_desired()

        # apk_path = os.path.dirname(os.path.abspath('D:\\'))
        # desired_caps = {}
        # desired_caps['platformName'] = 'Android'  # 设备系统名称
        # desired_caps['platformversion'] = '6.0.1'
        # desired_caps['deviceName'] = '127.0.0.1：21503'
        # desired_caps['sessionOverride'] = True
        # desired_caps['noReset'] = True  # 不需要每次都安装apk
        # desired_caps['automationName'] = 'UiAutomator2'  # 设置V1.5.0以上的appium默认使用UiAutomator2
        # desired_caps['appPackage']='com.example.todolist'
        # desired_caps['appActivity']='com.example.todolist.LoginActivity'
        # desired_caps['app'] = apk_path + 'software\\adt-bundle-windows\\sdk\\build-tools\\android-4.4W\\todolist.apk'
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        time.sleep(5)
        # self.driver.close_app()













