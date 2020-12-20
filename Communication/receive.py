# -*- coding:utf-8 -*-
"""
 @Time: 2020/12/20 下午8:27
 @Author: LiuHe
 @File: receive.py
 @Describe: 通信模块 接受指令
"""
import socket
import RPi.GPIO as GPIO
import time
import signal
import atexit


class Service(object):
    def __init__(self):
        """
        服务端
        """
        self.from_addr = "127.0.0.1"
        self.from_port = 9090
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.from_addr, self.from_port))
        self.recv_data = None
        self.recv_addr = None
        self.servopin = 18
        atexit.register(GPIO.cleanup)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servopin, GPIO.OUT, initial=False)
        self.p = GPIO.PWM(self.servopin, 50)

    def recv(self):
        """
        接受数据
        TODO 解析模块 开线程
        :return: 客户端发送的数据
        """
        print("======== 等待接收数据 =======")
        while True:
            self.recv_data, self.recv_addr = self.socket.recvfrom(1024)
            print("接收到的数据：" + self.recv_data.decode("utf-8"))
            print("客户端地址：" + str(self.recv_addr))
            if self.recv_data == "1":
                self.p.start(0)
                self.p.ChangeDutyCycle(2.5 + 10 * 90 / 180)
                time.sleep(5)
                self.p.ChangeDutyCycle(2.5)

        # return self.recv_data

    def close(self):
        print("======= 服务端关闭 =======")
        self.socket.close()

