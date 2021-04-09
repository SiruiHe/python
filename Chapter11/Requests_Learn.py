import requests
response=requests.get("http://www.baidu.com/")
response.raise_for_status()
ptr=open("webdata.txt","wb")
for chunk in response.iter_content(10000):
    ptr.write(chunk)
ptr.close()


