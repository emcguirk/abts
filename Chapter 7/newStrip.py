import re
import pyperclip


def newStrip(text, char = '\s'):
	removeChar = r'^(' + re.escape(char) + r')*([^' + re.escape(char) + '])+(' + re.escape(char) + r')*$'
	
