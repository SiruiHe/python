import re,pyperclip
text=str(pyperclip.paste())
new=text.replace(r"\\","\\")
pyperclip.copy(new)
