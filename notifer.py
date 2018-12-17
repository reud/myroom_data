#coding:UTF-8
import os
import requests
def output(strings: str):
    print(strings)
    url='https://notify-api.line.me/api/notify'
    token=os.environ['KION_OSIETE_LINE_NOTIFER_ID']
    headders={'Authorization':'Bearer '+token}
    message=strings
    payload={'message':message}
    res=requests.post(url,data=payload,headers=headders)
