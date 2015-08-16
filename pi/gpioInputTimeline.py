#coding:utf-8 专职定时读取gpio
import RPi.GPIO as GPIO
import time
import datetime
import event
from time import ctime, sleep

__inputs    = {} #{‘see’: 是否监听, ‘event_key’: #发生变化时的触发时间, 'now': 当前的值, ‘last’:上一次输出的值, 'time0': 上次发生变化的事件}

def init():
    while(True):
        print('init-while: ', __inputs)
        for gpio in __inputs:
            inp         = __inputs[gpio]
            v           = GPIO.input(gpio)
            inp['now']  = v;
            print('timeline: ', v)
            if inp['see'] and v != inp['last']:
                __inputs[gpio]['last'] = v;
                event.trigger(inp['event_key'], {
                    'gpio'  : gpio,
                    'now'   : v,
                    'time0' : inp['time0']
                })
                __inputs[gpio]['time0']   = datetime.datetime.now()
        # time.sleep(0.0001)
        time.sleep(0.1)

def register(gpio, eventKey):
    GPIO.setup(gpio, GPIO.IN)
    v           = GPIO.input(gpio)
    __inputs[gpio]  = {
        'see'       : True,
        'event_key' : eventKey,
        'time0'     : datetime.datetime.now(),
        'now'       : v,
        'last'      : v
    }
    print('register: ', __inputs)

def pause(gpio):
    __inputs[gpio]['see']   = False

def regain(gpio):
    __inputs[gpio]['see']   = True

