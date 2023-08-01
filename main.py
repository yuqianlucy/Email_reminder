# IMporting the require library
import os
from  email.message import EmailMessage
import ssl
import smtplib
# Intialized few varibale for email senting
email_sender = 'yuqianlucy@gmail.com'
email_password = os.environ("EMAIL_PASSWORD")
email_receiver='yuqianlucy@gmail.com'

#defining the subject
subject ='Check out the email reminder'
body = """
Starting to test whether we are able to sent email successfully through python.
"""

# declare EMailMessage object
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
# We are taking care of the body
em.set_content(body)

# taking care of the security
context = ssl.create_default_context()

# using smtplib to sent the email
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sentmail(email_sender,email_receiver,em.as_string())


# # # # Import the require libirary
# import os
# import base64
# import google.auth
# from googleapiclient.discovery import build
# from google.auth.transport.requests import Request

# # We are creating an function to create gmail service
# def create_gmail_service():
#     SCOPES = ['https://www.googleapis.com/auth/gmail.compose']

#     # We are Loading the credentials from the JSON file obtain from the Google API Console
#     credentials_filename = 'credentials.json'
#     creds = None
#     if os.path.exists(credentials_filename):
#         creds, _ = google.auth.load_credentials_from_file(credentials_filename,SCOPES)

#     # checking if credentials are not valid or expired, get new credentials
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = google.auth.default(scopes=SCOPES)
#             creds = flow.run_local_server()
#         # Save the credentials for future use
#         with open(credentials_filename, 'w') as f:
#             f.write(creds.to_json())
#     # We are Building the Gmail API service
#     service = build('gmail','v1', credentials=creds)
#     return service

# # Defining the first function to send_email
# def send_email(service, to_email, subject, body):
#     message = f'From: your_email@gmail.com\nTo:{to_email}\nSubject: {subject}\n\n{body}'
#     raw_message = base64.urlsafe_b64decode(message.encode()).decode()
#     # using an try block to test whether email are senting successfully

#     try:
#         service.users().messages().send(userId='me',body={'raw':raw_message}).execute()
#         # if email are senting successfully, we are printing message to show
#         print("Email sent successfully!")
#     # taking care of the exception block
#     except Exception as e:
#         # Sorry we are failing to sent email
#         print(f"Failed to send email: {e}")



# # defining the main function
# def main():
#     # defining the recipent_email
#     # Using the personal email to check
#     recipient_email = 'yuqianlucy@gmail.com'
#     reminder_subject = 'Reminder: Follow Up'
#     reminder_body = 'This is a friendly reminder to follow up on the task.'

#     # Create the Gmail API service
#     service = create_gmail_service()

#     # send the email
#     send_email(service, recipient_email, reminder_subject,reminder_body)
    

# # Defining the entry point
# if __name__ == "__mian__":
#     main()
# # Step 2: we are setting up an connection to our email server
# smtp = smtplib.SMTP('smtp.gmail.com',587)
# smtp.ehlo()
# smtp.starttls()
# smtp.login('YourMail@gmail.com','Your Password')

# # Step 3: send the email message 'msg' to the owner
# def message(subject="Python Notification",
#             text="", img=None,
#             attachment=None):
#     # build message contnets
#     msg = MIMEApplication()
#     # we are adding Subject
#     msg['Subject']=subject
#     # Add text contents
#     msg.attach(MIMEText(text))
#     # We are checking if we have anything
#     # given the img parameter
#     if img is not None:
#         # We are Checking whether we have the lists of images or not!
#         if type(img) is not list:
#             # if it isn't a list, make it one
#             img=[img]
#         # then, we are iterate through the list
#         for one_img in img:
#             # We are reading the image binary data
#             img_data = open(one_img, 'rb').read()
#             # We are Attaching the image data to MIMEMultipart
#             # then, using MIMEImage, add the given filename
#             msg.attach(MIMEImage(img_data,
#                                  name=os.path.basename(one_img)))
#         # We also do the same for
#         # attachment 
#     if attachment is not None:
#         # Check whether we have 
#         # lists of attachemnts or not
#         if type(attachment) is not list:
#             # If it isn't a list, make it one
#             attachment = [attachment]
#         # going through for loop
#         for one_attachment in attachment:
#             # opening in reading binary 
#             with open(one_attachment,'rb') as f:
#                 # We are Read in the attachemnt
#                 # We are using MIMEApplication
#                 file = MIMEApplication(
#                     f.read(),
#                     name=os.path.basename(one_attachment)
#                 )
#             file['Content-Disposition'] = f'attachmnt;\
#                 filename="{os.path.basename(one_attachment)}"'
#             # lastly, we are Adding the attachemnt to our message object
#             msg.attach(file)
#     # We are returning the message   
#     return msg

# defining the main function to call the subfunction
# def main():
#     pass
    # # We are Calling the message function
    # msg = message("Good", "Hi there!",
    #               r"C:\Users\yuqia\OneDrive\Desktop\6.PNG",
    #               r"C:\Users\yuqia\OneDrive\Desktop\hello.txt")
    # # Make a list of emails, right now is in testing phase, we are only doing one
    # to = ["yuqianlucy@gmail.com"]

    # # We arw Providing some data to the sendmail function!
    # smtp.sendmail(from_addr="yuqianlucy@gmail.com",
    #               to_addrs=to, msg=msg.as_string())
    
    # # Finally, we need to close the connection
    # smtp.quit()
           



# import schedule
# import time

# # Creating an function to send email, which require three parameter, the to_email, the subject, and the body of the email
# def send_email(to_email, subject, body):
#     # Need to set variable to store which email it is from
#     from_email = 'yuqianlucy@gmail.com'
#     # setting an variable to store the password, kind of worry of security issues, might need to come up a way to fix or modify it
#     # setting up the server
#     smtp_server = 'smtp.gmail.com'
#     # setting up the port 
#     smtp_port = 587

#     # Setting up an try block to check the server connections
#     try:
#         #Create a secure connection to the SMTP server, using the server variable and port variable
#         server = smtplib.SMTP(smtp_server,smtp_port)
#         # the starttls function does: (keyfile: str | None = None, certfile: str | None = None, context: SSLContext | None = None) -> _ReplyPuts the connection to the SMTP server into TLS mode.
#         #If there has been no previous EHLO or HELO command this session, this method tries ESMTP EHLO first.
#         #If the server supports TLS, this will encrypt the rest of the SMTP session. If you provide the keyfile and certfile parameters, the identity of the SMTP server and client can be checked. This, however, depends on whether the socket module really checks the certificates.
#         #This method may raise the following exceptions:
#         #SMTPHeloError The server didn't reply properly tothe helo greeting.
#         server.starttls()
#         # We are using server.login function to login to the personal email account
#         server.login(from_email, password)
#         # Then, we are composing the email message
#         message = f'Subject: {subject}\n\n{body}'
#         # We are sending the email with three parameter from_email, to_email, message
#         server.sendmail(from_email, to_email, message)
#         # if Email are senting successfully, then we print out an message to show
#         print("Email sent successfully!")
    
#     # taking care of exception for different email senting error
#     except Exception as e:
#         # print the Error message
#         print(f"Error sending email: {e}")
    
#     # Take care of the final block
#     finally:
#         server.quit()
# # Defining the main function
# def main():
#     # Defining the require variables
#     recipient_email = 'yuqianlucy@gmail.com'
#     reminder_subject = 'Reminder: Follow Up'
#     reminder_body = 'This is a friendly reminder to follow up on task'
#     send_email(recipient_email,reminder_subject,reminder_body)

# # next, we need to create an function to send the reminder
# def send_reminder():
#     # Creating an variable to store recipent email
#     recipient_email = 'recipient@example.com'
#     # Creating an variable to store reminder_subject
#     reminder_subject = 'Reminder: Follow Up'
#     # Creating an variable to store the reminder body
#     reminder_body = 'This is a friendly reminder to follow up on the task.'
#     # calling the function send_email
#     send_email(recipient_email,reminder_subject,reminder_body)

# # Then, we are schedule the reminder to be sent every day at a specific time (9:00 AM)
# schedule.every().day.at("09:00").do(send_reminder)

# Keep the program running to execute schedues tasks

