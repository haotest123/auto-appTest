import os,time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
apk_path=os.path.dirname(os.path.abspath('.'))

desired_caps={}
desired_caps['platformName']='Android'  #设备系统名称
desired_caps['platformversion']='6.0.1'
desired_caps['deviceName']='127.0.0.1：21503'
desired_caps['sessionOverride']=True
desired_caps['noReset']=True   #不需要每次都安装qpk
desired_caps['automationName']='UiAutomator2' #设置V1.5.0以上的appium默认使用UiAutomator2
#apk
desired_caps['appPackage']='com.ss.android.ugc.aweme'
# desired_caps['appActivity']='com.example.todolist.LoginActivity'
desired_caps['app']=apk_path+'auto-apptest\\app\\抖音.apk'
#与appium进行连接，
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(2)

#-----------------------登录抖音账号-----------

# driver.save_screenshot('01.png')
# driver.get_screenshot_as_file('../screenshot')

# xuanfu=driver.find_element_by_class_name('android.widget.TextView')  #未成年人警告悬浮框：我知道了


try:
    # xuanfu = driver.find_element_by_class_name('android.widget.TextView').click()  # 未成年人警告悬浮框：我知道了
    aa=driver.find_element_by_id('com.ss.android.ugc.aweme:id/alz').click()    #我同意
    time.sleep(2)
except NoSuchElementException:
    b = driver.find_element_by_xpath('//*[@text="我"]').click()
    time.sleep(10)
else:
    b = driver.find_element_by_xpath('//*[@text="我"]').click()
    time.sleep(10)







#我

b=driver.find_element_by_xpath('//*[@text="我"]').click()
time.sleep(2)


# #消息
# d=driver.find_element_by_xpath('//*[@text="消息"]').click()
#
# #  +  号
# c=driver.find_element_by_id('com.ss.android.ugc.aweme:id/giy')
#
# #朋友
# e=driver.find_element_by_xpath('//*[@text="朋友"]').click()
#
# #首页
# f=driver.find_element_by_xpath('//*[@text="首页"]').click()


















