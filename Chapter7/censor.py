#审查规避：屏蔽敏感词
import pyperclip,re
CensorRegex=re.compile(r"(\w)\
((主席)|(总理)|(总书记))",re.VERBOSE)

text=str(pyperclip.paste())
matches=[]
censored=[]
for group in CensorRegex.findall(text):
    matches.append(group[0])


if len(matches)>0:
    pyperclip.copy("\n".join(matches))
    print("copied.")
    print("\n".join(matches))
    print(CensorRegex.sub(r"X\2",text))

else:
    print("没有敏感词！")

