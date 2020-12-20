# -*- coding:utf-8 -*-
"""
 @Time: 2020/12/20 下午10:13
 @Author: LiuHe
 @File: new.py
 @Describe:
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
ip_port = ('127.0.0.1', 9999)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp协议
server.bind(ip_port)
while True:
    data, client_addr = server.recvfrom(BUFSIZE)
    print('server收到的数据', data)
    if data == '1':
        p.start(0)
        p.ChangeDutyCycle(2.5 + 10 * 90 / 180)
        time.sleep(5)
        p.ChangeDutyCycle(2.5)
    server.sendto(data.upper(), client_addr)

server.close()