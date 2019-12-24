#!/usr/bin/env python3
import pandas as pd

def quarter_volume():
    data = pd.read_csv('apple.csv', header=0)
    s = pd.Series(list(data.Volume), index=pd.to_datetime(data.Date))
    second_volumn = s.resample('q').sum().sort_values()[-2]
    return second_volumn

if __name__ == '__main__':
    quarter_volume()
