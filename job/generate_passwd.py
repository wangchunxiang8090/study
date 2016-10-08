#!/usr/bin/env python 
import random

def password(length=12):
	code = []
	for i in range(length):
	  r = random.randrange(1,9)
	  if r == 2 or r == 4:
		temp = random.randrange(0,9)
		code.append(str(temp))
	  elif r > 4: 
		temp = chr(random.randrange(97,122))
		code.append(temp)
	  else:
		temp = chr(random.randrange(65,90)) 
		code.append(temp)

	print ''.join(code)

if __name__ == '__main__':

	number = raw_input('please input generator password length default length 12:')
	try:
		i_number = int(number)
	except Exception:
		password(12)
	try:
		password(i_number)	
	except Exception:
		pass
