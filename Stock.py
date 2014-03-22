'''
Created on Mar 2, 2014

@author: jwsschneider

License: All of the code and supporting files in the stockpi git repository are licensed under the Creative Commons Attribution-ShareAlike 4.0 International Public License (https://creativecommons.org/licenses/by-sa/4.0/legalcode and https://creativecommons.org/licenses/by-sa/4.0/). Anyone is free to take and modify the files as long as the attribution to its original author is maintained and the modifier agrees to, in turn, license his/her modified files under the Creative Commons Attribution-ShareAlike 4.0 International Public License, too.

'''

from bs4 import BeautifulSoup # must have Beautiful Soup library installed
import urllib.request # for making http requests
import time

class Stock(object):


    def __init__(self, ticker, quantity):
        self.ticker = ticker
        self.quantity = quantity
        self.opening_price = 0.0
        self.current_price = 0.0
        self.daily_gain = 0.0

    
    '''
    This function updates the Stock's daily performance data by making a web request to Yahoo Finance
    (sorry, Yahoo Finance). All of this can be rewritten to pick out data from other web sources. If
    Yahoo Finance's HTML response page changes format, the Beautiful Soup portion of the code will
    have to be rewritten as well.
    '''
    def update_price(self):
      
        # take a 3-second break to avoid overloading Yahoo Finance
        time.sleep(3) 

        # build URL for http request
        url = 'http://finance.yahoo.com/q?s=' + self.ticker 
        
        # send HTTP request and pour response into source variable
        source = urllib.request.urlopen(url).read()
        
        # process the response with Beautiful Soup
        soup = BeautifulSoup(source)
        
        # grab current price of the stock from the soup (this part will need to be rewritten if Yahoo changes its HTML formatting)
        self.current_price = float(soup.find('span', {'class', 'time_rtq_ticker'}).contents[0].contents[0].replace(',', ''))
        
        # grab open price of the stock from the soup (this part will need to be rewritten if Yahoo changes its HTML formatting)
        self.open_price = float(soup.findAll('td', {'class', 'yfnc_tabledata1'})[1].contents[0].replace(',', ''))
        
        # compute the daily gain (even if negative) from the financial data
        self.daily_gain = self.quantity * (self.current_price - self.open_price)
        
        
            
