'''
import  requests
re = requests.get('https://api.lovelive.tools/api/SweetNothings')
print(re.text)

import random
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

index=random.randint(0,len(xianzhong_quote)-1)
print(xianzhong_quote[index])

'''


def tranlate(source, direction):
    import requests
    import json

    url = "http://api.interpreter.caiyunai.com/v1/translator"

    # WARNING, this token is a test token for new developers, and it should be replaced by your token
    token = "3975l6lr5pcbvidl6jl2"

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

text="翻译：hello,bro."
text=text.split("：")
source=text[1]
target = tranlate(source, "auto2zh")

#source = "test"
#target = tranlate(source, "auto2zh")
a=target
print(target)