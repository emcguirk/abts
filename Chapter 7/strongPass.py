import re

rgx = re.compile(r'''(
	([a-zA-Z0-9]){0,7} # Any character preceding required character
	(\d)			# Required digit somewhere in regex
	([a-zA-Z0-9])+ # Remainder of password
	)''', re.VERBOSE)
	

def isStrong(pwd):
	assert type(pwd) == str
	x = rgx.search(pwd)
	if len(pwd) == len(x.group(0)):
		return True
	else:
		return False