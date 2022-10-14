import smtplib, ssl
import sys

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "walid.khelifa.az@gmail.com"  # Enter your address
name = sys.argv[1]
receiver_email = sys.argv[2]
msg = sys.argv[3]
receiver_email2 = "doctor@gmail.com" # Enter receiver address
message = """\
Subject: Hi {}

This message is sent from the doctor.""".format(name)+"\n"+msg

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, 161631116278)
    server.sendmail(sender_email, receiver_email, message)
    server.sendmail(sender_email, receiver_email2, message)
    print("")

