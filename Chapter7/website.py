#从剪切板中读取并筛选出URL，再复制至剪切板
import pyperclip,re
webregex=re.compile(r'''(
(http://|https://)
(.*)
.
(.*)
)''',re.VERBOSE)

text=str(pyperclip.paste())
matches=[]
for group in webregex.findall(text):
    matches.append(group[0])

if len(matches)>0:
    pyperclip.copy("\n".join(matches))
    print("已复制到剪切板：")
    print("\n".join(matches))
else:
    print("没有找到URL。")