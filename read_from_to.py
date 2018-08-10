import os
from email.parser import Parser
from clean_address import clean_address as clean
parser = Parser()
result_list = []
cleaned_result_list = []
def read_from_to(path,field,email_list):
	for email_names in email_list:
		with open(path+email_names,'r') as r:
			emailText =r.read()
			parsed_email = parser.parsestr(emailText)
			result_list.append(parsed_email.get(field))
	for email_id in result_list:
		cleaned_result_list.append(clean(email_id))
	return cleaned_result_list


#test case
"""path = '/home/skanda/cloudxProjects/got-your-back/GYB-GMail-Backup-skandasneha@gmail.com/2018/3/2/'
email_list = os.listdir(path)
print(read_from_to(path,"From",email_list))"""
