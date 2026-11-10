# My first linear model

#Эта модель вычисляет параметры линейной регрессии (веса \(w\) и \(b\)) 
#методом градиентного спуска, чтобы найти наилучшую прямую линию, 
#описывающую зависимость между массивами данных \(x\) и \(y\).

import numpy as np 

x = np.array([1, 2, 3])
y = np.array([3, 6, 9])
w = 0.0
b = 0.0
lr = 0.01

for step in range(1000):
    slope_w = (2 * (w * x + b - y) * x).mean()
    slope_b = (2 * (w * x + b - y)).mean()
    w = w - lr * slope_w
    b = b - lr * slope_b
    if step % 100 == 0:
        print(f"W:{w}, B:{b}")
print(f"W:{w}, B:{b}")

