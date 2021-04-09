import requests,os,bs4
#index=0
os.makedirs("bing",exist_ok=True)
text=input("Input what you wanna search...:")
url="https://cn.bing.com/images/search?q="+text
response=requests.get(url)
response.raise_for_status()
soap=bs4.BeautifulSoup(response.text)
#elem=soap.select("img[class='main_img img-hover']")
elem=soap.select("div.img_cont.hoff img")
#
if elem==[]:
    print("Failed.")
else:
    num=min(20,len(elem))
    for i in range(num):
        imageurl=elem[i].get("src")
        print(imageurl)
        image=requests.get(imageurl)
        image.raise_for_status()

        file=open(os.path.join("bing","{}.jfif".format(i)),"wb")
        print("Start downloading image{}".format(i))
        for chunk in image.iter_content(100000):
            file.write(chunk)
        file.close()
    path=os.getcwd()+"\\bing"
    print("Successfully finished! You can see them in Folder "+path)
