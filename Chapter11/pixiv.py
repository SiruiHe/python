import requests,os,bs4,random
#index=0
os.makedirs("yandex",exist_ok=True)
text=input("Input what you wanna search...:")
#print("Start searching...")
#num=random.randint(10000000,99999999)
url="https://yandex.com/images/search?text="+text
response=requests.get(url)
response.raise_for_status()
soap=bs4.BeautifulSoup(response.text)
#elem=soap.select("img[class='main_img img-hover']")
elem=soap.select("img")
if elem==[]:
    print("Failed.")
else:
    num=min(20,len(elem))
    for i in range(num):
        imageurl=elem[i].get("src")
        print(imageurl)
        image=requests.get(imageurl)
        image.raise_for_status()

        file=open(os.path.join("bing",os.path.basename(imageurl)),"wb")
        print("Start downloading "+os.path.basename(imageurl))
        for chunk in image.iter_content(100000):
            file.write(chunk)
        file.close()
    path=os.getcwd()+"\\pixiv"
    print("Successfully finished! You can see them in Folder "+path)
