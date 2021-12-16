import csv
import logging
from email.mime.text import MIMEText

# settin up logger
# FIXME try creating global logger file
def setup_logger():
    # create logger
    logger = logging.getLogger('toy-mail')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    return logger

def create_mailing_list_from_csv(file_name) :    
    logger.info("creating mailing list from csv file: %s", file_name)
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

    print("length of mailing list : ",len(msg_list))
    return msg_list

file_name = "sample.csv"
logger = setup_logger()

sender = input('Sender Email Address : ')
msg_list = create_mailing_list_from_csv(file_name)

for msg in msg_list:
    logger.info("from: %s, to: %s", msg['from'],msg['to'])
