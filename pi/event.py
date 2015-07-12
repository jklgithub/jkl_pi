#event.py coding:utf-8 事件调度中心
import time
import datetime

#以一定的事件间隔，调用传入函数
def start(second):
    l = second * 1000
    while l > 0:
  #      now = datetime.datetime.now()
  #      print(l, ': ', now.strftime('%b-%d-%y %H:%M:%S'), ' ',  now.microsecond)
        #时序触发  每毫秒触发一次的事件
        trigger('hz_1000', {})
        l -= 1
        time.sleep(0.001)   #时钟精度，1000HZ

__es = {}
def trigger(event_key, p):
    if(event_key in __es and len(__es[event_key]) > 0):
        for s in __es[event_key]:
            s(p)

def bind(evnet_key, func):
    if(evnet_key not in __es):
        __es[evnet_key] = []
    __es[evnet_key].append(func)

def test1(p):
    print('----test1:', p)

def test2(p):
    print('----test2:', p)

if __name__ == '__main__':
#    start(5)
    bind('e1', test1)
    bind('e1', test2)
    bind('e2', test2)
    time.sleep(1)
    trigger('e1', 'trigger1')
    trigger('e2', 'trigger1')
    time.sleep(2)
    trigger('e1', 'trigger2')
