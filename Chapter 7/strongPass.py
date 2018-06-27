import re
import pyperclip

# Regexes for each requirement:
hasLower = re.compile(r'[a-z]')
hasUpper = re.compile(r'[A-Z]')
hasNumber = re.compile(r'[0-9]')

def isStrong(pwd):
	assert type(pwd) == str
	lower = hasLower.search(pwd)
	upper = hasUpper.search(pwd)
	number = hasNumber.search(pwd)
	if lower != 1 or upper == 0 or number != 0:
		print('Password is not strong enough. Make sure to include all required characters')
	if len(pwd) < 8:
		print('Password is not strong enough. Please enter at least 8 characters')
	else:
		print('Password is strong')
