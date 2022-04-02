import numpy as np
import matplotlib.pyplot as plt
import random as r
from math import pow

N = 100
x = np.random.randn(N)

delta = 0.2  # r.uniform(0.1, 2)
y = delta * np.random.randn(N) + x

plt.scatter(y, x, linewidths=4)

mean_x = np.average(x)
mean_y = np.average(y)

m = 0
numerator = 0
denominator = 0

for i in range(0, N):
    numerator = numerator + x[i] * y[i] - mean_y * x[i]
    denominator = denominator + x[i] * x[i] - mean_x * x[i]

m = numerator / denominator

c = mean_y - m * mean_x  # Intercept

Y = m * x + c

plt.plot(Y, x)
plt.show()

# Sum of Squared Error

e = 0
y_cap = Y
for i in range(0, N):
    e = e + pow((y_cap[i] - y[i]), 2)

# print("Slope of line : {}\nIntercept of line : {}\nSSE Error : {}\n".format(m, c, e))

######
delta = 0.0
for i in range(11):
    N = 100
    x = np.random.randn(N)
    y = delta * np.random.randn(N) + x
    mean_x = np.average(x)
    mean_y = np.average(y)
    m = 0
    numerator = 0
    denominator = 0
    for i in range(0, N):
        numerator = numerator + x[i] * y[i] - mean_y * x[i]
        denominator = denominator + x[i] * x[i] - mean_x * x[i]
    m = numerator / denominator
    c = mean_y - m * mean_x  # Intercept
    Y = m * x + c
    e = 0
    y_cap = Y
    for i in range(0, N):
        e = e + pow((y_cap[i] - y[i]), 2)
    print("Slope of line : {}\nIntercept of line : {}\nSSE Error : {}\n".format(m, c, e))
    delta += 0.2
