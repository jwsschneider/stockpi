'''
Created on Mar 8, 2014

@author: jwschneider
'''
from Stock import Stock

class Portfolio(object):

    def __init__(self, input_file):
        
        self.stocks = []
        
        self.size = 0
        
        
        for line in open(input_file,'r').readlines():       
            
            self.stocks.append(Stock(line.split()[0], int(line.split()[1])))
            
            self.size += 1
        
        
        self.daily_gain = 0.0
        
        for i in range(0, self.size):
            self.stocks[i].update_price()
            self.daily_gain += self.stocks[i].daily_gain
            
            
        def update_daily_gain(self):
        
            self.daily_gain = 0.0
            
            for i in range(0, self.size):
                self.stocks[i].update_price()
                self.daily_gain += self.stocks[i].daily_gain
                
