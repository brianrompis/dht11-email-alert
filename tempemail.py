import smtplib
import time
import Adafruit_DHT
import subprocess

sensor = Adafruit_DHT.DHT22
pin = 4

threshold_bottom = 20.0
threshold_top = 24.0
threshold_humidity = 60.0
ACtemp = 20
AClowest = 16
AChighest = 25

smtpUser = 'server@astonmanado.com'
smtpPass = '5tgb%TGB6yhn'

toAdd = ['it@astonmanado.com', 'ce@astonmanado.com', 'brian.rompis@gmail.com']
fromAdd = smtpUser

subject = 'Server Room Warning!'
header = 'To: ' + ', '.join(toAdd) + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject

print 'Set AC Temperature to: {0}*C'.format(ACtemp)
sendir = subprocess.call(["irsend", "SEND_ONCE", "TCL", "KEY_" + str(ACtemp) + "C-cool-hi-mid"])

while True:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	print 'Temp= {0:6.2f}*C  Humidity= {1:6.2f}%'.format(temperature, humidity)
	
	if temperature > threshold_top:
		if ACtemp <= AClowest:
			body = 'Warning. Server Room temperature is too high' + '\n' + 'Temperature= {0:6.2f}*C\nHumidity= {1:6.2f}%'.format(temperature, humidity)
			
			print header + '\n' + body
			
			email = smtplib.SMTP('smtp.gmail.com',587)
			
			email.ehlo()
			email.starttls()
			email.ehlo()
			
			email.login(smtpUser, smtpPass)
			email.sendmail(fromAdd, toAdd, header + '\n\n' + body)
			
			email.quit()
		else:
			ACtemp -= 1
			sendir = subprocess.call(["irsend", "SEND_ONCE", "TCL", "KEY_" + str(ACtemp) + "C-cool-hi-mid"])
			print 'Attempting to decrease AC Temperature to: {0}*C'.format(ACtemp)
		time.sleep(300)
			
	elif temperature < threshold_bottom:
		if ACtemp >= AChighest:
			body = 'Warning. Server Room temperature is too low' + '\n' + 'Temperature= {0:6.2f}*C\nHumidity= {1:6.2f}%'.format(temperature, humidity)
			
			print header + '\n' + body
			
			email = smtplib.SMTP('smtp.gmail.com',587)
			
			email.ehlo()
			email.starttls()
			email.ehlo()
			
			email.login(smtpUser, smtpPass)
			email.sendmail(fromAdd, toAdd, header + '\n\n' + body)
			
			email.quit()
		else:
			ACtemp += 1
			sendir = subprocess.call(["irsend", "SEND_ONCE", "TCL", "KEY_" + str(ACtemp) + "C-cool-hi-mid"])
			print 'Attempting to increase AC Temperature to: {0}*C'.format(ACtemp)
		time.sleep(300)
		
	elif humidity > threshold_humidity:
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

