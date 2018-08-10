def clean_address(a):
	num = 0	
	#print(a)
	for i in a:
		num +=1
		if i =='<':
			return(a[num:-1])
	else:
		return a
		
