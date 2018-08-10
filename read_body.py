import os
from email.parser import Parser
email_body = []
parser = Parser()
def read_body(path,email_list):
	for email_id in email_list:
		with open(path+email_id,'r') as r:
			emailText = r.read()
			parsed_email = parser.parsestr(emailText)
			if parsed_email.is_multipart():
				for email_part in parsed_email.walk():
					ctype = email_part.get_content_type()
					cdispo = str(email_part.get('Content-Disposition'))
					if ctype =='text/plain' and 'attachment' not in cdispo:
						email_body.append(str(email_part.get_payload(decode=True)))
						break
					else:
						email_body.append(str(parsed_email.get_payload(decode=True)))
	return email_body


#test_case
"""path = '/home/skanda/cloudxProjects/got-your-back/GYB-GMail-Backup-skandasneha@gmail.com/2018/3/2/'
email_list = os.listdir(path)
print(type(read_body(path,email_list)[0]))"""

