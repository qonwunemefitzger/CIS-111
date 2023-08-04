# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 17:54:37 2023

@author: 16614
OLS ordinary squares
"""
import numpy as np
import statsmodels.api as sm
import pandas as pd

# reading data from the_cv
data= pd.read_csv('ToyData.csv')
# defining the variables
x1 = data['x1'].tolist()
x2 = data['x2'].tolist()
y = data['y'].tolist()


X= np.array([[1,-4,6,3],[4,3,1,5]])
X = X.T
# adding the constant term
X = sm.add_constant(X)

#performing the regression 
# and fitting the model
result = sm.OLS(y,X).fit()

# printing the summarytable
print(result.summary())
