# Import the require libirary
import smtplib
import schedule
import time

# Creating an function to send email, which require three parameter, the to_email, the subject, and the body of the email
def send_email(to_email, subject, body):
    # Need to set variable to store which email it is from
    from_email = 'Your_email@gmail.com'
    # setting an variable to store the password, kind of worry of security issues, might need to come up a way to fix or modify it
    password = 'your_password'
    # setting up the server
    smtp_server = 'smtp.gmail.com'
    # setting up the port 
    smtp_port = 587

    # Setting up an try block to check the server connections
    try:
        #Create a secure connection to the SMTP server, using the server variable and port variable
        server = smtplib.SMTP(smtp_server,smtp_port)
        # the starttls function does: (keyfile: str | None = None, certfile: str | None = None, context: SSLContext | None = None) -> _ReplyPuts the connection to the SMTP server into TLS mode.
        #If there has been no previous EHLO or HELO command this session, this method tries ESMTP EHLO first.
        #If the server supports TLS, this will encrypt the rest of the SMTP session. If you provide the keyfile and certfile parameters, the identity of the SMTP server and client can be checked. This, however, depends on whether the socket module really checks the certificates.
        #This method may raise the following exceptions:
        #SMTPHeloError The server didn't reply properly tothe helo greeting.
        server.starttls()
        # We are using server.login function to login to the personal email account
        server.login(from_email, password)
        # Then, we are composing the email message
        message = f'Subject: {subject}\n\n{body}'
        # We are sending the email with three parameter from_email, to_email, message
        server.sendmail(from_email, to_email, message)
        # if Email are senting successfully, then we print out an message to show
        print("Email sent successfully!")
    
    # taking care of exception for different email senting error
    except Exception as e:
        # print the Error message
        print(f"Error sending email: {e}")
    
    # Take care of the final block
    finally:
        server.quit()

# next, we need to create an function to send the reminder
def send_reminder():
    # Creating an variable to store recipent email
    recipient_email = 'recipient@example.com'
    # Creating an variable to store reminder_subject
    reminder_subject = 'Reminder: Follow Up'
    # Creating an variable to store the reminder body
    reminder_body = 'This is a friendly reminder to follow up on the task.'
    # calling the function send_email
    send_email(recipient_email,reminder_subject,reminder_body)

# Then, we are schedule the reminder to be sent every day at a specific time (9:00 AM)
schedule.every().day.at("09:00").do(send_reminder)

# Keep the program running to execute schedues tasks

