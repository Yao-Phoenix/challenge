#!/usr/bin/env python3
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def data_plot():
    data = pd.read_json('user_study.json')
    df = data.groupby('user_id').sum()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('StudyData')
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
    ax.plot(df.index, df.minutes)

    plt.show()

    return ax

if __name__ == '__main__':
    data_plot()

