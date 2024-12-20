from mail_client.mail import Mail
from mail_client.get_mails import get_mails_from_server
from load_env import load_sender_filter, load_subject_filter
from gui.app import App
import time
import threading
from logger import logger

gui_thread = None
app = None

def main():
    # Start Gui Thread
    if __name__ == "__main__":
        app = App()
        gui_thread = threading.Thread(target=app.start_application)
        gui_thread.start()
        time.sleep(2) # Wait for GUI to start -> to avoid problems accessing app's attributes

    while True:
        mails = get_mails_from_server()

        if mails:
            for mail in mails: 
                print_mail_info(mail)
                if (load_subject_filter() in mail.subject and load_sender_filter() in mail.sender):
                    content = mail.parse_content()
                    app.update_content(content)

        if (gui_thread.is_alive()): # when gui is closed, kill the whole program
            time.sleep(10)
        else:
            logger.info("Programm wird beendet, weil GUI beendet wurde.")
            exit(1)


def print_mail_info(mail):
    logger.info("-----------------------------------")
    logger.info("Neue Mail empfangen")
    logger.info("-----------------------------------")
    logger.info(f"Betreff: {mail.subject}")
    logger.info("-----------------------------------")


main()
