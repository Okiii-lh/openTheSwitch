# -*- coding:utf-8 -*-
"""
 @Time: 2020/12/20 下午10:14
 @Author: LiuHe
 @File: new_.py
 @Describe:
"""
import socket

BUFSIZE = 1024
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input(">> ").strip()
    ip_port = ('192.168.1.181', 9999)
    client.sendto(msg.encode('utf-8'), ip_port)

    data, server_addr = client.recvfrom(BUFSIZE)
    print('客户端recvfrom ', data, server_addr)

client.close()