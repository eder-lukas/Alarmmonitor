from mail_client.mail import Mail
from mail_client.get_mails import get_unseen_mails
from gui.app import App
import time
import threading

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
        mails = get_unseen_mails()
        for mail in mails: 
            print("-----------------------------------")
            print("Sender:", mail.sender)
            print("Betreff:", mail.subject)
            print("Inhalt:", mail.content)
            print("-----------------------------------")
            if ("@fitt-gmbh.de" in mail.sender):
                app.update_content(mail.parse_content())
        time.sleep(10)  # Warten Sie 10 Sekunden, bevor Sie erneut überprüfen

main()


#namenskonvention