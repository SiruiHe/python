import requests,os,bs4
url="http://xkcd.com"
os.makedirs("xkcd",exist_ok=True)
while not url.endswith("#"):
    print("Downloading page %s"%url)
    res=requests.get(url)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text)

    # 返回一个找到的列表
    comicElem=soup.select("#comic img")

    if comicElem==[]:
        print("cannot find images...555")
    else:
        comicUrl="https:"+comicElem[0].get("src")
        print("Downloading IMAGE %s"%url)
        res=requests.get(comicUrl)
        res.raise_for_status()
        imageFile=open(os.path.join("xkcd",os.path.basename(comicUrl)),"wb")
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    prevlink=soup.select("a[rel='prev']")[0]
    url="http://xkcd.com"+prevlink.get("href")

print("Done.")
