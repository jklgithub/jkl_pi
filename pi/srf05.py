#app.py coding:utf-8 srf05超声测距模块驱动
import RPi.GPIO as GPIO
import time
from time import ctime, sleep

__gproTrig = 16
__gproEcho = 20
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(__gproTrig, GPIO.OUT)
    GPIO.setup(__gproEcho, GPIO.In)


def measure():
    #启动测距
    GPIO.output(__gproTrig, True)
    time.sleep(0.00001)
    GPIO.output(__gproTrig, False)
    start = time.time()
    #延时读书
    while GPIO.input(__gproEcho) == 0:
        start = time.time()
    while GPIO.input(__gproEcho)==1:
        stop = time.time()
    #根据驱动公式计算测距结果
    elapsed = stop-start
    distance = (elapsed * 34300)/2

    return distance


if __name__ == '__main__':
    for i in range(60):
        print("srf05-start:", i)
        dis = measure()
        print('--------dis:', dis)
        sleep(1)