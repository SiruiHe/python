import re
text="我的邮箱是:350321341@qq.com，请多指教"
regex=re.compile(r"[0-9]*@[a-zA-Z]{2,3}.[a-zA-Z]{2,3}")
result=regex.search(text)
print("邮箱："+result.group(0))
new=regex.sub("censored",text)
print(new)