import requests
import base64
import json
from lxml import etree

"""
【目的】通过打码平台识别验证码, 模拟登录【古诗文】网
【获取目的url】(1) f12, (2) network, (3) preserve logs, (4) all 
"""
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

def download_png(url):
    """
    将验证码保存到本机
    """
    page_text = requests.get(url=url, headers=headers).text

    tree = etree.HTML(page_text)
    code_img_src ="https://so.gushiwen.cn/" + tree.xpath('/html/body/form[1]/div[4]/div[4]/img/@src')[0]
    img_data = requests.get(url=code_img_src, headers=headers).content
    with open('./code.png','wb') as f:
        f.write(img_data)
    return img_data


def get_code(image, verify_type="60000"):
    """
    在线识别, 获取验证码
    """
    _custom_url = "http://api.jfbym.com/api/YmServer/customApi"
    _token = "aMRurUVe_aQ_66ejmWaMVeFnJy6MkTo02mUYrHI_gdI"
    _headers = {
        'Content-Type': 'application/json'
    }
    
    payload = {
        "image": base64.b64encode(image).decode(),
        "token": _token,
        "type": verify_type
    }

    # print(payload)
    resp = requests.post(_custom_url, headers=_headers,data=json.dumps(payload))
    # print(resp.text)
    return resp.json()['data']['data']


if __name__ == "__main__":

    # 1. 将验证码保存本地
    url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
    img_data = download_png(url)
    
    # 2. 调用打码平台示例程序进行验证码识别
    # 2.1 我们自己封装整理出一个识别验证码的函数
    code_text = get_code(image=img_data, verify_type="10110")
    print('识别结果: ', code_text)

    # 2.2 导入其他文件中的类【其他的方法】
    # y = YdmVerify()
    # y.common_verify(img_data,10110) 

    login_url = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"
    data = {
        "__VIEWSTATE": "kgCPZcmBWciXXasiCxE7SctULlln4O+k98VKRAWxZ+/4eoyvGjYbpVEpuWc6cYrG0o19/bAUzzCVBEbDDTHaAM1uN/+H1oEDRnGDRDKRZkHOVLXzim78bORTqa4a5sYzH2zpFagM/bB+LInuWdOqHt8iwS8=",
        "__VIEWSTATEGENERATOR": "C93BE1AE",
        "from": "http://so.gushiwen.cn/user/collect.aspx",
        "email": "18251608826",
        "pwd": "08183080xhl",
        "code": code_text,
        "denglu": "登录"
    }

    resp = requests.post(url=login_url, headers=headers, data=data)
    print(resp.status_code)
    # print(resp.text)
    # 返回200，则是响应成功...
