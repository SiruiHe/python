# 强口令检测
import re
KeyRegex1=re.compile(r".{8,}")
keyRegex2=re.compile(r"[a-z]+")
keyRegex3=re.compile(r"[A-Z]+")

text=input("Input Your PWD:")
if KeyRegex1.search(text) and keyRegex2.search(text) and keyRegex3.search(text):
    print("This is a strong one.")
else:
    print("Too weak!")