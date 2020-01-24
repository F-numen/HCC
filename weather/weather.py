# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 23:10:23 2019

@author: F_numen
"""

#----------------------------------
# 在线接口文档：https://code.juhe.cn/docs/1064
#----------------------------------

import requests

# 根据城市查询天气
def get_weather(appkey):
    url = "http://apis.juhe.cn/simpleWeather/query"
    params = {
        "city" : "210", #要查询的城市，如：温州、上海、北京
        "key" : appkey, #应用APPKEY(应用详细页查询)
        "dtype" : "", #返回数据的格式,xml或json，默认json
    }

    req = requests.get(url, params=params).json()

    if req:
        error_code = req["error_code"]
        if error_code == 0:
            #成功请求
            return req["result"]
        else:
            print("%s:%s" % (req["error_code"],req["reason"]))
    else:
        print("request api error")
 
if __name__ == '__main__':
    
    # 配置申请的APPKey
    appkey = "9d798287563d8b4e5cdaeb25d9e811b4"
 
    # 根据城市查询天气
    weather = get_weather(appkey)
    print(weather)
