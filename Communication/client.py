# -*- coding:utf-8 -*-
"""
 @Time: 2020/12/20 下午8:29
 @Author: LiuHe
 @File: client.py
 @Describe: 客户端
"""
from socket import *


class Client(object):
    def __init__(self):
        """
        客户端类
        初始化传输参数
        """
        self.from_port = 9090
        self.to_addr = '192.168.1.181'
        self.to_port = 9090
        self.sender = None
        self.msg_data = None

    def send(self, msg):
        """
        TODO 单开线程
        发送数据
        :param msg: 数据
        :return: None
        """
        self.sender = socket(AF_INET, SOCK_DGRAM)
        self.sender.sendto(msg.encode("utf-8"), (self.to_addr, self.to_port))
        self.msg_data = self.sender.recvfrom(1024)

        return self.msg_data

    def close(self):
        self.sender.close()