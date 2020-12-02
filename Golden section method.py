# -*- coding: utf-8 -*-

# 黄金分割法python实现
# f(x)=x^4 - 4x^3 - 6x^2 -16x +4极值
# 区间[-1,6] e=0.05

import numpy as np
import matplotlib.pyplot as plt

rate = 0.618034
pointset = []
x = 0
y = 0


def f(x):
    return 1.0*pow(x, 2) - x + 1
    #return 1.0 * (pow(x, 4) - 4 * pow(x, 3) - 6 * pow(x, 2) - 16 * x + 4)
# f(x)=x^4 - 4x^3 - 6x^2 -16x +4极值

def backtrace(f, a0, b0, accuracy):
    a = a0
    b = b0
    x2 = a + rate * (b - a)
    x1 = a + b - x2
    f2 = f(x2)
    f1 = f(x1)
    print
    x1, x2, '\n'
    arr = search(f, a, b, f1, f2, x1, x2, accuracy)
    printFunc(f, a, b, arr[0], arr[1])


def search(f, a, b, f1, f2, x1, x2, accuracy):
    if f1 <= f2:
        if x2 - a < accuracy:
            x = x1
            y = f1
            print
            x, y
            return (x, y)
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + b - x2
            f1 = f(x1)
            print
            x1, x2, '\n'
            return search(f, a, b, f1, f2, x1, x2, accuracy)

    else:
        if b - x1 < accuracy:
            x = x2
            y = f2
            print
            x, y
            return (x, y)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + b - x1
            f2 = f(x2)
            print
            x1, x2, '\n'
            return search(f, a, b, f1, f2, x1, x2, accuracy)


# 绘制函数图像

def printFunc(f, a, b, x, y):
    t = np.arange(a, b, 0.01)
    s = f(t)
    plt.plot(t, s)
    plt.plot([x], [y], 'ro')
    plt.show()


backtrace(f, -1, 6, 0.05)