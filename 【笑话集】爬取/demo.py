import re
import os
import requests
from lxml import etree

"""
【背景】从客户这里接了个python爬虫的小项目, 这不就熬夜搞起来了.
【基础】我有着python爬虫基础
【回忆】先写一个小demo, 单单只从一张网页中爬取数据先.
【参考】参考以前的模块化代码: 在我的微信公众号【与龙邂逅】
【感悟】AI工具可以大幅度增加生产力, 强者越强, 弱者越弱...
"""

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}
url = "http://www.jokeji.cn/jokehtml/fq/2023102811264268.htm"


def get_response(html_url):
    """
    发送请求：
        1. url地址
        2. 请求方式<get post>
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    response = requests.get(url=html_url, headers=headers)
    # <Response [200]>
    # 自动识别编码（智能提示，不需要记...）
    response.encoding = response.apparent_encoding  
    return response


def get_content(html_url):
    """
    获取小说内容
    :param  html_url: 传入小说详情页url地址
    :return 小说内容 
    提取数据, 解析数据
    parsel 使用里面css选择器去解析提取数据

    """
    try:
        response = get_response(html_url).text
        tree = etree.HTML(response)
        category = tree.xpath("//h1/a/text()")[1]
        # print(category)
        title = tree.xpath("//h1/text()")[1]
        # print(title)

        # 匹配中文开头字符串
        pattern = re.compile(r'[\u4e00-\u9fa5]')
        match = pattern.search(title)
        if match:
            start_index = match.start()
            title = title[start_index:]
            print(title)

        content = tree.xpath("/html/body/div[2]/div[1]/div[1]/ul/span/p/text()")
        content = '\n'.join(content)
        # print(content)
    except Exception as e:
        print(e)
    # for i in content:
    #     print(i)
    # print(content)
    return category, title, content

def save(category, title, content, directory):
    """
    将文件保存到文件夹(directory)中...
    """
    if not os.path.exists(directory):
        os.mkdir(directory)
    file = directory + "/" + category + "+" + title + ".txt"
    with open (file, mode="a", encoding="utf-8") as f:
        f.write(content)
        print(f"{title}保存成功!")
    

if __name__ == "__main__":
    # print(get_response(url).text)
    category, title, content = get_content(url)
    save(category,title, content, "笑话")