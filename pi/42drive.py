#http_api.py coding:utf-8 42步进电机驱动

import RPi.GPIO as GPIO
import time
from time import ctime, sleep

__gproSrep  = 13
__gproDir   = 19
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(__gproSrep, GPIO.OUT)
    GPIO.setup(__gproDir, GPIO.OUT)

def run():
    GPIO.output(__gproDir, False)
    for i in range(10000):
        print('--------------step:', i)
        if i % 2 == 0:
            GPIO.output(__gproSrep, True)
        else:
            GPIO.output(__gproSrep, False)
        time.sleep(0.001)

if __name__ == '__main__':
    init()
    time.sleep(1)
    run()
    GPIO.cleanup()
