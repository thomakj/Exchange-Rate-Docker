from math import pi
# from bokeh.plotting import figure, show, output_file
from datetime import datetime

import pandas as pd
import requests, json

class Exchange:
    """https://openexchangerates.org/api/"""
    def __init__(self):
        with open('/tmp/openexchangerates.conf', 'r') as f:
            config = json.load(f)
        self.APP_ID = config['APP_ID']

    def requestLatest(self, base):
        url = 'https://openexchangerates.org/api/latest.json?app_id=%s' %(self.APP_ID)
        #print url
        r = requests.get(url)
        return r.json()

    def requestHistorical(self, timestamp):
        url = 'https://openexchangerates.org/api/historical/%s.json?app_id=%s' %(timestamp, self.APP_ID)
        r = requests.get(url)
        return r.json()

    def requestTimeSeries(self, start, end, symbols):
        url = "https://openexchangerates.org/api/historical/time-series.json?app_id={0}&start={1}&end={2}&symbols={3}".format(self.APP_ID, start, end, symbols)
        print(url)
        r = requests.get(url)
        return r.json()

class Graph:
    """Graphing of stocks and exchange rates."""
    def __init__(self):
        pass

    def stock(self, df):
        df = pd.DataFrame(df)
        df["date"] = pd.to_datetime(df["date"])

        inc = df.close > df.open
        dec = df.open > df.close
        w = 12*60*60*1000 # half day in ms

        TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

        p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title = "MSFT Candlestick")
        p.xaxis.major_label_orientation = pi/4
        p.grid.grid_line_alpha=0.3

        p.segment(df.date, df.high, df.date, df.low, color="black")
        p.vbar(df.date[inc], w, df.open[inc], df.close[inc], fill_color="#D5E1DD", line_color="black")
        p.vbar(df.date[dec], w, df.open[dec], df.close[dec], fill_color="#F2583E", line_color="black")

        output_file("candlestick.html", title="candlestick.py example")

        show(p)  # open a browser

if __name__ == '__main__':
    e = Exchange()
    today = datetime.today().strftime("%Y-%M-%d")
    # g = Graph()
    #print(e.requestTimeSeries("2018-05-01", today, "NOK"))
    print(e.requestLatest("NOK"))
