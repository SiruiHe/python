# 随即选出五学图片并给出路径
import os,re,random
os.chdir(r"C:\Users\sword\Pictures\New_Pictures\五学土味表情包")
ImageRegex=re.compile(r"(.*)(png|jpg)$",re.IGNORECASE)
ImageList=[]
for file in os.listdir("."):
    if ImageRegex.search(file):
        ImageList.append(file)
print(ImageList)
index=random.randint(0,len(ImageList))
path=os.path.join("C:\\","Users","sword","Pictures","New_Pictures","五学土味表情包")
a=path+"\\"+ImageList[index]
print(path+"\\"+ImageList[index])
path=a.split("\\")
print("/".join(path))