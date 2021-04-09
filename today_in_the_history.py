def today_in_the_history():
    import requests
    import json
    import time
    def func_standard(num):
        if(num<10):
            return "0"+str(num)
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

result2=today_in_the_history()
for i in range(len(result2)):
    text=result2[i]["year"]+"年的今天，"+result2[i]["title"]

    print(text)