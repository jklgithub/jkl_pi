import RPi.GPIO as GPIO
import time

def start1():
    l1 = 26
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(l1, GPIO.IN)
    for i in xrange(100):
        n1 = GPIO.input(l1)
        print(n1)
        time.sleep(1)
    GPIO.cleanup()
    return

if __name__ == '__main__':
    start1()
