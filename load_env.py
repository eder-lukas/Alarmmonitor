from dotenv import load_dotenv
import os

def load_mail():
    load_dotenv("./alarmmonitor.env")
    return os.getenv('EMAIL_ADDRESS').strip()

def load_password():
    load_dotenv("./alarmmonitor.env")
    return os.getenv('EMAIL_PASSWORD').strip()

def load_imap_server_address():
    load_dotenv("./alarmmonitor.env")
    return os.getenv('IMAP_SERVER_ADDRESS').strip()

def load_sender_filter():
    load_dotenv("./alarmmonitor.env")
    return os.getenv('FILTER_EMAIL_SENDER').strip()

def load_subject_filter():
    load_dotenv("./alarmmonitor.env")
    return os.getenv('FILTER_EMAIL_SUBJECT').strip()
