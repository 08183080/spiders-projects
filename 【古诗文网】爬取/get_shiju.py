import re
import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}
url = "https://so.gushiwen.cn/mingjus/"
shiju_url = "https://so.gushiwen.cn/mingjus/"

def get_response(html_url):
    """
    发送请求：
        1. url地址
        2. 请求方式<get post>
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    response = requests.get(url = html_url, headers = headers)
    # <Response [200]>
    # 自动识别编码（智能提示，不需要记...）
    response.encoding = response.apparent_encoding  
    # print(response)
    return response

def get_content(html_url):
    """
    获取当前页面的所有诗句...
    """
    try:
        response = get_response(html_url).text
        tree = etree.HTML(response)
        shijus = tree.xpath("//div[@class='cont']/a/text()")
        for shiju in shijus:
            if len(shiju) == 2 or len(shiju) == 3 or len(shiju) == 4:
                continue
            print(shiju)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    get_response(url)
    get_content(shiju_url)