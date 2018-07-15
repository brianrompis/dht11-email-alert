import smtplib

smtpUser = 'brian.rompis@gmail.com'
smtpPass = 'mymanado5566'

toAdd = 'it@astonmanado.com'
fromAdd = smtpUser

subject = 'Python Test Email'
header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject
body = 'Warning. Server Room temperature is too high'

print header + '\n' + body

email = smtplib.SMTP('smtp.gmail.com',587)

email.ehlo()
email.starttls()
email.ehlo()

email.login(smtpUser, smtpPass)
email.sendmail(fromAdd, toAdd, header + '\n\n' + body)

email.quit()
