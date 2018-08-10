import re
import os
from email.parser import Parser
from clean_address import clean_address as clean
from read_from_to import read_from_to
from read_body import read_body
parser = Parser()
search_list = []

def search_pattern(path,field,pattern):
	
	if field =='From' or field=='To':
		search_list = read_from_to(path,field,email_list)
		#print(search_list)
		for i in search_list:
			if(re.match(pattern,i)):
				return i
		else:
			return "Found no pattern"
	else:
		search_list =read_body(path,email_list)	
		to_list = read_from_to(path,'From',email_list)
		number = 0;print(to_list)		
		for i in search_list:
			if(re.match(pattern,i)):
				return to_list[number]
			else:
				number +=1
		else:
			return("Found no pattern")				
		
	
	
pattern ="(oo\w+)"
path ='/home/skanda/cloudxProjects/_Project1/emails/'
field = input("Which field to search?:From,To or Body?:")
email_list = os.listdir(path)
print(search_pattern(path,field,pattern))
	
