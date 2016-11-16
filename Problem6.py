#!/usr/bin/python

import numpy as np
from scipy.linalg import toeplitz

def square_diff(num):
    s = num*(num+1)/2
    s2 = num*(num+1)*(2*num+1)/6

    return s**2 -s2

print(square_diff(100))


