#chassis.py coding:utf-8 42 底盘电机的驱动

import RPi.GPIO as GPIO
import time

__gproEn        = 21    #使能信号
__gproPmw11     = 16
__gproPmw12     = 20
__gproPmw21     = 12
__gproPmw22     = 22
__ps            = []

def init():
    GPIO.setmode(GPIO.BCM)
    #使能信号
    GPIO.setup(__gproPmw11, GPIO.OUT)
    GPIO.output(__gproPmw11, True)
    GPIO.setup(__gproPmw11, GPIO.OUT)
    GPIO.setup(__gproPmw12, GPIO.OUT)
    GPIO.setup(__gproPmw21, GPIO.OUT)
    GPIO.setup(__gproPmw22, GPIO.OUT)
    p11 = GPIO.PWM(__gproPmw11, 50)
    p12 = GPIO.PWM(__gproPmw12, 50)
    p21 = GPIO.PWM(__gproPmw21, 50)
    p22 = GPIO.PWM(__gproPmw22, 50)
    __ps[0] = [p11, p12]
    __ps[1] = [p21, p22]
    # try:
    #     while 1:
    #         for dc in range(0, 101, 5):
    #             p.ChangeDutyCycle(dc);
    #             time.sleep(0.1)
    #         for dc in range(100, -1, -5):
    #             p.ChangeDutyCycle(dc);
    #             time.sleep(0.1)
    # except KeyboardInterrupt:
    #     pass
    # p.stop()
    # GPIO.cleanup()

def gohead(speed, t):
    __ps[0][0].start(speed)
    __ps[1][0].start(speed)
    time.sleep(t)
    __ps[0][0].stop()
    __ps[1][0].stop()

if __name__ == '__main__':
    init()
    gohead(50, 1);

# p = GPIO.PWM(channel, frequency) 创建一个 PWM 实例：
# p.start(dc)   # dc 代表占空比（范围：0.0 <= dc >= 100.0）
# p.ChangeFrequency(freq)   # freq 为设置的新频率，单位为 Hz
# p.ChangeDutyCycle(dc)  # 范围：0.0 <= dc >= 100.0
# p.stop() 停止 PWM：



