import threading
import requests
import sys
import time
import os

prices = {}


if len(sys.argv) < 2:
    print('Supply symbols')
    quit()


for coin in sys.argv[1:]:
    prices[coin.lower()] = 0.00


def update_price(coin):
    while True:
        template = 'https://api.bittrex.com/api/v1.1/public/getticker?market={}-{}'

        pricing = requests.get(template.format('btc', coin)).json()
        prices[coin] = pricing['result']['Last']

        time.sleep(3)


for coin, price in prices.items():
    t = threading.Thread(target=update_price, args=(coin,))
    t.start()


while True:
    # os.system('cls' if os.name == 'nt' else 'clear')
    for coin, _ in prices.items():
        coin_price = prices[coin]
        coin_format = coin.ljust(5)
        print('{} -> {:8f}'.format(coin_format, coin_price))
    time.sleep(1)
