from PageObjects.base import BasePage
from selenium.webdriver.common.by import By
import time
from framework.logger import Logger


logger=Logger(logger="android_BussinessHomepage").getlog()
class android_BussinessHomepage(BasePage):
#在app页面右上角点击‘+’号，新增一条事务，点击保存按钮，然后长按一条事务点击删除按钮，确定删除后，点击右上角的退出按钮退出该app
    #在app页面右上角点击‘+’号：
    android_BussinessHomepage_button1_loc=(By.ID,'com.example.todolist:id/action_new')
    #在新增页面录入信息，点击保存按钮：
    android_BussinessHomepage_input1_loc=(By.ID,'com.example.todolist:id/toDoItemDetailET')
    android_BussinessHomepage_button2_loc=(By.ID,'com.example.todolist:id/saveBtn')
    #在app页面长按一条事务：
    android_BussinessHomepage_button3_loc=(By.CLASS_NAME,'android.widget.RelativeLayout')
    #长按一条事务后，在弹出的控件中点击编辑按钮：
    android_BussinessHomepage_button4_loc=(By.XPATH,'//*[@text="编辑"]')
    #对事务进行编辑：
    android_BussinessHomepage_input2_loc=(By.CLASS_NAME,'android.widget.EditText')
    #编辑完成后点击保存按钮：
    android_BussinessHomepage_button5_loc=(By.CLASS_NAME,'android.widget.Button')
    #长按一条事务后，在弹出的控件中上滑后点击删除按钮：
    android_BussinessHomepage_button6_loc=(By.XPATH,'//*[@text="删除"]')
    #选择是否删除：1、确定 ；2、取消  ：
    android_BussinessHomepage_button7_loc=(By.ID,'android:id/button1')
    #点击右上角的退出图标后，在点击退出按钮：
    android_BussinessHomepage_button8_loc=(By.CLASS_NAME,'android.widget.ImageButton')
    android_BussinessHomepage_button9_loc=(By.ID,'android:id/title')
    #选择是否确定退出：1、确定 ；2、取消  ：
    # android_BussinessHomepage_button7_loc=(By.ID,'android:id/button1')

    def increase_bussiness(self,increase_information):
        logger.info('在app页面右上角点击‘+’号')
        self.click(*self.android_BussinessHomepage_button1_loc)
        time.sleep(2)
        logger.info('在app页面输入新增的事务内容')
        self.sendkeys(increase_information,*self.android_BussinessHomepage_input1_loc)
        time.sleep(2)
        logger.info('点击保存按钮')
        self.click(*self.android_BussinessHomepage_button2_loc)
        time.sleep(2)

    def edit_bussiness(self,edit_information):
        logger.info('在事务列表页面长按一条事务')
        self.touch_action(*self.android_BussinessHomepage_button3_loc)
        time.sleep(2)
        logger.info('点击编辑按钮')
        self.click(*self.android_BussinessHomepage_button4_loc)
        time.sleep(2)
        self.clear(*self.android_BussinessHomepage_input2_loc)
        logger.info('对事务进行编辑')
        self.sendkeys(edit_information,*self.android_BussinessHomepage_input2_loc)
        time.sleep(2)
        logger.info('点击保存按钮')
        self.click(*self.android_BussinessHomepage_button5_loc)
        time.sleep(2)

    def remove_bussiness(self):
        logger.info('在事务列表页面长按一条事务')
        self.touch_action(*self.android_BussinessHomepage_button3_loc)
        time.sleep(2)
        self.driver.swipe(389,110,389,20,5000)
        time.sleep(2)
        logger.info('点击删除按钮')
        self.click(*self.android_BussinessHomepage_button6_loc)
        time.sleep(2)
        logger.info('点击确定按钮')
        self.click(*self.android_BussinessHomepage_button7_loc)
        time.sleep(2)

    def exit_app(self):
        logger.info('在app页面右上角点击退出图标')
        self.click(*self.android_BussinessHomepage_button8_loc)
        time.sleep(2)
        logger.info('在app页面右上角点击退出按钮')
        self.click(*self.android_BussinessHomepage_button9_loc)
        time.sleep(2)
        logger.info('点击确定按钮')
        self.click(*self.android_BussinessHomepage_button7_loc)
        time.sleep(2)


























