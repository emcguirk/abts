import re
import pyperclip as pc


def newStrip(text, char = ' '):
	'''
	text: str; text surrounded by another character
	char: default is space; character that needs to be removed from text
	Copies output to the clipboard
	'''
	assert type(text) == str
	regex = r'^(' + re.escape(char) + r')*(.*?)(' + re.escape(char) + r')*$'  #Constructs a raw string to be used as a regex
	removeChar = re.compile(regex).search(text).groups()[1]
	pc.copy(removeChar)