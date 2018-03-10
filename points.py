import numpy as np
import math

def generate_points_random(amount):
    amount = math.floor(amount / 2)
    positive = np.random.random((2, amount)) * 2 - 1
    negative = np.random.random((2, amount)) * 2 - 1
    return positive, negative


def generate_points_fx(amount):
    arr = np.random.random((amount, 2)) * 2 - 1
    xp, yp, xn, yn = [], [], [], []
    for i in range(amount):
        if arr[i][0] - arr[i][1] < 0:
            xp.append(arr[i][0])
            yp.append(arr[i][1])
        else:
            xn.append(arr[i][0])
            yn.append(arr[i][1])
    positive = [xp, yp]
    negative = [xn, yn]

    return np.asarray(positive), np.asarray(negative)


def generate_points_radius(amount):
    amount = math.floor(amount / 2)
    p1, n1 = np.random.rand(2), np.random.rand(2) * 2 - 1
    xp, yp, xn, yn = [], [], [], []


    while amount > 0:
        alpha = 2 * math.pi * np.random.rand(1)
        r = np.random.rand(1)
        x = r * math.cos(alpha) + p1[0]
        y = r * math.sin(alpha) + p1[1]
        xp.append(x)
        yp.append(y)

        alpha = 2 * math.pi * np.random.rand(1)
        r = np.random.rand(1)
        x = r * math.cos(alpha) + n1[0]
        y = r * math.sin(alpha) + n1[1]
        xn.append(x)
        yn.append(y)

        amount = amount - 1

    positive = [xp, yp]
    negative = [xn, yn]

    return np.asarray(positive), np.asarray(negative)