#app.py coding:utf-8 树莓派应用入口
import sys;
import os;
rootPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(rootPath)
import pi.gpioInputTimeline as gpioInputTimeline
import pi.event as event
import RPi.GPIO as GPIO
import threading
import time
# import srf05
# from time import ctime, sleep

def init():
    GPIO.setmode(GPIO.BCM)

def test1():
    print('test1-start')
    event.bind('input_13_change', inputChange)
    event.bind('input_26_change', inputChange)
    gpioInputTimeline.register(13, 'input_13_change')
    gpioInputTimeline.register(26, 'input_26_change')
    print('test1-end')

def inputChange(p):
    print(p)

def gpioInputTimelineStart():
    print('gpioInputTimelineStart-start')
    gpioInputTimeline.init()
    print('gpioInputTimelineStart-end')

threads = []
t1 = threading.Thread(target=gpioInputTimelineStart, args=())
threads.append(t1)
t2 = threading.Thread(target=test1, args=())
threads.append(t2)

if __name__ == '__main__':
    print('main-1')
    GPIO.cleanup()
    print('main-2')
    init()
    print('main-3')
    for t in threads:
        print('main-4', t)
        t.setDaemon(True)
        t.start()
    print('main-5')
    t.join()
    print('main-5')
    try:
        print('main-6')
        while 1:
            print('main~')
            time.sleep(1)
    except KeyboardInterrupt:
        print('main-7-KeyboardInterrupt')
        pass

    GPIO.cleanup()
    print('main-8-over')




#def hz1000(p):
#    print('hz1000~~')

# def view_distance(p):
#     print('--------view_distance:', p)
#
# def eventsInit():
#     event.bind('srf05_dis', view_distance)
#     print('----eventsInit ok----')
#
# def events():
#     eventsInit()
#     event.start(60)
#
# # def time2():
#     # srf05.init()
#     # for i in range(60):
#     #     print("srf05-start:", i)
#         # dis = srf05.measure()
#         # print('--------dis:', dis)
#         # event.trigger('srf05_dis', dis)
#         # sleep(1)
#
# threads = []
# t1 = threading.Thread(target=events, args=())
# threads.append(t1)
# t2 = threading.Thread(target=time2, args=())
# threads.append(t2)
#
# if __name__ == '__main__':
#     for t in threads:
#         t.setDaemon(True)
#         t.start()
#     t.join()
