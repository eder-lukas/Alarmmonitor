from dotenv import load_dotenv
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = current_dir.strip()

def load_mail():
    load_dotenv(current_dir + os.path.sep + "alarmmonitor.env")
    return os.getenv('EMAIL_ADDRESS')

def load_password():
    load_dotenv(current_dir + os.path.sep + "alarmmonitor.env")
    return os.getenv('EMAIL_PASSWORD')

def load_imap_server_address():
    load_dotenv(current_dir + os.path.sep + "alarmmonitor.env")
    return os.getenv('IMAP_SERVER_ADDRESS')

def load_sender_filter():
    load_dotenv(current_dir + os.path.sep + "alarmmonitor.env")
    return os.getenv('FILTER_EMAIL_SENDER')

def load_subject_filter():
    load_dotenv(current_dir + os.path.sep + "alarmmonitor.env")
    return os.getenv('FILTER_EMAIL_SUBJECT')

def load_default_latitude():
    load_dotenv(current_dir + os.path.sep + "alarmmonitor.env")
    return os.getenv('DEFAULT_LATITUDE')

def load_default_longitude():
    load_dotenv(current_dir + os.path.sep + "alarmmonitor.env")
    return os.getenv('DEFAULT_LONGITUDE')