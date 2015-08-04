#coding:utf-8

class Chassis:
	def __init__(gpios):
		self.GpioEn		= gpios['en']
		#TODO: 打开en的gpio
		self.MotroLeft	= Motor({'front' : gpios['leftFront'], 'back' : gpios['leftBack'], 'en' : gpios['en']})
		self.MotroRight	= Motor({'front' : gpios['rightFront'], 'back' : gpios['rightBack'], 'en' : gpios['en']})
	
class Motor:
	def __init(gpios):
		self.GpioEn		= gpios['en']
		self.GpioFront	= gpios['front']
		self.GpioBack	= gpios['back']
		#TODO: 打开gpio
		
	def go():
		


if __name__ == '__main__':
	chassis = Chassis()
	
	