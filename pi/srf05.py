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
    GPIO.output(__gproTrig, False)
    time.sleep(0.0001)
    GPIO.output(__gproTrig, True)
    time.sleep(0.00001)
    GPIO.output(__gproTrig, False)
   # start = time.time()
  #  print("measure--1--", GPIO.input(__gproEcho))
    #延时读数
  #  while GPIO.input(__gproEcho) == 0:
  #      start = time.time()
  #  print("measure--2")
  #  while GPIO.input(__gproEcho) == 1:
  #      stop = time.time()
  #  print("measure--3")

    start   = 0
    stop    = 0
    while start == 0 or stop == 0:
        #    print("measure----1--:", time.time(), ", GPIO.input:", GPIO.input(__gproEcho))
        val     = GPIO.input(__gproEcho)
        if stop == 0 and start == 0 and val == 1:
   #         print("measure--2")
            start = time.time()
        if start > 0 and stop == 0 and val == 0:
      #      print("measure--3")
            stop = time.time()
    #根据驱动公式计算测距结果
    elapsed = stop - start
 #   print("measure--4:start:", start, "  stop:", stop, '  elapsed:', elapsed)
    distance = (elapsed * 34300)/2

    return distance


if __name__ == '__main__':
    init()
    for i in range(300):
     #   print("srf05-start:", i)
        dis = measure()
        print('--------------dis:', dis)
        sleep(1)