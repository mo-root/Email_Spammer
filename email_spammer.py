import smtplib
import time

i=0
email_login = str(input('enter your spam account email(your own email)'))
email_password = str(input('enter your spam account password, you should use a generated password.'))
spam = str(input('enter the email to spam: '))
subject = str(input('enter the email subject: '))
body = str(input('enter the email body: '))
number_of_emails = int(input('how many emails?'))


while i < number_of_emails:
	with smtplib.SMTP('smtp.gmail.com',587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		smtp.login(email_login, email_password)
		msg = f'subject: {subject}\n\n{body}'
		print(msg)
		smtp.sendmail('',spam,msg)
		print(i)
		i+=1
print('finished')
#in case an error comes up go to your google acc, and search for "less secure" and enable
