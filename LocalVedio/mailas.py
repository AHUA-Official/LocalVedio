import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP配置信息
SMTP_HOST = 'smtp.qq.com'
SMTP_PORT = 587
SMTP_USERNAME = '3309719563@qq.com'
SMTP_PASSWORD = 'gqedgkpjbfuvdbhd'
SMTP_USE_SSL = False

# 发件人和收件人
SENDER_EMAIL = SMTP_USERNAME
RECIPIENT_EMAIL1 = 'cmkallj@163.com'
RECIPIENT_EMAIL2 = '1877490426@qq.com'
RECIPIENT_EMAIL3 = '3309719563@qq.com'

def send_email(subject, body):
    # 创建邮件内容
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = RECIPIENT_EMAIL1
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # 连接SMTP服务器并发送邮件
    try:
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        if SMTP_USE_SSL:
            server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL1, message.as_string())
        print("邮件发送成功")
    except Exception as e:
        print(f"邮件发送失败: {e}")
    finally:
        server.quit()
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = RECIPIENT_EMAIL2
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # 连接SMTP服务器并发送邮件
    try:
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        if SMTP_USE_SSL:
            server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL2, message.as_string())
        print("邮件发送成功")
    except Exception as e:
        print(f"邮件发送失败: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    subject = input("请输入邮件主题：")
    body = input("请输入邮件内容：")
    send_email(subject, body)
