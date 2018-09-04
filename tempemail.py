import smtplib
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 4

smtpUser = 'server@astonmanado.com'
smtpPass = '5tgb%TGB6yhn'

toAdd = ['it@astonmanado.com', 'ce@astonmanado.com', 'brian.rompis@gmail.com']
fromAdd = smtpUser

subject = 'Server Room Warning!'
header = 'To: ' + ', '.join(toAdd) + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject

while True:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	print 'Temp= {0:6.2f}*C  Humidity= {1:6.2f}%'.format(temperature, humidity)
	
	if temperature > 24.0:
		body = 'Warning. Server Room temperature is too high' + '\n' + 'Temperature= {0:6.2f}*C\nHumidity= {1:6.2f}%'.format(temperature, humidity)
		
		print header + '\n' + body
		
		email = smtplib.SMTP('smtp.gmail.com',587)
		
		email.ehlo()
		email.starttls()
		email.ehlo()
		
		email.login(smtpUser, smtpPass)
		email.sendmail(fromAdd, toAdd, header + '\n\n' + body)
		
		email.quit()
		time.sleep(300)
	elif temperature < 20.0:
		body = 'Warning. Server Room temperature is too low' + '\n' + 'Temperature= {0:6.2f}*C\nHumidity= {1:6.2f}%'.format(temperature, humidity)

		print header + '\n' + body
		
		email = smtplib.SMTP('smtp.gmail.com',587)
		
		email.ehlo()
		email.starttls()
		email.ehlo()
		
		email.login(smtpUser, smtpPass)
		email.sendmail(fromAdd, toAdd, header + '\n\n' + body)
		
		email.quit()
		time.sleep(300)

	elif humidity > 60.0:
		body = 'Warning. Server Room humidity is too high' + '\n' + 'Temperature= {0:6.2f}*C\nHumidity= {1:6.2f}%'.format(temperature, humidity)
		
		print header + '\n' + body

		email = smtplib.SMTP('smtp.gmail.com',587)
		
		email.ehlo()
		email.starttls()
		email.ehlo()
		
		email.login(smtpUser, smtpPass)
		email.sendmail(fromAdd, toAdd, header + '\n\n' + body)
		
		email.quit()
		time.sleep(300)

	else:
		time.sleep(2)

