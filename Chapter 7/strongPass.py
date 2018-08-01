import re
import pyperclip

# Regexes for each requirement:
hasLower = re.compile(r'[a-z]')
hasUpper = re.compile(r'[A-Z]')
hasNumber = re.compile(r'[0-9]')

def isStrong(pwd):
	assert type(pwd) == str
	lower = hasLower.findall(pwd)
	upper = hasUpper.findall(pwd)
	number = hasNumber.findall(pwd)
	if len(lower) < 1 or len(upper) < 1 or len(number) < 1:
		print('Password is not strong enough. Make sure to include all required characters')
	if len(pwd) < 8:
		print('Password is not strong enough. Please enter at least 8 characters')
	else:
		print('Password is strong')
