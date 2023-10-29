import smtplib, ssl
import os

def send_confirmation(message, receiver):
    host = "smtp.gmail.com"
    port = 465

    username="mundydavidc@gmail.com"
    password=os.getenv("KEY")
    
    receiver = "######"
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)