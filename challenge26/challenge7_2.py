#!/usr/bin/env python3

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def co2_gdp_plot():
    data = pd.read_excel('ClimateChange.xlsx')
    # 处理 GDP 数据
    gdp = data[data['Series code'] == 'NY.GDP.MKTP.CD'].set_index('Country code')
    gdp.drop(gdp.columns[:5], axis=1, inplace=True)
    gdp.replace({'..': pd.np.nan}, inplace=True)
    gdp = gdp.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    gdp.replace({pd.np.nan: '0'}, inplace=True)

    # 处理 CO2 排放数据
    co2 = data[data['Series code'] == 'EN.ATM.CO2E.KT'].set_index('Country code')
    co2.drop(co2.columns[:5], axis=1, inplace=True)
    co2.replace({'..': pd.np.nan}, inplace=True)
    co2 = co2.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1) 
    co2.replace({pd.np.nan: '0'}, inplace=True)
    
    # 组合CO2排放和 GDP
    df = pd.concat([co2.sum(1), gdp.sum(1)], 1)
    df.columns = ['CO2-SUM', 'GDP-SUM']

    # MAX-MIX
    df_max_min = (df - df.min()) / (df.max() - df.min())

    # 获取归一后的CHINA的值
    china = []
    for i in df_max_min[df_max_min.index == 'CHN'].values:
        china.extend(np.round(i, 3).tolist())

    # 绘图
    labels, labels_pos = [], []
    for i in range(len(df_max_min)):
        if df_max_min.index[i] in ['CHN', 'USA', 'GBR', 'FRA', 'RUS']:
            labels.append(df_max_min.index[i])
            labels_pos.append(i)

    fig = plt.subplot()
    df_max_min.plot(kind='line', title='GDP-CO2', ax=fig)
    plt.xlabel('Countries')
    plt.ylabel('Values')
    plt.xticks(labels_pos, labels, rotation='vertical')
    plt.show()


    return fig, china

if __name__ == '__main__':
    print(co2_gdp_plot())
