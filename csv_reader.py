import csv
from log import logger
from email.mime.text import MIMEText

title = "[테스트] 서버 데이터 현황"


def create_mailing_list_from_csv(sender, file_name):
    logger.info("creating mailing list from csv file: %s", file_name)
    email_msgs = []

    f = open(file_name, 'r')
    reader = csv.DictReader(f)
    for row in reader:
        # get information off of csv
        # name, email, server-name, cpu-usage, mem-usage

        receiver = row['email']
        message = MIMEText(_text=create_mail_body(row), _charset="utf-8")  # 메일 내용

        message['Subject'] = title  # 메일 제목
        message['From'] = sender  # 송신자
        message['To'] = receiver  # 수신자

        email_msgs.append(message)

    return email_msgs


def create_mail_body(csv_row):
    sample_file = open('sample.txt', 'r')
    lines = sample_file.readlines()

    name = csv_row['name']
    server_name = csv_row['server-name']
    cpu_usage = csv_row['cpu-usage']
    mem_usage = csv_row['mem-usage']

    mail_body = ""
    for line in lines:
        text = line
        text = text.replace("<name>", name or "")
        text = text.replace("<server-name>", server_name or "")
        text = text.replace("<cpu-usage>", cpu_usage + "% " or 0)
        text = text.replace("<mem-usage>", mem_usage + "% " or 0)

        mail_body += text

    return mail_body
