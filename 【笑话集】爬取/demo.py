import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}
url = "http://www.jokeji.cn/jokehtml/%E5%86%B7%E7%AC%91%E8%AF%9D/2016050223075420.htm"

resp = requests.get(url=url, headers=headers)
resp.encoding = resp.apparent_encoding
print(resp.text)
