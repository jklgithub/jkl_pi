#coding:utf-8 电机控制类
import sys;
import os;
rootPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(rootPath)
import pi.gpioInputTimeline as gpioInputTimeline
import pi.event as event
import RPi.GPIO as GPIO

class Motor:
    def __init__(self, gpioOut1, gpioOut2, gpioIn):
        self.freq       = 50
        self.gpioOut1   = gpioOut1  #pwm1
        self.gpioOut2   = gpioOut2  #pwm2
        self.gpioIn     = gpioIn    #
        self.out1Run    = False
        self.out2Run    = False
        # GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpioOut1, GPIO.OUT)
        GPIO.setup(self.gpioOut2, GPIO.OUT)
        # GPIO.setup(self.gpioIn, GPIO.In)
        self.out1       = GPIO.PWM(self.gpioOut1, self.freq)
        self.out2       = GPIO.PWM(self.gpioOut2, self.freq)
        self.mileage    = 0
        evKey           = 'input_' + str(self.gpioIn) + '_change'
        event.bind(evKey, self.mileageChange)
        gpioInputTimeline.register(self.gpioIn, evKey)

    def mileageChange(self, ev):
        if(self.out1Run):
            self.mileage    = self.mileage + 1
            print('mileageChange', self.gpioIn, ':', self.mileage, 'self.out1_l:', self.out1_l, ev)
            if self.out1Run and self.mileage >= self.out1_l:
                self.out1.stop()
        if(self.out2Run):
            self.mileage    = self.mileage - 1
            print('mileageChange', self.gpioIn, ':', self.mileage, 'self.out1_l:', self.out2_l, ev)
            if self.out2Run and self.mileage >= self.out2_l:
                self.out2.stop()

    def gohead(self, speed, l):
        print('gohead', self.gpioIn, ':', speed, 'self.out1_l:', l)
        self.out2.stop()
        self.out1.start(speed)
        self.out1Run    = True
        self.out2Run    = False
        self.out1_l     = self.mileage + l

    def retreat(self, speed, l):
        self.out1.stop()
        self.out2.start(speed)
        self.out1Run    = False
        self.out2Run    = True
        self.out2_l     = self.mileage - l

    def stop(self):
        self.out1.stop()
        self.out2.stop()
        self.out1Run    = False
        self.out2Run    = False

if __name__ == '__main__':
    motor1  = Motor(19, 16, 13)
    motor2  = Motor(12, 6, 26)


