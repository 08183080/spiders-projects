import requests
import base64

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
