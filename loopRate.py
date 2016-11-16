from time import time
from time import sleep
from datetime import datetime

class LoopRate():
	def __init__(self,rate):
		self.rate = rate
		if rate<=1 : print 'Please try with a rate greater than 1'
	def __enter__(self):
		self.startTime = datetime.now()
		return self
	def __exit__(self,type,value,traceback):
		difference = datetime.now() - self.startTime
		while(difference.microseconds/1000000.0 <1.0/self.rate):
			difference = datetime.now() - self.startTime
			pass
		print 1/(difference.microseconds/1000000.0)

if __name__ == "__main__":
	for i in range(10):
		#print datetime.now()
		with LoopRate(1000):
			for i in range(1000):
				pass
