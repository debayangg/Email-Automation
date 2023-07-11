import smtplib
import csv
import asyncio

async def send_email(server,sender_email,receiver_email,message):
    server.sendmail(sender_email, receiver_email, message)
    await asyncio.sleep(1)

port = 587  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = ''  # Enter your address
receiver_email = ""  # Enter receiver address
password = ''
message_subject = "" # Enter subject
message_text = "" # Enter message


server=smtplib.SMTP(smtp_server, port)
server.starttls() # Secure the connection using TLS
server.login(sender_email, password)
with open('./check.csv', 'r') as csv_file: # check.csv is the file with the list of emails
    fromaddr = sender_email
    toaddr = receiver_email
    csv_reader = csv.reader(csv_file)
    for line in csv_reader: # line is a list of emails
        for val in line: # val is an email
            bcc=val
            message = "From:{s}\n".format(s=fromaddr) + "To:{s}\n".format(s=toaddr)+"BCC:{s}\n".format(s=bcc)+ "Subject: %s\r\n" % message_subject+ "\r\n" + message_text
            print(bcc)
            asyncio.run(send_email(server,sender_email, [bcc,toaddr], message))