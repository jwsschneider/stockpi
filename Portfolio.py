'''
Created on Mar 8, 2014

@author: jwsschneider

License: All of the code and supporting files in the stockpi git repository are licensed under the Creative Commons Attribution-ShareAlike 4.0 International Public License (https://creativecommons.org/licenses/by-sa/4.0/legalcode and https://creativecommons.org/licenses/by-sa/4.0/). Anyone is free to take and modify the files as long as the attribution to its original author is maintained and the modifier agrees to, in turn, license his/her modified files under the Creative Commons Attribution-ShareAlike 4.0 International Public License, too.

'''

from Stock import Stock

class Portfolio(object):

    def __init__(self, input_file):
        
        self.stocks = [] # A Portfolio object can hold any number of Stock objects
        
        self.size = 0 # Total number of Stock objects in a Portfolio object
        
        # Grab input from "portfolio" file, where each line takes the form of '[STOCK TICKER] [NUM SHARES]'
        for line in open(input_file,'r').readlines():       
            
            # Instantiate a Stock object
            self.stocks.append(Stock(line.split()[0], int(line.split()[1])))
            
            self.size += 1
        
        
        self.daily_gain = 0.0
        
        for i in range(0, self.size):
            self.stocks[i].update_price() # This actually performs a web call to grab the stock's daily performance
            self.daily_gain += self.stocks[i].daily_gain # Build daily gain (in dollars)
            
    
    '''
    Update the Portfolio's daily_gain by performing web calls for each stock.
    This function is never utilized because stockpi only runs once, but could
    be useful if stockpi was modified to run for longer periods. In those cases
    a Portfolio refresh would be useful.
    '''
    def update_daily_gain(self):
    
        self.daily_gain = 0.0
        
        for i in range(0, self.size):
            self.stocks[i].update_price() # This actually performs a web call to grab the stock's daily performance
            self.daily_gain += self.stocks[i].daily_gain # Build daily gain (in dollars)
                
