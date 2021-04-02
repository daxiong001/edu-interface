import requests
import json

class Method(object):


    @staticmethod
    def send_method(method, url, header, params=None):
        if method == "get":
            response = requests.request(method=method, url=url, params=params, headers=header)
        elif method == "post":
            response = requests.request(method=method, url=url, json=params, headers=header)
        else:
            raise Exception("请求方式不正确,只能使用get或post方法")
        return response

if __name__ == '__main__':
    login_param = {
        "mobile": "19999999999",
        "password": "IABSvX2Sc8aKVaDuK0CysPZCEDEjQpzbfWQvX9WmNw11GYp2/OkCgyv26IcjA8MEEB2lrM9amP+sB8uo471xTcE8GYar2jl71BGasgcQImQVnmagA/LRUjbvB00RhRRX3Gw22M8lnzlOl4j5andNikPyjroXhNzcU+BJYJHLcz0="
    }
    header = {
        "content-type": "application/json"
    }
    url = "https://dapi.bighome360.com/edu-portal-server/api/portal/base/user/login"
    a = Method.send_method("post", url, header, params=login_param)
    print(a.json())