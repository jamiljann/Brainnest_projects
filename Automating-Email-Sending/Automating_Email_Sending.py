''' You work at a company that sends daily reports to clients via email. The goal of this project is to automate 
the process of sending these reports via email.

Here are the steps you can take to automate this process:

    Use the smtplib library to connect to the email server and send the emails.

    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.

    Use the os library to access the report files that need to be sent.

    Use a for loop to iterate through the list of recipients and send the email and attachment.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred 
    during the email sending process. '''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule     
import time
import logging

logging.basicConfig(filename="c:\Python\class\Session3(21-0202023)\proj\log.txt", level=logging.DEBUG, filemode="w")
mail_content = '''Hello,
This is a test mail with an attachment.
The mail is sent using Python SMTP library.
Thank You
'''
                            #The mail addresses of sender and receivers and sender email password
sender_address = 'sabbaghijamil@gmail.com'
sender_pass = 'odguxhuhnufihkxg'
receiver_address = ['jsabaghi@gmail.com', 'jsabaghi@yahoo.com', 'jsabbaghi@yahoo.com']
                            #Setup the MIME.     Add sender and receiver address into the MIME
message = MIMEMultipart()   # Creating an instance of MIMEMultipart
message['From'] = sender_address    # Assigning the sender_email, receiver_email, and subject of our mail
message['Subject'] = 'This email sent by Python. It has an attachment.'
#The subject line
message.attach(MIMEText(mail_content, 'plain')) #     Attach the body into the MIME
attach_file_name = 'c:\Python\class\Session3(21-0202023)\proj\Report.txt' # the attachments for the mail
attach_file = open(attach_file_name, 'rb') # Open the file as binary mode, which is going to be attached with the mail
payload = MIMEBase('application', 'octate-stream') # Read the byte stream and encode the attachment using base64 encoding scheme.
payload.set_payload((attach_file).read())   # the payload is the file that we are mailing and here the payload is being encoded
encoders.encode_base64(payload) #encode the attachment
                            #add payload header for the attachments
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)

                            #Create SMTP session for sending the mail
def send_emails():
    for receiver in receiver_address:
        message['To'] = receiver
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:  # use gmail server
                connection.starttls()                           #enable security
                connection.login(user= sender_address, password= sender_pass)    #login with mail_id and password
                text = message.as_string()                      #Converting the message into a string 
                connection.sendmail( sender_address, receiver, text)    # Sending the mail
            logging.info("Program is working as expected and mail sent to "+ receiver) # log send successfully mail messages into the log file
        except Exception as e:
            print('Error is:', e)
            logging.error("The program encountered an error" + e)# log error messages into the log file

print('Mails Sent')

                            # Every day at 8am the function will be called.
#schedule.every().day.at("08:00").do(send_emails)
schedule.every(1).minutes.do(send_emails)
while True:
    schedule.run_pending()
    time.sleep(1)