# main.py

import numpy as np
import matplotlib.pyplot as plt
from mc_integrate import MCintegrate

def f(x):
    return x

area = MCintegrate(f, 0., 1., 50)
print("Area of the function f(x) = x from 0 to 1:", area)
