from education.constant.globalvar import *

import requests

dsj_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=0240303c-1dc1-4729-b681-8d8522fe4f5c"

auto_robat = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=e83e4b37-5c5e-4108-9a72-969babda318f"

dict = ["###### -----自动化测试消息通知-----\n" + "***项目名称：***<font color=\"info\">教育项目</font>\n" + "***时间：***<font color=\"comment\">{}</font>\n".format(timestamp())]

def content():
    s = ""
    for i in dict:
        s += i + ""
    return s



def send_msg():
    # json格式化发送的数据信息

    headers = {"Content-Type": "text/plain"}
    send_data = {
        "msgtype": "markdown",  # 消息类型，此时固定为markdown
        "markdown": {
            "content": content()
        }
    }

    res = requests.post(url=auto_robat, headers=headers, json=send_data)





if __name__ == '__main__':
    send_msg()