import math
import numpy as np
import matplotlib.pyplot as plt


def diff(nodes, values, left, right):
    if nodes[left] == nodes[right]:
        return values[left] / math.factorial(right - left)
    return (diff(nodes, values, left + 1, right) - diff(nodes, values, left, right - 1)) / (nodes[right] - nodes[left])


def hermite(nodes, values, x):
    result = 0
    product = 1

    for i in range(len(values)):
        result += diff(nodes, values, 0, i) * product
        product *= (x - nodes[i])
    return result
