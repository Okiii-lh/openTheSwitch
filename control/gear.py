# -*- coding:utf-8 -*-
"""
 @Time: 2020/12/22 下午9:31
 @Author: LiuHe
 @File: gear.py
 @Describe: 舵机控制
"""
import socket
import RPi.GPIO as GPIO
import time
import signal
import atexit

servopin = 18
atexit.register(GPIO.cleanup)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin, GPIO.OUT, initial=False)
p = GPIO.PWM(servopin, 50)

BUFSIZE = 1024
ip_port = ('192.168.1.181', 9999)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp协议
server.bind(ip_port)
while True:
    data, client_addr = server.recvfrom(BUFSIZE)
    print('server收到的数据', data)
    if data == b'1':
        p.start(0)
        p.ChangeDutyCycle(2.5 + 10 * 180 / 180)
        # 解决舵机抖动问题 sleep(0.04)
        time.sleep(0.04)
        time.sleep(2)
        p.ChangeDutyCycle(2.5+10*90/180)
        # 解决舵机抖动问题 sleep(0.04)
        time.sleep(0.04)
        time.sleep(2)
        # 解决舵机抖动
        p.ChangeDutyCycle(0)
    server.sendto(data.upper(), client_addr)

server.close()
