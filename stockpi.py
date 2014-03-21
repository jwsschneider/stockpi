'''
Created on Mar 2, 2014

@author: jwschneider
'''

from Portfolio import Portfolio
import datetime
import RPi.GPIO as GPIO
import time

if __name__ == '__main__':
    pass


#setup GPIO using Board numbering
GPIO.setmode(GPIO.BOARD)

#setup GPIO output pins
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

def burnLED(color, sec):

	if (color=="blue"):
		pin = 7
	
	if (color=="green"):
		pin = 11
	
	if (color=="red"):
		pin = 13
		
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(sec)
	GPIO.output(pin, GPIO.LOW)


burnLED("blue", 1)


process_start = datetime.datetime.now()


portfolio = Portfolio('//home/pi/stockCheck/portfolio')


print ("--------------------------------------------------------------------")
print ("New process starting at ", datetime.datetime.now().date(), " @  ", datetime.datetime.now().time())
print ("--------------------------------------------------------------------")
print ("Total Portfolio Daily Gain = ", portfolio.daily_gain)
print ("--------------------------------------------------------------------")
print ("Stock Breakdown:\n")

for s in portfolio.stocks:
    print ("      ", s.ticker, "; Open = ", s.open_price, "; Current = ", s.current_price, ";  Daily Gain = ", s.daily_gain)

print ("--------------------------------------------------------------------")
print ("DONE. Total Process Time = ", (datetime.datetime.now() - process_start))
print ("--------------------------------------------------------------------")



if (portfolio.daily_gain < 0):
	burnLED("red", 300)
else:
	burnLED("green", 300)
	
	
GPIO.cleanup()


