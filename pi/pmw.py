#coding:utf-8 脉宽调制(PWM)输出
import time
import RPi.GPIO as GPIO

def init(gpi):
    GPIO.setmode(GPIO.BCM)
    #使能信号
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, False)
    GPIO.setup(gpi, GPIO.OUT)
    p = GPIO.PWM(gpi, 50)
    p.start(0)
    try:
        while 1:
            for dc in range(0, 101, 5):
                p.ChangeDutyCycle(dc);
                time.sleep(0.1)
            for dc in range(100, -1, -5):
                p.ChangeDutyCycle(dc);
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    p.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    init(12)



# p = GPIO.PWM(channel, frequency) 创建一个 PWM 实例：
# p.start(dc)   # dc 代表占空比（范围：0.0 <= dc >= 100.0）
# p.ChangeFrequency(freq)   # freq 为设置的新频率，单位为 Hz
# p.ChangeDutyCycle(dc)  # 范围：0.0 <= dc >= 100.0
# p.stop() 停止 PWM：