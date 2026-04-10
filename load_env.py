from dotenv import load_dotenv
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = current_dir.strip()
env_dir = current_dir + os.path.sep + "alarmmonitor.env"

def load_mail():
    load_dotenv(env_dir)
    return os.getenv('EMAIL_ADDRESS')

def load_password():
    load_dotenv(env_dir)
    return os.getenv('EMAIL_PASSWORD')

def load_imap_server_address():
    load_dotenv(env_dir)
    return os.getenv('IMAP_SERVER_ADDRESS')

def load_sender_filter():
    load_dotenv(env_dir)
    return os.getenv('FILTER_EMAIL_SENDER')

def load_subject_filter():
    load_dotenv(env_dir)
    return os.getenv('FILTER_EMAIL_SUBJECT')

def load_default_latitude():
    load_dotenv(env_dir)
    return os.getenv('DEFAULT_LATITUDE')

def load_default_longitude():
    load_dotenv(env_dir)
    return os.getenv('DEFAULT_LONGITUDE')

def load_gate_control_active():
    load_dotenv(env_dir)
    return os.getenv('GATE_CONTROL_ACTIVE')