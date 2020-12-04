# Exchange Rate
'''
import bs4
import requests
import time
import winsound
import datetime

#floatFreq = [261.63, 293.66, 329.63, 349.23, 392, 440, 493.88, 523.25, 587.33]

while True:
    url = "https://www.x-rates.com/table/?from=SGD&amount=1"
    requestObj = requests.get(url)
    requestObj.raise_for_status()
    soup = bs4.BeautifulSoup(requestObj.text, 'html.parser')
    
    #exchange rate
    elements = soup.select("#content > div:nth-child(1) > div > div.col2.pull-right.module.bottomMargin > div.moduleContent > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(3) > a") # $69.90 
    currenttime = datetime.datetime.now()
    print(str(currenttime.strftime("%d-%b-%y %H:%M:%S")) + "\t Price: " + elements[0].text)
    
    if float(elements[0].text) >=1.331451:  # sound this if higher than this price
        winsound.Beep(int(261.63), 300)
        winsound.Beep(int(493.88), 300)
        winsound.Beep(int(493.88), 300)
        
    if float(elements[0].text) <1.331400: # sound this if lower than this price
        winsound.Beep(int(493.88), 300)
        winsound.Beep(int(261.63), 300)
        
    time.sleep(10)
    
'''

#Monitoring UOB stocks

import bs4
import requests
import time
import winsound
import datetime

buy_price = 22.01
num_shares = 1000

while True:
    url= "https://sg.finance.yahoo.com/quote/U11.SI?p=U11.SI&.tsrc=fin-srch"
    requestObj = requests.get(url)
    requestObj.raise_for_status()
    soup = bs4.BeautifulSoup(requestObj.text, 'html.parser')
    
    #UOB Share price
    elements = soup.select("#quote-header-info > div.My\(6px\).Pos\(r\).smartphone_Mt\(6px\) > div.D\(ib\).Va\(m\).Maw\(65\%\).Ov\(h\) > div > span.Trsdu\(0\.3s\).Fw\(b\).Fz\(36px\).Mb\(-4px\).D\(ib\)")
    profit = (float(elements[0].text)-buy_price) * num_shares
    currenttime = datetime.datetime.now()
    print(str(currenttime.strftime("%d-%b-%y %H:%M:%S")) + "\t Price: " + elements[0].text+ "\tProfit: $"+str(profit))
    
    if float(profit) >1000:  # sound this if profit higher than this price
        winsound.Beep(int(261.63), 300)
        winsound.Beep(int(493.88), 300)
        winsound.Beep(int(493.88), 300)
        
    if float(profit) <-1000: # sound this if loss more than this price
        winsound.Beep(int(493.88), 300)
        winsound.Beep(int(261.63), 300)

        


    time.sleep(10)
    
