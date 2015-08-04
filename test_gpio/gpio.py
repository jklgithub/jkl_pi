#gpiotest coding:utf-8

BCM		= "gpio.bcm"
OUT		= "gpio.out"

def setmode(m):
    print "GPIO.setmode", m
    
def setup(m1, m2):
    print "GPIO.setup", m1, m2
    
    