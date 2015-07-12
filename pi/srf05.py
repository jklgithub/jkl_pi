#app.py coding:utf-8 srf05超声测距模块驱动
import RPi.GPIO as GPIO
import time
from time import ctime, sleep

__gproTrig = 16
__gproEcho = 12
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(__gproTrig, GPIO.OUT)
    GPIO.setup(__gproEcho, GPIO.IN)


def measure():
    #启动测距
    GPIO.output(__gproTrig, True)
    time.sleep(0.00001)
    GPIO.output(__gproTrig, False)
    start = time.time()
    print("measure--1")
    #延时读数
    while GPIO.input(__gproEcho) == 0:
        start = time.time()
    print("measure--2")
    while GPIO.input(__gproEcho) == 1:
        stop = time.time()
    print("measure--3")
    #根据驱动公式计算测距结果
    elapsed = stop - start
    distance = (elapsed * 34300)/2

    return distance


if __name__ == '__main__':
    init()
    for i in range(60):
        print("srf05-start:", i)
        dis = measure()
        print('--------dis:', dis)
        sleep(2)