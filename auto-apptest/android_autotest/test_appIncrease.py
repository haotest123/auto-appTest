
from android_autotest.base_testcase import base_testcase
from PageObjects.android_BussinessHomepage import android_BussinessHomepage
from PageObjects.android_LoginHomepage import android_LoginHomepage
from framework.logger import Logger

logger=Logger(logger="appIncrease").getlog()

class appIncrease(base_testcase):
    def test_appIncrease(self):
        logger.info('--------------APP自动化测试登录场景开始执行----------------------')
        # 在app登陆页面输入用户名和密码后，点击登录按钮进行登录
        app_Login = android_LoginHomepage(self.driver)
        app_Login.shouye_login('1', '1')

        logger.info('-------------------APP自动化测试新增事务场景开始执行-----------------------')
    # 登录进入app页面后，在页面右上角点击‘+’号，新增页面录入完成信息后，点击保存按钮，然后在页面右上角的退出图标后，点击退出按钮，退出app：
        appIncrease=android_BussinessHomepage(self.driver)
        appIncrease.increase_bussiness('新增加的事务')

        logger.info('-------------------APP自动化测试编辑事务场景开始执行-------------------')
        # 登录进入app页面后，事务列表中长按一条事务后，在弹出的控件中点击编辑按钮，弹出的页面中编辑完成后点击保存按钮，然后在页面右上角的退出图标后，点击退出按钮，退出app：
        appCompile = android_BussinessHomepage(self.driver)
        appCompile.edit_bussiness('编辑新事务')

        logger.info('--------------------APP自动化测试删除事务场景开始执行--------------------')
        # 登录进入app页面后，事务列表中长按一条事务后，在弹出的控件中点击删除按钮，删除完成后在页面右上角的退出图标后，点击退出按钮，退出app：
        appRemove = android_BussinessHomepage(self.driver)
        appRemove.remove_bussiness()

        logger.info('--------------------APP自动化测试退出场景开始执行-------------------')
        appExit=android_BussinessHomepage(self.driver)
        appExit.exit_app()

