from education.common.sendmethod import *

BASE_URL = "https://dapi.bighome360.com"

HEAD = ["application/x-www-form-urlencoded", "multipart/form-data", "application/json", "text/xml", "image/jpeg"]

def geturl(url):
    return BASE_URL + url

def getHeader(type, i, token=0):
    if type == 0:
        return {"content-type": HEAD[i]}
    else:
        return {"content-type": HEAD[i], "token": token}
