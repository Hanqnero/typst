import pandas as pd

frame = pd.read_csv('../sup/data.csv')
frame["Date"] = pd.to_datetime(frame["Date"])
frame["Average"] = (frame['Open']+frame['Close']+frame['High']+frame['Low']) / 4
subset = frame[frame["Date"] > pd.to_datetime("2016-12-31")]

time = dict(
    minute=1,
    hour  =60,
    day   =60*24,
    week  =60*24*7,
    month =60*24*30,
    year  =60*24*365
)