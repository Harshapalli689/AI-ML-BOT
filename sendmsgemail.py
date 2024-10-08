import pywhatkit
email_sender="harshapalli678@gmail.com"
password="Harsha@12345"
subject="From Harsha"
message="harsha"
email_receiver="harshapalli689@gmail.com"
def emailer():
    try:
      pywhatkit.start_server()
      # note : password is the app password you should generate from email
      pywhatkit.send_mail(email_sender, password, subject, message, email_receiver)
      print("Successfully Sent the Message..")
    except Exception as ex: 
      print("Something went wrong....",ex)

emailer()