# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import requests


data = {'k1':100,'k2':300}


#requests.get("http://127.0.0.1:8000/api/asset?k1=123")
#requests.get("http://127.0.0.1:8000/api/asset",params=data)
#参数放在url 以GET方式传值
#requests.post("http://127.0.0.1:8000/api/asset",params=data)
#参数放在请求体
requests.post("http://127.0.0.1:8000/api/asset",data=data,headers='')

#传递headers
headers = {'a':123}
