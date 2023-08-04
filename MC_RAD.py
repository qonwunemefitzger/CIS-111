# verification.py
from Mc_double import MonteCarlo_double

def f(x, y):
    return x**2 + y**2

def g(x, y):
    return x**2 + y**2 - 1.5**2

x0, x1 = -1.5, 1.5
y0, y1 = -1.5, 1.5
n = 1000

circle_area = MonteCarlo_double(f, g, x0, x1, y0, y1, n)
print("Area of the circle with radius 1.5:", circle_area)
