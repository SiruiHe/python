import bs4,os,requests
res=requests.get("http://nostarch.com")
res.raise_for_status()
response=bs4.BeautifulSoup(res.text)
print(type(response))