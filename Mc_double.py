import numpy as np

def MonteCarlo_double(f, x0, x1, y0, y1, n):
    """
    Parameters:
    f : function
        The function to be integrated
    x0 : float
        The starting x-coordinate of the integration domain
    x1 : float
        The ending x-coordinate of the integration domain
    y0 : float
        The lower y-coordinate of the rectangle
    y1 : float
        The upper y-coordinate of the rectangle
    n : int
        Number of random points

    Returns:
    float
        Integral of f over the specified domain
    """

    x = np.random.random(n) * (x1 - x0) + x0
    y = np.random.random(n) * (y1 - y0) + y0

    areaCount = 0
    for i in range(len(x)):
        xVal = x[i]
        for j in range(len(y)):
            yVal = y[j]
            if f(xVal) < yVal:
                areaCount += 1

    area = areaCount / (n**2) * (x1 - x0) * (y1 - y0)
    return area

if __name__ == "__main__":
    def f(x):
        return x**2

    x0 = 0
    x1 = 1
    y0 = 0
    y1 = 1
    n = 500

    ans = MonteCarlo_double(f, x0, x1, y0, y1, n)
    print(ans)


