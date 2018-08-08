import os
from email.parser import Parser
email_list = []
email_body = []
parser = Parser()
path ='/home/skanda/cloudxProjects/Project1/emails/'
email_list =os.listdir(path)
for email_id in email_list:
	with open (path+email_id,'r') as r:
		emailText = r.read()
		email1 = parser.parsestr(emailText)
		if email1.is_multipart():
			for part in email1.walk():
				ctype = part.get_content_type()
				cdispo = str(part.get('Content-Disposition'))
				if ctype =='text/plain' and 'attachment' not in cdispo:
					search.append(part.get_payload(decode=True))
					break
				else:
					search.append(email1.get_payload(decode=True))

print(search)

