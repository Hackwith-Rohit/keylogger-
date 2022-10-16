import smtplib

email = "bamajjw@gmail.com"
password = "ieygqvxsourdlshj"
def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)


email = "bamajjw@gmail.com"
password = "ieygqvxsourdlshj"
message = "hey rohit how are you"
send_mail(email, password, message)


