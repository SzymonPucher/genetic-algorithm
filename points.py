import numpy as np
import math
import csv

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
    p1, n1 = np.random.rand(2) * scope - scope/2 - 0.3, np.random.rand(2) * scope - scope/2 - 0.3
    xp, yp, xn, yn = [], [], [], []

    while amount > 0:
        alpha = 2 * math.pi * np.random.rand(1)
        r = np.random.rand(1) * scope/1.5 - 1
        x = r * math.cos(alpha) + p1[0]
        y = r * math.sin(alpha) + p1[1]
        xp.append(x)
        yp.append(y)

        alpha = 2 * math.pi * np.random.rand(1)
        r = np.random.rand(1) * scope/1.5 - 1
        x = r * math.cos(alpha) + n1[0]
        y = r * math.sin(alpha) + n1[1]
        xn.append(x)
        yn.append(y)

        amount = amount - 1

    positive = [xp, yp]
    negative = [xn, yn]

    return np.asarray(positive), np.asarray(negative)


def generate_to_csv(amount, scope):
    positive, negative = generate_points_random(amount, scope)
    csvfile = "data/pos_rand.csv"
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for i in range(len(positive[0])):
            writer.writerow([positive[0][i]] + [positive[1][i]])
    csvfile = "data/neg_rand.csv"
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for i in range(len(negative[0])):
            writer.writerow([negative[0][i]] + [negative[1][i]])


def get_points(name):
    x = []
    y = []
    with open(name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            x.append(row[0])
            y.append(row[1])
    positive = [x, y]
    return positive

