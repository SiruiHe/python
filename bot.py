import asyncio
from pickle import GET
import requests
import re,os
from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication
from graia.application.message.elements.internal import At, Plain
from graia.application.session import Session
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from graia.application.interrupts import GroupMessageInterrupt
from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session, Image
from graia.application.message.chain import MessageChain
import asyncio
import random



from graia.application.message.elements.internal import Plain
from graia.application.friend import Friend
from graia.broadcast.interrupt import InterruptControl

trans_or_not=0
qdh = re.compile(r"(全)?((斗焕)|(小将)|(将军))")

loop = asyncio.get_event_loop()

bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="http://localhost:8100",  # 填入 httpapi 服务运行的地址
        authKey="graia-mirai-api-http-authkey",  # 填入 authKey
        account=1933632011,  # 你的机器人的 qq 号
        websocket=True  # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
    )
)




def tranlate(source, direction):
    import requests
    import json

    url = "http://api.interpreter.caiyunai.com/v1/translator"

    # WARNING, this token is a test token for new developers, and it should be replaced by your token
    token = "wtxbbkeuspizmykzn484"  # "3975l6lr5pcbvidl6jl2"

    payload = {
        "source": source,
        "trans_type": direction,
        "request_id": "demo",
        "detect": True,
    }

    headers = {
        'content-type': "application/json",
        'x-authorization': "token " + token,
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

    return json.loads(response.text)['target']

def today_in_the_history():
    import requests
    import json
    import time
    def func_standard(num):
        if (num < 10):
           return "0" + str(num)
        else:
            return str(num)
    localtime = time.localtime(time.time())
    tm_mon = func_standard(localtime.tm_mon)
    tm_day = func_standard(localtime.tm_mday)
    today = tm_mon + tm_day
    response = requests.get("https://api.qzone.work/api/today.history?date=" + today)
    result = json.loads(response.text)
    result2 = result["data"]["list"]
    return result2

def ImagePath():
    import os,re,random
    os.chdir(r"C:\Users\sword\Pictures\New_Pictures\五学土味表情包")
    ImageRegex=re.compile(r"(.*)(png|jpg)$",re.IGNORECASE)
    ImageList=[]
    for file in os.listdir("."):
        if ImageRegex.search(file):
            ImageList.append(file)
    print(ImageList)
    index=random.randint(0,len(ImageList)-1)
    path=os.path.join("C:\\","Users","sword","Pictures","New_Pictures","五学土味表情包")
    return path+"\\"+ImageList[index]


@bcc.receiver("FriendMessage")
async def friend_message_listener(app: GraiaMiraiApplication, friend: Friend):
    await app.sendFriendMessage(friend, MessageChain.create([
        Plain("Hello, World!")
    ]))

    await app.sendFriendMessage(friend, MessageChain.create([
        Image.fromLocalFile("C:/Users/sword/Pictures/bow_to_bit_dalao.jpg")
    ]))

inc = InterruptControl(bcc)

'''
@bcc.receiver("GroupMessage")
async def group_message_handler(
    message: MessageChain,
    app: GraiaMiraiApplication,
    group: Group, member: Member,
):
    if message.asDisplay().startswith("/test_need_confirm"):
        await app.sendGroupMessage(658395370, MessageChain.create([
            At(member.id), Plain("发送 /accelerate 以继续运行")
        ]))
        await inc.wait(GroupMessageInterrupt(
            658395370, member,
            custom_judgement=lambda x: x.messageChain.asDisplay().startswith("/accelerate")
        ))
        await app.sendGroupMessage(658395370, MessageChain.create([
            Plain("我就感觉到快，有种催人跑的意思")
        ]))
'''

def set_global(num):
    global trans_or_not
    if(num==1):
        trans_or_not=1
    else:
        trans_or_not=0

@bcc.receiver("GroupMessage")
async def group_message_handler(
    message: MessageChain,
    app: GraiaMiraiApplication,
    group: Group, member: Member,
):

    global trans_or_not
    if message.asDisplay().startswith("开翻译"):
        set_global(1)

    if message.asDisplay().startswith("关翻译"):
        set_global(0)

    list=["我就感觉到快，有种催人跑的意思","换不了思想就换人","稳定压倒一切","穷了几千年了，再耽误不得咯","保证永不翻案",
          "不管白猫、黑猫，会捉老鼠就是好猫。","这些方面的制度好可以使坏人无法任意横行；制度不好可以使好人无法充分做好事，甚至会走向反面。",
          "做几件使人民满意的事情。主要是两个方面，一个是更大胆地改革开放，另一个是抓紧惩治腐败。",
          "计算机的普及要从娃娃抓起。",
          "教育要面向现代化、面向世界、面向未来。",
          "我荣幸地以中华民族一员的资格，而成为世界公民。我是中国人民的儿子。我深情地爱着我的祖国和人民。",
          "只要站在民族的立场上，维护民族的大局，不管抱什么政治观点，包括骂CPC的人，都要大团结。",
          "右可以葬送socialism，“左”也可以葬送socialism。中国要警惕右，但主要是防止“左”。",
          "socialism的本质，是解放生产力，发展生产力，消灭剥削，消除两极分化，最终达到共同富裕。",
          "socialism的目的就是要全国人民共同富裕，不是两极分化。如果我们的政策导致两极分化，我们就失败了；如果产生了什么新的资产阶级，那我们就真是走了邪路了。",
          "还要开放，不能关门，关起门来，信息不灵，什么追踪新技术呀，赶超世界先进水平呀，不开放是不成的。"]
    #while(1):


    if message.asDisplay().startswith("/quote"):
            #await app.sendGroupMessage(658395370, MessageChain.create([
            #    At(member.id), Plain("发送 /accelerate 以继续运行")
            #]))
            #await inc.wait(GroupMessageInterrupt(
            #    658395370, member,
            #    custom_judgement=lambda x: x.messageChain.asDisplay().startswith("/accelerate")
            #))
        index=random.randint(0,len(list)-1)
        await app.sendGroupMessage(658395370, MessageChain.create([
            At(member.id),Plain(" 他曾说过："+list[index])
        ]))
    elif message.asDisplay().startswith("/meme"):
        await app.sendGroupMessage(658395370, MessageChain.create([
            At(member.id), Plain(" 差不多得了😅")
        ]))

    elif message.asDisplay().startswith("西交"):
        for i in range(5):
            await app.sendGroupMessage(658395370, MessageChain.create([
                Plain("真的费拉")
            ]))

    if message.asDisplay().startswith("/love"):
        re = requests.get('https://api.lovelive.tools/api/SweetNothings')
        await app.sendGroupMessage(658395370, MessageChain.create([
            Plain(re.text)
        ]))

    if message.asDisplay().startswith("献忠") or message.asDisplay().startswith("/kill")\
            or message.asDisplay().endswith("献忠"):
        xianzhong=\
        "天は万物で人を生かす\
        人は天に怨嗟して続く\
        害虫が世間で溢れること知らぬ\
        庶民を苦しんで王臣を満足しまう\
        人は出身によって貴賤あり\
        人の富貴は天にあり\
        庶民の貧乏は天による罰し\
        ある狂人は夜で包丁研ぎ\
        帝星が蛍惑高を揺らした\
        このより天地を覆すように\
        人を殺すことは手を惜しまない\
        不忠な人が殺すべき\
        不貞な人が殺すべき\
        不仁な人が殺すべき\
        不義な人が殺すべき\
        無礼無智無信者\
        大西王は殺々々を曰く\
        王道征くこと思わない\
        表に黄金台を建てること思嫌い\
        進士も大臣も犬に如き\
        いつも刀の下に殻材なり\
        部下の四王子を命令し\
        城破れも刀を封じる必要はない\
        天の代わりに碑を山の頭代で立ち\
        天に逆らう者は即死、足曲んでも死ぬ\
        天は万物で人を生かす\
        人は一善ほど恩返しもできぬ\
        殺！殺！殺！殺！殺！殺！殺！\
        "
        xianzhong_quote=xianzhong.split('        ')
        index=random.randint(0,len(xianzhong_quote)-1)
        await app.sendGroupMessage(658395370, MessageChain.create([
            Plain(xianzhong_quote[index])
        ]))


    if message.asDisplay().startswith("晚安"):
        await app.sendGroupMessage(658395370, MessageChain.create([
                Plain(" 晚安")
        ]))

    if message.asDisplay().startswith("翻译+"):
        text=message.asDisplay().split("+")
        source=text[1]
        try:
            target = tranlate(source, "auto2zh")
            #a=target
            #print(a)
        except KeyError:
            target="抱歉，翻译失败。"
        await app.sendGroupMessage(658395370, MessageChain.create([
            Plain(target)
        ]))
    #source = ["Lingocloud is the best translation service.", "彩云小译は最高の翻訳サービスです"]


        print(target)

    if message.asDisplay().startswith("trans+"):
        text = message.asDisplay().split("+")
        source = text[1]
        try:
            target = tranlate(source, "auto2en")
            # a=target
            # print(a)
        except KeyError:
            target = "抱歉，翻译失败。"
        await app.sendGroupMessage(658395370, MessageChain.create([
            Plain(target)
        ]))
        print(target)

    if message.asDisplay().startswith("transjp+"):
        text = message.asDisplay().split("+")
        source = text[1]
        try:
            target = tranlate(source, "auto2ja")
            # a=target
            # print(a)
        except KeyError:
            target = "抱歉，翻译失败。"
        await app.sendGroupMessage(658395370, MessageChain.create([
            Plain(target)
        ]))
        print(target)


    if message.asDisplay().startswith("/today") or message.asDisplay().startswith("今天") :
        result2 = today_in_the_history()
        text=result2[0]["year"] + "年的今天，" + result2[0]["title"]
        text=" ".join(text.split("-"))
        await app.sendGroupMessage(658395370, MessageChain.create([
                Plain(text)
        ]))

    if trans_or_not==1 and message.asDisplay()!="开翻译":
        source = message.asDisplay()
        try:
            target = tranlate(source, "auto2en")
        except KeyError:
            target = "抱歉，翻译失败。"
        await app.sendGroupMessage(658395370, MessageChain.create([
            Plain(target)
        ]))
        print(target)


    if qdh.search(message.asDisplay()):
        path=ImagePath().split("\\")
        path="/".join(path)
        await app.sendGroupMessage(658395370, MessageChain.create([
            Image.fromLocalFile(path)
        ]))





app.launch_blocking()

