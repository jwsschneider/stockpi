'''
Created on Mar 2, 2014

@author: jwsschneider

License: All of the code and supporting files in the stockpi git repository are licensed under the Creative Commons Attribution-ShareAlike 4.0 International Public License (https://creativecommons.org/licenses/by-sa/4.0/legalcode and https://creativecommons.org/licenses/by-sa/4.0/). Anyone is free to take and modify the files as long as the attribution to its original author is maintained and the modifier agrees to, in turn, license his/her modified files under the Creative Commons Attribution-ShareAlike 4.0 International Public License, too.

'''

from Portfolio import Portfolio
import datetime
import time
import RPi.GPIO as GPIO


if __name__ == '__main__':
    pass


#setup GPIO using Board numbering
GPIO.setmode(GPIO.BOARD)

#setup GPIO output pins
GPIO.setup(7, GPIO.OUT) # for the blue LED
GPIO.setup(11, GPIO.OUT) # for the green LED
GPIO.setup(13, GPIO.OUT) # for the red LED

'''
Simple function that takes an LED color and number of seconds to let it burn. It could be improved
by spawning this functionality as an independent thread.

color = either "blue", "green" or "red"
sec = number of seconds you want the LED to burn for

'''
def burnLED(color, sec):

	if (color=="blue"):
		pin = 7
	
	if (color=="green"):
		pin = 11
	
	if (color=="red"):
		pin = 13
		
	GPIO.output(pin, GPIO.HIGH) # light up the LED!
	time.sleep(sec) # wait
	GPIO.output(pin, GPIO.LOW) # turn the LED off


# blink the blue LED to tell the user that the process has begun
burnLED("blue", 1)

# measure the moment that the process started
process_start = datetime.datetime.now()


'''
Load the "portfolio" file. The portfolio file is simple. It lists the stock ticker, followed by a space,
followed by the number of shares you hold in the stock. Example:

	AAPL 19
	MSFT 81

The user holds 19 shares of Apple and 81 shares of Microsoft.
'''
portfolio = Portfolio('//home/pi/stockpi/portfolio')


# Text output that details the status of each individual stock, as well as te starting and stop times. The user will never seen this background info, but it's good for the logs.
print ("--------------------------------------------------------------------")
print ("New process starting at ", datetime.datetime.now().date(), " @  ", datetime.datetime.now().time())
print ("--------------------------------------------------------------------")
print ("Total Portfolio Daily Gain = ", portfolio.daily_gain)
print ("--------------------------------------------------------------------")
print ("Stock Breakdown:\n")

# Iterate over all of the stocks, output how they are doing in detail.
for s in portfolio.stocks:
    print ("      ", s.ticker, "; Open = ", s.open_price, "; Current = ", s.current_price, ";  Daily Gain = ", s.daily_gain)

print ("--------------------------------------------------------------------")
print ("DONE. Total Process Time = ", (datetime.datetime.now() - process_start))
print ("--------------------------------------------------------------------")


# If the portfolio is down on the day, burn the red LED. Otherwise, burn the green LED. A break-even day is green!
if (portfolio.daily_gain < 0):
	burnLED("red", 300)
else:
	burnLED("green", 300)
	

# Always cleanup the GPIO to put out any stray LEDs or electrical signals.
GPIO.cleanup()


