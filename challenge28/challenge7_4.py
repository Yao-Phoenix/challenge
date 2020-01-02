#!/usr/bin/env python3
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression as lr

def Temperature():
    temp = pd.read_csv('GlobalSurfaceTemperature.csv')
    temp = temp.iloc[:, 1:].set_index(
            pd.to_datetime(temp.Year.astype('str')))

    gas = pd.read_csv('GreenhouseGas.csv')
    gas = gas.iloc[:, 1:].set_index(
            pd.to_datetime(gas.Year.astype('str')))

    co2 = pd.read_csv('CO2ppm.csv')
    co2 = co2.iloc[:, 1:].set_index(
            pd.to_datetime(co2.Year.astype('str')))

    df = pd.concat([gas, co2, temp], 1)
    gas_part = df.iloc[:, :4].fillna(method='ffill').fillna(method='bfill')
    data = gas_part['1970': '2010']
    test = gas_part['2011': '2017']

    model_median = lr().fit(data, df['1970': '2010'].Median)
    median = pd.np.round(model_median.predict(test), 3)
    model_upper = lr().fit(data, df['1970': '2010'].Upper)
    upper = pd.np.round(model_upper.predict(test), 3)
    model_lower = lr().fit(data, df['1970': '2010'].Lower)
    lower = pd.np.round(model_lower.predict(test), 3)
    return list(upper), list(median), list(lower)

if __name__ == '__main__':
    Temperature()







