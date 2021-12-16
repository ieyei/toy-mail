import smtplib
import csv_reader as csv
from log import logger
from email.mime.text import MIMEText
import getpass

sender = input('Sender Email Address : ')
password = getpass.getpass('Password : ')

smtp_info = dict({"smtp_server": "smtp.naver.com",  # SMTP 서버 주소
                  "smtp_user_id": sender,  # sender mail address
                  "smtp_user_pw": password,  # sender mail password
                  "smtp_port": 587})  # SMTP 서버 포트

csv_file = "sample.csv"


# send emails
def send_email(msgs):
    with smtplib.SMTP(smtp_info["smtp_server"], smtp_info["smtp_port"]) as server:
        logger.info("getting credential for login")
        # TLS 보안 연결
        server.starttls()
        # 로그인
        server.login(smtp_info["smtp_user_id"], smtp_info["smtp_user_pw"])
        logger.info("login succeeded")

        for msg in msgs:
            # 로그인 된 서버에 이메일 전송(메시지를 보낼때는 .as_string() 메소드를 사용해서 문자열로 바꿔줍니다.)
            response = server.sendmail(msg['from'], msg['to'], msg.as_string())

            # 이메일을 성공적으로 보내면 결과는 {}
            if not response:
                print(msg['to'] + ' 에게 이메일을 성공적으로 보냈습니다.')
            else:
                print(response)


# main logic
msg_list = csv.create_mailing_list_from_csv(sender, csv_file)
send_email(msg_list)
