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
    a=json.loads(response.text)
    re=a['target']

    return re #json.loads(response.text)['target']

text=input()
a=tranlate(text,"auto2en")
result=a
print(result)