# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 15:32:43 2023

linear regression
y = b0 + b1*x
given data pairs, y,x find values for b0 and b1 that best 

demonstrate use of pandas and probability density function

"""
def estimate_coef(x,y):
    """
    

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    y : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    import numpy as np 
    
    n = len(x)
    # get means of x and y
    m_x = np.mean(x)
    m_y = np.mean(y)
    
    SS_xy = np.sum(x*y) - n*m_x*m_y
    SS_xx = np.sum(x*x) - n*m_x*m_x
    
    b1 = SS_xy/SS_xx
    b0 = m_y - b1*m_x
    return (b0, b1)
 
    if __name__ =='__main__':
        import numpy as np 
        import matplotlib.pyplot as plt 
        
        y = np.array([4,-1,2])
        x = np.array([1,2,3])
        
        b0, b1 = estimate_coef(x,y)
        
        plt.plot(x,y,'.')
        
        xline = np.linspace(0,4)
        yline = b0 + b1*xline
        
        plt.plot(xline,yline,color='red')
        plt.xlabel('y')
        plt.ylabel('y')
        plt.title('regression')
        plt.grid()
        plt.show()