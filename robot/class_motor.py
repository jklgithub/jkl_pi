#coding:utf-8 电机控制类
__ispi = False
if(__ispi):
    import RPi.GPIO as GPIO
else:
    import sys;
    import os;
    rootPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(rootPath)
    import test_gpio.gpio as GPIO

class Motor:
    def __init__(self, gpioOut1, gpioOut2, gpioIn):
        self.freq       = 50
        self.gpioOut1   = gpioOut1  #pwm1
        self.gpioOut2   = gpioOut2  #pwm2
        self.gpioIn     = gpioIn    #
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpioOut1, GPIO.OUT)
        GPIO.setup(self.gpioOut2, GPIO.OUT)
        GPIO.setup(self.gpioIn, GPIO.In)
        p11 = GPIO.PWM(self.gpioOut1, self.freq)
        p12 = GPIO.PWM(self.gpioOut2, self.freq)

    def gohead(self, speed):
        self.gpioOut2.stop()
        self.gpioOut1.start(speed)

    def retreat(self, speed):
        self.gpioOut1.stop()
        self.gpioOut2.start(speed)

    def stop(self):
        self.gpioOut1.stop()
        self.gpioOut2.stop()

if __name__ == '__main__':
    motor1  = Motor(19, 16, 13)
    motor2  = Motor(12, 6, 26)


