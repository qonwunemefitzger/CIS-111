import numpy as np
def MCintegrate(f, a, b, n):
    """
    
    Parameters
    ----------
    f : TYPE function
        f returns a float between a and b
    a : TYPE float 
        DESCRIPTION. lower limit
    b : TYPE float
        DESCRIPTION. upper limit
    n : TYPE int
        DESCRIPTION, number of random points to take in the box

    Returns
    -------
    integral of f from a to b

    """

    from random import random
    # random returns a random number betwee 0 and 1
    
    n = 50
    x = np.linspace(a,b, num=n, endpoint=True)
    maxF = max(f(x))
    
    area = 0
    for i in range(n):
        
        #generate a random point in the boxc
        #x between a and b
        #z between 0 and maxF
        randNoX = random()*(b-a)+(b-a)/2
        randNoY = random()*maxF
        if randNoY <= f(randNoX): area += 1
    
    boxArea = (b-a)*maxF
    integral = area/n * boxArea
    return(integral)
    
if __name__ == "__main__":
    
    import numpy as np    
    import matplotlib.pyplot as plt
    
    def f(x) :
        return x**2
    
    area = MCintegrate(f, 1.,3., 50)
    
    print(area)