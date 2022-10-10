import smtplib
import time
i=0


spam = str(input('enter the email to spam: '))
J = int(input('how many emails?'))
while i < J:
	with smtplib.SMTP('smtp.gmail.com',587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		smtp.login('ostaz.rod123@gmail.com','rodrodrod123')
		subject = 'Please give us the free credits back'
		body = 'I beg you please give the free credits back this is my favorite website and it had never let me down and I really need to use yor serivce;('
		msg = f'subject: {subject}\n\n{body}'
		print(msg)
		smtp.sendmail('',spam,msg)
		print(i)
		i+=1
print('finished')
#in case an error comes up go to your google acc, and search for "less secure" and enable
