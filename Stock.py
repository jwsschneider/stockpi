'''
Created on Mar 2, 2014

@author: jwschneider
'''

from bs4 import BeautifulSoup
import urllib.request
import time

class Stock(object):


    def __init__(self, ticker, quantity):
        self.ticker = ticker
        self.quantity = quantity
        self.opening_price = 0.0
        self.current_price = 0.0
        self.daily_gain = 0.0


    def update_price(self):
      
        time.sleep(3)

        url = 'http://finance.yahoo.com/q?s=' + self.ticker 
        
        source = urllib.request.urlopen(url).read()
        
        soup = BeautifulSoup(source)
        
        self.current_price = float(soup.find('span', {'class', 'time_rtq_ticker'}).contents[0].contents[0].replace(',', ''))
        
        self.open_price = float(soup.findAll('td', {'class', 'yfnc_tabledata1'})[1].contents[0].replace(',', ''))
        
        self.daily_gain = self.quantity * (self.current_price - self.open_price)
        
        
            
