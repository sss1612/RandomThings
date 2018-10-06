import smtplib
#!!!
#Change privacy settings to less secure apps otherwise email provider will block(gmail)
#!!!
content = "example email stuff here. Just checking that this works"
email, passw = "", ""
sender, recipient = "", ""	#Ideally the mail sending from and to whom
							#so essentially email and sender is the same, easier to read
mail = smtplib.SMTP("smtp.gmail.com", 587)

mail.ehlo()

mail.starttls()

mail.login(email, passw)

mail.sendmail(sender, recipient, content)

mail.close()