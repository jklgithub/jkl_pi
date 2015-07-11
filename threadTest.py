#coding=utf-8

import threading
import dbs
from time import ctime, sleep

def music(func):
    for i in range(10):
        dbs.a1 += 1
        print "music ~~ %s. %s ~ %s" %(func, ctime(), dbs.a1)
        sleep(1)

def move(func):
    for i in range(5):
        dbs.a1 += 1
        print "move  ~~ %s! %s ~ %s" %(func, ctime(), dbs.a1)
        sleep(2 )

threads = []
t1 = threading.Thread(target=music, args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move, args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
#    music(u'爱情买卖')
#    move(u'阿凡达')

    print "all over %s" %ctime()