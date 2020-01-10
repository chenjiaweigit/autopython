# coding: utf-8
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def bbbbb():
    msg_from = '704723194@qq.com'  # 发送方邮箱
    passwd = 'iziowisravhlbfde'  # 填入发送方邮箱的授权码
    msg_to = 'wangbin@winchannel.net'  # 收件人邮箱

    subject = "python邮件测试"  # 主题
    # content = "这是我使用python smtplib及email模块发送的邮件"
    # msg = MIMEText(content)
    msg =MIMEText()
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    testfile = open(r'E:\banben.txt', 'r')
    result = testfile.readline()
    if result:
        part = MIMEText("自动化测试失败,具体请看测试的日志")
        msg.attach(part)
        part = MIMEApplication(open(r'E:\banben.txt', 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename="**.doc")
        msg.attach(part)
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print(1)


# def aaaaa():
#     message ='''
#     hello，world！
#     来自我的电脑
#     '''
#     msg = MIMEText(message, 'plain', 'utf-8')
#     msg['Subject'] = Header("来自Python的邮件", 'utf-8')
#     msg['From'] = Header('704723194@qq.com')
#     msg['To'] = Header('wangbin@winchannel.net', 'utf-8')
#     from_addr = '704723194@qq.com'  # 发件邮箱
#     password = 'aa248163'  # 邮箱密码
#     to_addr = 'wangbin@winchannel.net'  # 收件邮箱
#     smtp_server = 'smtp.qq.com'
#     try:
#         server = smtplib.SMTP(smtp_server,465)  # 第二个参数为默认端口为25，有些邮件有特殊端口
#         print('开始登录')
#         server.login(from_addr, password)  # 登录邮箱
#         print('登录成功')
#         print("邮件开始发送")
#         server.sendmail(from_addr, to_addr, msg.as_string())  # 将msg转化成string发出
#         server.quit()
#         print("邮件发送成功")
#     except smtplib.SMTPException as e:
#         print("邮件发送失败", e)






if __name__ == '__main__':
    bbbbb()