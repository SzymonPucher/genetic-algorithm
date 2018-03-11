import numpy as np
import math

def generate_points(amount, scope, p_type):
    if p_type == 1:
        return generate_points_random(amount, scope)
    if p_type == 2:
        return generate_points_fx(amount, scope)
    if p_type == 3:
        return generate_points_radius(amount, scope)

def generate_points_random(amount, scope):
    amount = math.floor(amount / 2)
    positive = np.random.random((2, amount)) * scope - scope/2
    negative = np.random.random((2, amount)) * scope - scope/2
    return positive, negative


def generate_points_fx(amount, scope):
    arr = np.random.random((amount, 2)) * scope - (scope / 2)
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


def generate_points_radius(amount, scope):
    amount = math.floor(amount / 2)
    scope = scope * 0.35 + 1.3
    p1, n1 = np.random.rand(2) * scope - scope/2, np.random.rand(2) * scope - scope/2
    xp, yp, xn, yn = [], [], [], []

    while amount > 0:
        alpha = 2 * math.pi * np.random.rand(1)
        r = np.random.rand(1) * scope/2
        x = r * math.cos(alpha) + p1[0]
        y = r * math.sin(alpha) + p1[1]
        xp.append(x)
        yp.append(y)

        alpha = 2 * math.pi * np.random.rand(1)
        r = np.random.rand(1) * scope/2
        x = r * math.cos(alpha) + n1[0]
        y = r * math.sin(alpha) + n1[1]
        xn.append(x)
        yn.append(y)

        amount = amount - 1

    positive = [xp, yp]
    negative = [xn, yn]

    return np.asarray(positive), np.asarray(negative)