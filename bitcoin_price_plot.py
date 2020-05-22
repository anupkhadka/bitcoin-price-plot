#!/usr/bin/env python 

from datetime import date
import json
import matplotlib.pyplot as plt
import requests

date_list = []
price_list = []

today = date.today()
today = today.strftime("%Y-%m-%d")

# pull in json data of bitcoin price from Jan 1, 2020 to today from api.coindesk.com
url = f'https://api.coindesk.com/v1/bpi/historical/close.json?start=2020-01-01&end={today}' 
response = requests.get(url)
data = response.json()
date_price_dict = data['bpi']

for date,price in date_price_dict.items():
  date_list.append(date)
  price_list.append(price)

plt.plot(date_list, price_list)
plt.title(f'Bitcoin price change from 2020-01-01 to {today}')
plt.show()
