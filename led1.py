import RPi.GPIO as GPIO
import time

def start1():
    l1 = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(l1, GPIO.OUT)
    for i in xrange(100):
        if i % 2 == 0:
            GPIO.output(l1, GPIO.HIGH)
        else:
            GPIO.output(l1, GPIO.LOW)
        time.sleep(1)
    GPIO.cleanup()
    return

if __name__ == '__main__':
    start1()
