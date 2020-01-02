#!usr/bin/env python3

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def climate_plot():
    df_temperature = pd.read_excel('GlobalTemperature.xlsx')
    df_data = pd.read_excel('ClimateChange.xlsx')
    df_gases = df_data[df_data['Series code'].isin([
        'EN.ATM.CO2E.KT', 'EN.ATM.METH.KT.CE', 'EN.ATM.NOXE.KT.CE',
        'EN.ATM.GHGO.KT.CE', 'EN.CLC.GHGR.MT.CE'])].iloc[:, 6:-1]
    df_gases.replace({'..':pd.np.nan}, inplace=True)
    df_gases = df_gases.fillna(method='ffill', axis=1).fillna(
            method='bfill', axis=1).sum()
    df_gases = pd.DataFrame(
            df_gases.values, index=df_gases.index, columns=['Total GHG'])
    
    df_gt = df_temperature.iloc[:, [1, 4]].set_index(
            pd.to_datetime(df_temperature.Date))
    df_gt.fillna(0, inplace=True)
    df_gt_y = df_gt.resample('a').mean()['1990': '2010']
    df_gt_q = df_gt.resample('q').mean()
    df = pd.concat([df_gt_y.set_index(df_gases.index), df_gases], axis=1)
    df = (df - df.min()) / (df.max() - df.min())
    

    fig, axes = plt.subplots(nrows=2, ncols=2)
    ax1 = df.plot(kind='line', figsize=(16, 9), ax=axes[0, 0], xticks=df.index)
    ax1.set_xlabel('Years')
    ax1.set_ylabel('Values')
    ax1.set_xticklabels(df.index, rotation=90)

    ax2 = df.plot(kind='bar', figsize=(16, 9), ax=axes[0, 1])
    ax2.set_xlabel('Years')
    ax2.set_ylabel('Values')

    ax3 = df_gt_q.plot(kind='area', figsize=(16, 9), ax=axes[1, 0])
    ax3.set_xlabel('Quarters')
    ax3.set_ylabel('Temperature')

    ax4 = df_gt_q.plot(kind='kde', figsize=(16, 9), ax=axes[1, 1])
    ax4.set_label('Values')
    ax4.set_label('Values')
    plt.show()
    return fig

if __name__ == '__main__':
    climate_plot()
