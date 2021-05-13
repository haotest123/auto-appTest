import os,time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
apk_path=os.path.dirname(os.path.abspath('.'))

desired_caps={}
desired_caps['platformName']='Android'  #设备系统名称
# desired_caps['platformversion']='6.0.1'
desired_caps['platformversion']='7.1.2'       # adb shell getprop ro.build.version.release
desired_caps['deviceName']='127.0.0.1：21503'
desired_caps['sessionOverride']=True
desired_caps['noReset']=True   #不需要每次都安装qpk
desired_caps['automationName']='UiAutomator2' #设置V1.5.0以上的appium默认使用UiAutomator2
#apk
desired_caps['appPackage']='com.example.todolist'
desired_caps['appActivity']='com.example.todolist.LoginActivity'

desired_caps['app']=apk_path+'software\\adt-bundle-windows\\sdk\\build-tools\\android-4.4W\\todolist.apk'  #apk包的安装路径
#与appium进行连接，
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)   #启动app

# ==========================================登录页面=======================
#输入用户名密码，点击登录按钮
driver.find_element_by_id('com.example.todolist:id/nameET').send_keys('1')
driver.find_element_by_id('com.example.todolist:id/passwordET').send_keys('1')
driver.find_element_by_id('com.example.todolist:id/loginBtn').click()
time.sleep(2)

# =================点击右上角‘+’ 号，添加事项，输入完事项内容后，点击保存按钮================================
driver.find_element_by_id('com.example.todolist:id/action_new').click()
time.sleep(2)
driver.find_element_by_id('com.example.todolist:id/toDoItemDetailET').send_keys('自动化测试添加事务')
time.sleep(2)
driver.find_element_by_id('com.example.todolist:id/saveBtn').click()
time.sleep(2)
#===================长按一条事务进行删除========================================================
#长按方法：
a=driver.find_element_by_class_name('android.widget.RelativeLayout')
TouchAction(driver).long_press(a,duration=5).perform()
time.sleep(2)
# c=driver.find_element_by_xpath('//*[@text="编辑"]')
# loc=c.location   #获取开始滑动元素的坐标 
# print(loc)
driver.swipe(389,110,389,0,5000)
time.sleep(2)
b=driver.find_element_by_xpath('//*[@text="删除"]').click()
time.sleep(2)
c=driver.find_element_by_id('android:id/button1').click()
time.sleep(2)
#===================点击一条事务进行编辑========================================================
e=driver.find_element_by_class_name('android.widget.RelativeLayout')
TouchAction(driver).long_press(e,duration=5).perform()
time.sleep(2)
d=driver.find_element_by_xpath('//*[@text="编辑"]').click()
time.sleep(2)
f=driver.find_element_by_class_name('android.widget.EditText').clear()
time.sleep(2)
f.send_keys('对事物进行编辑')
time.sleep(2)
g=driver.find_element_by_class_name('android.widget.Button').click()
time.sleep(2)

#==================点击退出图标，退出此系统==========================================
h=driver.find_element_by_class_name('android.widget.ImageButton').click()
time.sleep(2)
j=driver.find_element_by_id('android:id/title').click()
time.sleep(2)
k=driver.find_element_by_id('android:id/button1').click()
time.sleep(10)

