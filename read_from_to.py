import os
from email.parser import Parser
from clean_address import clean_address as c
parser = Parser()
email_from = []
cleaned = []
path = '/home/skanda/cloudxProjects/got-your-back/GYB-GMail-Backup-skandasneha@gmail.com/2018/3/2/'
email_list = os.listdir(path)

for email_names in email_list:
	with open(path+email_names, 'r') as r:
		emailText = r.read()
		email1 = parser.parsestr(emailText)
		email_from.append(email1.get('from'))
for email_id in email_from:
	cleaned.append(c(email_id))


print(cleaned)



