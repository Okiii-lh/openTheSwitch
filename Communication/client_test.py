# -*- coding:utf-8 -*-
"""
 @Time: 2020/12/20 下午8:34
 @Author: LiuHe
 @File: client_test.py
 @Describe:
"""
from Communication.client import Client

try:
    client = Client()
    a = client.send("1")
    print(a)
    client.close()
except Exception as e:
    print(e)