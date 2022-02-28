import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date

dt = date.today().strftime("%d-%m-%Y")
# d1 = date.today().strftime("%a")

msg = MIMEMultipart()

# Parameters
msg['From'] = "<usermail>@gmail.com"
msg['To'] = "<usermail>@gmail.com"
password = "<password>"
msg['Subject'] = "Notificação de Backup"

# Server
server = smtplib.SMTP("smtp.gmail.com: 587")
server.starttls()
 
# Login Credentials
server.login(msg['From'], password)
