from math import pi
from datetime import datetime

import pandas as pd
import requests, json

class Exchange:
    """https://openexchangerates.org/api/"""
    def __init__(self):
        with open('/tmp/openexchangerates.conf', 'r') as f:
            config = json.load(f)
        self.APP_ID = config['APP_ID']

    def request_latest(self, base):
        url = 'https://openexchangerates.org/api/latest.json?app_id=%s' %(self.APP_ID)
        r = requests.get(url)
        return r.json()

    def request_historical(self, timestamp):
        url = 'https://openexchangerates.org/api/historical/%s.json?app_id=%s' %(timestamp, self.APP_ID)
        r = requests.get(url)
        return r.json()

    def request_time_series(self, start, end, symbols):
        url = "https://openexchangerates.org/api/historical/time-series.json?app_id={0}&start={1}&end={2}&symbols={3}".format(self.APP_ID, start, end, symbols)
        print(url)
        r = requests.get(url)
        return r.json()


if __name__ == '__main__':
    e = Exchange()
    today = datetime.today().strftime("%Y-%M-%d")
    print(e.request_latest("NOK"))
