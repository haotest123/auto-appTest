import HTMLTestRunner
import unittest
from Log_SendMail import SendEmail
import warnings
import datetime
import os



report_path=os.path.dirname(os.path.abspath('.'))+ '/test_report/'

nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
HtmlFile = report_path+'result.html'
fp=open(HtmlFile,'wb')
# test_dir='./'
#加载所有以test开头的.py文件
suite=unittest.TestLoader().discover('android_autotest',pattern='test*.py')


if __name__=='__main__':
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'APP自动化测试报告，测试结果如下',description=u'功能用例测试情况如下')
    runner.run(suite)
    fp.close()
    # warnings.simplefilter('ignore', ResourceWarning)
    # s = SendEmail()
    # s.send_mail(['2804160559@qq.com'], "安勇--自动化测试邮件", "App自动化测试报告，详情请见附件~")


