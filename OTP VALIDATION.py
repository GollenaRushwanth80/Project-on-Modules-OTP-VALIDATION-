import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

otp = random.randint(1111,9999)
body = f"OTP for Verification is {otp}"

msg = MIMEMultipart()
msg["From"] = "gollenarushwanth80@gmail.com"
msg["To"] = input("Enter Email id: ")
msg["Subject"] = "OTP For Validation"
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("gollenarushwanth80@gmail.com","wqce cxjd tzao xsnh")
server.send_message(msg)
server.quit()

cotp = int(input("Enter OTP Received: "))
if otp == cotp:
           print("OTP Verification Successful")
else:
    print("Invalid otp")
    
