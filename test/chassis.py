#coding:utf-8
__ispi = False
if(__ispi):
    import test_gpio.gpio as GPIO
else:
    import sys; 
    import os; 
    rootPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(rootPath)
    import test_gpio.gpio as GPIO
import time
#import RPi.GPIO as GPIO

#左右 速度与占空比的对应关系
_speedDc    = [
    [0, 0],      #0
    [50, 50],    #1
    [70, 70],    #2
    [75, 75],    #3
    [80, 80],    #4
    [85, 85],    #5
    [90, 90],    #6
    [93, 93],    #7
    [95, 95],    #8
    [98, 98],    #9
    [100, 100],    #10
]

class Chassis:
    def start(gpios):
        self.GpioEn       = gpios['en']
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GpioEn, GPIO.OUT)
        self.MotroLeft    = Motor({'front' : gpios['leftFront'], 'back' : gpios['leftBack'], 'en' : gpios['en']})
        self.MotroRight   = Motor({'front' : gpios['rightFront'], 'back' : gpios['rightBack'], 'en' : gpios['en']})
    
    def go(speed):
        dc = _speedDc[speed]
        self.MotroLeft.PmwFront.changeDc(dc);
            
class Motor:
    def __init__(self, gpios):
        self.GpioEn     = gpios['en']
        self.PmwFront   = Pmw(gpios['front'])
        self.PmwBack    = Pmw(gpios['back'])
        #TODO: 打开gpio
        
#    def go():
        

class Pmw:
    def __init__(self, gpio):
        self.Gpio       = gpio
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(clk, GPIO.OUT)
        self.Clk        = GPIO.PWM(clk, 50)
        self.Clk.start(0)
        
    def changeDc(dc):
        self.Clk.ChangeDutyCycle(dc)
        
    
if __name__ == '__main__':
    chassis = Chassis()
    chassis.start()
#    chassis.start({"en":12, "leftFront":13, "leftBack": 14, "rightFront": 15, "rightBack": 16})
    
    
# p = GPIO.PWM(channel, frequency) 创建一个 PWM 实例：
# p.start(dc)   # dc 代表占空比（范围：0.0 <= dc >= 100.0）
# p.ChangeFrequency(freq)   # freq 为设置的新频率，单位为 Hz
# p.ChangeDutyCycle(dc)  # 范围：0.0 <= dc >= 100.0
# p.stop() 停止 PWM：
