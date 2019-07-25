# coding=utf-8
import time
from retrying import retry
from config import SPIDER_DEFAULT_HEADERS
import requests

@retry(stop_max_attempt_number=3)
def _parse_url(url):
    response = requests.get(url,timeout=5,headers=SPIDER_DEFAULT_HEADERS)
    assert response.status_code == 200
    return response.content.decode()

def parse_url(url):  #发送请求,获取响应
    print("now parseing",url)
    try:
        time.sleep(0.4)
        html_str = _parse_url(url)
    except Exception as e:
        print(e)
        html_str = None
    return html_str

