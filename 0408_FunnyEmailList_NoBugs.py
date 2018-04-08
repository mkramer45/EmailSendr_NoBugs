import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import sqlite3

conn = sqlite3.connect('StriveDB2.db')
cursor = conn.cursor()
cur5 = cursor.execute('SELECT email FROM Sendr_Usr WHERE RadioB = "Funny"')
info5 = cur5.fetchall()


newlist = [row[0] for row in info5]

msg = MIMEMultipart()
msg['From'] = 'mkramer265@gmail.com'
msg['To'] = 'mkramer789@gmail.com'
msg['Subject'] = 'simple email in python'
message = 'here is the email'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('mkramer265@gmail.com', 'Celtics123')

mailserver.sendmail('mkramer265@gmail.com',newlist,msg.as_string())

mailserver.quit()
print(newlist)


