import smtplib
import csv
from email.mime.text import MIMEText
import getpass

sender = input('Sender Email Address : ')
password = getpass.getpass('Password : ')

smtp_info = dict({"smtp_server" : "smtp.naver.com", # SMTP 서버 주소
                  "smtp_user_id" : sender,          # sender mail address
                  "smtp_user_pw" : password ,       # sender mail password
                  "smtp_port" : 587})               # SMTP 서버 포트

csv_file = "sample.csv"


# send mail                  
def send_email(smtp_info, msg_list):
    with smtplib.SMTP(smtp_info["smtp_server"], smtp_info["smtp_port"]) as server:
        # TLS 보안 연결
        server.starttls() 
        # 로그인
        server.login(smtp_info["smtp_user_id"], smtp_info["smtp_user_pw"])

        for msg in msg_list:
            # 로그인 된 서버에 이메일 전송(메시지를 보낼때는 .as_string() 메소드를 사용해서 문자열로 바꿔줍니다.)
            response = server.sendmail(msg['from'], msg['to'], msg.as_string())

            # 이메일을 성공적으로 보내면 결과는 {}
            if not response:
                print(msg['to'] + ' 에게 이메일을 성공적으로 보냈습니다.')
            else:
                print(response)

# create mailing list from csv file
def create_mailing_list_from_csv(file_name) : 
       
    msg_list = []

    f = open(file_name, 'r')
    reader = csv.DictReader(f)
    for row in reader:
        # get email info off of csv
        title   = row['title']
        content = row['content']
        receiver= row['mail']

        msg = MIMEText(_text = content, _charset = "utf-8") # 메일 내용

        msg['Subject'] = title     # 메일 제목
        msg['From'] = sender       # 송신자
        msg['To'] = receiver       # 수신자

        msg_list.append(msg)

    return msg_list
                
## main logic

msg_list = create_mailing_list_from_csv(csv_file)
send_email(smtp_info, msg_list )

