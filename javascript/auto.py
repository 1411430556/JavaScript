#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from datetime import datetime
import time
import json
import importlib,sys
importlib.reload(sys)
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# 填写对应参数的值
data = {
    'aid': '2608',
    'uuid': '7095764327806060035',
    '_signature': ''
}

header = {
    "cookie": data.get('_ga=GA1.2.1678628831.1652111390; __tea_cookie_tokens_2608=%7B%22web_id%22%3A%227095764327806060035%22%2C%22user_unique_id%22%3A%227095764327806060035%22%2C%22timestamp%22%3A1652111390607%7D; _tea_utm_cache_2608={"utm_source":"gold_browser_extension"}; passport_csrf_token=1f33ffe141a9e75997254b9a4b91352b; passport_csrf_token_default=1f33ffe141a9e75997254b9a4b91352b; n_mh=bcXKVwQTayz-YT2-NvOiYqviRlPcD5eDMLSULfOmA-w; passport_auth_status=b290923246ee58605d2cfb96a8b213f1,; passport_auth_status_ss=b290923246ee58605d2cfb96a8b213f1,; sid_guard=233bc9ef9452a209b3182abc1585529a|1683726553|31536000|Thu,+09-May-2024+13:49:13+GMT; uid_tt=dc9a5b12b75659664ee28817127fe40d; uid_tt_ss=dc9a5b12b75659664ee28817127fe40d; sid_tt=233bc9ef9452a209b3182abc1585529a; sessionid=233bc9ef9452a209b3182abc1585529a; sessionid_ss=233bc9ef9452a209b3182abc1585529a; sid_ucp_v1=1.0.0-KGI5YmE0MTA5NzA5YzNlZWVhNDMwYjJmYjI5Yzg1MWM2MzI4ZDg2MTEKFwit48Ck-YytBBDZwe6iBhiwFDgCQPEHGgJsZiIgMjMzYmM5ZWY5NDUyYTIwOWIzMTgyYWJjMTU4NTUyOWE; ssid_ucp_v1=1.0.0-KGI5YmE0MTA5NzA5YzNlZWVhNDMwYjJmYjI5Yzg1MWM2MzI4ZDg2MTEKFwit48Ck-YytBBDZwe6iBhiwFDgCQPEHGgJsZiIgMjMzYmM5ZWY5NDUyYTIwOWIzMTgyYWJjMTU4NTUyOWE; store-region=cn-sc; store-region-src=uid; csrf_session_id=ea1c8399c54ffb2514d4eca71e6ec4fd; msToken=iwzO7i4VaOIhyh8REISGaq3pQbvKHUy8kp-s50mp9jdAvH9ObroTbkfhRxQ-81kVCf_9CyYawo4zxYwOzScB6CmLZEGXhWAJm5moGXh54GYybPufcWBnTaDixhKlc0Q=')
}

def sign_in():
    """
    请求签到接口
    :return: 
    """
    url = 'https://api.juejin.cn/growth_api/v1/check_in'
    r = requests.post(url, data, headers=header)
    print(r.text)
    return json.loads(r.text)['err_msg']

def draw():
    """
    签到后抽奖
    :return: 
    """
    urlD = 'https://api.juejin.cn/growth_api/v1/lottery/draw'
    dataD = {
        'aid': data.get('aid'),
        'uuid': data.get('uuid'),
    }
    r = requests.post(urlD, dataD, headers=header)
    print(r.text)
    return json.loads(r.text)['err_msg']

def start():
    """
    启动任务
    :return: 
    """
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    sign_msg = sign_in()
    time.sleep(10)
    draw_msg = draw()
    return "签到返回：" + sign_msg + '\n' + "抽奖返回：" + draw_msg

def send(str):
    body = {
		"token": 'd9202dc445914005b7379823867aca7f',
		"title": '【xxx】掘金签到&抽奖结果',
		"content": str
    }
    r = requests.post('http://www.pushplus.plus/send', data=body)
    print(json.loads(r.text))

if __name__ == "__main__":
    str = start()
    send(str)
exit(0)
