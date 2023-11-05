import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Cookie": "wxopenid=defoaltid; ticketStr=202553309%7cgQFU8DwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAyVzExMlF2bGVkN2kxdXFVRnhCMVEAAgSaa0JlAwQAjScA; Hm_lvt_9007fab6814e892d3020a64454da5a55=1696932163,1698850241,1699116144; login=flase; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1699150341; ASP.NET_SessionId=yn5tju4r0s2ez3d0o1ci4wrq; codeyzgswso=573734c5f363c5ac"
}


def login(url):
    """
    【目的】用cookie方式模拟登录【古诗文网】
    【进度】初次运行, 未扫码...
    """
    resp = requests.get(url = url, headers = headers).content.decode()
    print(resp)

if __name__ == "__main__":
    url = "https://so.gushiwen.cn/user/getEventLogin.aspx?scene_id=202553309"
    login(url)
    