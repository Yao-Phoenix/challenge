from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import numpy as np

def linear_plot():
    data = [[5.06, 5.79], [4.92, 6.61], [4.67, 5.48], [4.54, 6.11], [4.26, 6.39],
            [4.07, 4.81], [4.01, 4.16], [4.01, 5.55], [3.66, 5.05], [3.43, 4.34],
            [3.12, 3.24], [3.02, 4.80], [2.87, 4.01], [2.64, 3.17], [2.48, 1.61],
            [2.48, 2.62], [2.02, 2.50], [1.95, 3.59], [1.79, 1.49], [1.54, 2.10], ]
    data = np.array(data)
    x = data[:, 0]
    y = data[:, 1]

    model = LinearRegression()
    model.fit(x.reshape(len(x), 1), y)
    w = model.coef_
    b = model.intercept_

    fig = plt.figure()
    
    x_temp = np.linspace(1, 6, 20)
    plt.scatter(x, y)
    plt.plot(x_temp, x_temp*w + b, c='r')
    plt.show()
    return w, b, fig

if __name__ == '__main__':
    linear_plot()
