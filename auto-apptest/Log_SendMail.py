#coding:utf-8
import smtplib
import os.path
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import warnings

class SendEmail:
    global send_user
    global email_host
    global password
    password = "jcdfxlfyhwypddgb"
    email_host = "smtp.qq.com"
    send_user = "2804160559@qq.com"

    def send_mail(self,user_list,sub,content):
        user = "2804160559" + "<" + send_user + ">"

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        # 邮件正文内容
        message.attach(MIMEText(content, 'plain', 'utf-8'))
        log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
        log_path1 = os.path.dirname(os.path.abspath('.')) + '/test_report/result.html'
        #log_path=os.path.abspath(os.path.dirname(__file__)).split('newPython')[0] + 'newPython/logs/'
        log_name = os.path.join(log_path,'%s.log'%time.strftime('%Y-%m-%d'))

        # 构造附件（附件为txt格式的文本）
        att = MIMEText(open(log_name ,'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename=%s.txt'%time.strftime('%Y_%m_%d')
        # 构造附件（附件为html格式的文本）
        att1 = MIMEText(open(log_path1, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Disposition"] = 'attachment; filename=%s.html' % time.strftime('%Y_%m_%d')

        #发送txt测试文本日志和html测试结果文件
        message.attach(att)
        message.attach(att1)
        server=smtplib.SMTP_SSL(email_host)
        server.connect(email_host,465)# 启用SSL发信, 端口一般是465
        # server.set_debuglevel(1)# 打印出和SMTP服务器交互的所有信息
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()

        # warnings.simplefilter('ignore', ResourceWarning)
        # s = SendEmail()
        # s.send_mail('2804160559@qq.com', "安勇--自动化测试邮件", "App自动化测试报告，详情请见附件~")




# #coding:utf-8
# import imaplib
# import smtplib
# from email.mime.text import MIMEText
#
# class SendEmail:
#     global send_user
#     global email_host
#     global password
#     password = "jcdfxlfyhwypddgb"
#     email_host = "smtp.qq.com"
#     send_user = "2804160559@qq.com"
#
#     def send_mail(self,user_list,sub,content):
#         user = "MC小勇测试" + "<" + send_user + ">"
#         message = MIMEText(content,_subtype='plain',_charset='utf-8')
#         message['Subject'] = sub
#         message['From'] = user
#         message['To'] = ";".join(user_list)
#         server =smtplib.SMTP_SSL(email_host)
#         server.connect(email_host,465)
#         server.login(send_user,password)
#         server.sendmail(user,user_list,message.as_string())
#         server.close()
#
# if __name__ == '__main__':
#     send = SendEmail()
#     user_list = ['2804160559@qq.com']
#     # user_list = ['shuyali@jingyougroup.com']
#     sub = "测试邮件"
#     content = "山楂树之恋"
#     send.send_mail(user_list,sub,content)


