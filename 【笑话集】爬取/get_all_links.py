"""
获取所有的单页link
"""
import re
import time
import requests
import threading
import concurrent.futures
from lxml import etree
from demo import get_content, save

page_url = "http://www.jokeji.cn/keyword.asp?me_page=1"

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

def get_one_page_links(page_url):
    """
    获取所有单个页面的link

    我发现呀, 【笑话集】网页在分类这一页拥有者所有的笑话数据
    【思路】先将所有的link都收集下来, 然后采用多线程技术并行下载加快速度,
    【问题】数据以txt还是csv保存, 保存的时候保存哪些字段?
    【字段】笑话分类, 题目, 评论, 浏览, 日期, 内容
    【思考】我还缺少一个 py多线程代码 模板...
    【情况】py code在2023/11/2深夜, 缺少灵感了, 准备睡觉, 凌晨2点喽...
    【参考】python爬虫经典书籍【Python爬虫开发 从入门到实战】
    """
    ans = []
    try:
        response = get_response(page_url).text
        # print(response)
        tree = etree.HTML(response)
        lists = tree.xpath("//a/@href")  # 当前界面的所有 超链接
        # print(lists)
        for list in lists:
            if list[0:9] == "/jokehtml":
                i = "http://www.jokeji.cn" + list
                print(i)
                ans.append(i)
    except Exception as e:
        print(e)
    return ans



def get_all_links():
    """
    获取所有的link
    """
    ans = []
    url = "http://www.jokeji.cn/keyword.asp?me_page="
    for i in range(98, 100):
        u = url + str(i)
        links = get_one_page_links(u)
        ans += links
    return ans

def dowload_one(url):
    """
    下载单张图片...
    """
    try:
        category, title, content = get_content(url)
        # print(category, title, content)
        save(category, title, content, "笑话")
    except Exception as e:
        print(e)


def download_all(urls):
    """
    并发下载所有的url
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(dowload_one, urls)
    

def download(urls):
    """
    保存下载的所有
    """
    for url in urls:
        print("---")
        print(url)
        # if url == "None":
        #     continue
        try:
            category, title, content = get_content(url)
            # print(category, title, content)
            save(category, title, content, "笑话")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    ans = get_all_links()
    # download(ans)
    start_time = time.perf_counter()
    download_all(ans) # 并发下载 下载耗时8.98323490000621s
    download(ans) # 顺序下载 下载耗时26.213722700005746s
    end_time = time.perf_counter()
    print(f"下载耗时{end_time - start_time}s")

