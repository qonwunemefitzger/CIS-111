# verification.py
from Mc_double import MonteCarlo_double

def f(x):
    return x**2

x0, x1 = 0, 1
y0, y1 = 0, 1
n = 500

ans = MonteCarlo_double(f, x0, x1, y0, y1, n)
print(ans)
