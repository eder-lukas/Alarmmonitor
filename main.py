from mail_client.mail import Mail
from mail_client.get_mails import get_unseen_mails
from load_env import load_sender_filter, load_subject_filter
from gui.app import App
from datetime import datetime
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

    connection_established = None # variable to store connection status to avoid fleeding the log file
    while True:
        mails = None
        try: # get mails in try except -> otherwise program will crash when the internet connection is interrupted
            mails = get_unseen_mails()
            if connection_established == None or connection_established == False:
                print("Connected to Internet on " + datetime.now().strftime("%d.%m.%Y at %H:%M:%S"))
                connection_established = True
        except:
            if connection_established == None or connection_established == True:
                print("Lost Internet Connection on " + datetime.now().strftime("%d.%m.%Y at %H:%M:%S"))
                connection_established = False
            

        if mails:
            for mail in mails: 
                print()
                print("-----------------------------------")
                print("Neue Mail empfangen:")
                print("-----------------------------------")
                print("Sender:", mail.sender)
                print("Betreff:", mail.subject)
                print("Inhalt:", mail.content)
                print("-----------------------------------")
                print()
                if (load_subject_filter() in mail.subject and load_sender_filter() in mail.sender):
                    app.update_content(mail.parse_content())

        if (gui_thread.is_alive()): # when gui is closed, kill the whole program
            time.sleep(10)
        else:
            exit(1)

main()
