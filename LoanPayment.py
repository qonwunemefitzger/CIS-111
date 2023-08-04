# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 18:01:41 2023

@author: 16614
"""

def computesPmt(PV, r, n):
        r = r/100
        r = r/12
        Pmt = r * PV/(1-(1+r)**n)
        return Pmt
    
    
def computesPV(PV, r, n):
        r = r/100
        r = r/12
        PV = (1-(1+r)**(-n)) * PV / r
        return PV
     
def computesN(Pmt, PV, r):
        r = r/12 # converts to a % per month
        r = r/100 # converts APR to a decimal
        # given Pmt, PV, r, we compute n 
        n = - np.log (1-PV*r/Pmt) / np.log(1+r)
        n = round(n,1)
        return n
    
def computesR(Pmt,PV, n):
        rLow = 0
        rHigh = 0.5
        diff = 2 
        while abs(diff) > 0.001:
            rTry = (rLow +rHigh)/2
            diff = Pmt - PV*rTry/(1-(1+rTry)**(-n))
            if diff > 0:
                rLow = rTry
            else:
                rHigh = rTry
        return rTry
            
if __name__ == "__main__":
    
    import numpy as np
 
        
    while(True):
          
        choice = int(input('Enter choice 1 for PV, 2 for Pmt, 3 for months in debt, 4 for APR:'))
        if (choice== 1 or choice == 2 or choice == 3 or choice == 4):
            break
        else:
            print(f"ente a 1, 2, 3, or a 4 you entered {choice}.")
            
    if choice == 2:
        PV = input('Enter interst APR: ')
        PV = float(PV)
        print(f"PV = {PV}/n")
        
        r = input ('Enter interest APR:')
        r = float(r)
        print(f"interst = {r: 0.3f} /n")
        
        n = int(input('Enter how many months: '))
        pmt = computesPmt(PV, r, n)
        pmt = np.round(pmt, 2)
        print(f"The payment is $ {pmt} per month")
    
    if choice == 3:
        Pmt = input ("enter Pmt")
        Pmt = float (Pmt)
        print (f"Pmt = {Pmt} /n")
        PV = input("enter PV:")
        PV = float(PV)
        print(f"PV ={PV} /n") 
        r = input("enter interest APR:")
        r = float(r)
        print(f"interest = {r: 0.3f} /n")
        MonthsMakingPayment = computesN(Pmt,PV,r)
        MonthsMakingPayment = np.round(MonthsMakingPayment, 2)   
        print(f"{MonthsMakingPayment}")
    
    
    
    
    
    
    if choice == 1:
        Pmt = input ('enter Pmt: ')
        Pmt = float (Pmt)
        print(f"Pmt ={Pmt} /n")
        r = input ('enter Pmt: ')
        r = float(r)
        print(f"interest = {r: 0.3f} /n")
        n = int(input('number of months:'))
        print(f"n = {n} per month")
        PV = computesPV(Pmt, r, n)
        PV = np.round(PV,2)
        print(f"The payment i can borrow is $ {PV: 0.2f} per month") 
        
    if choice == 4:
        
        while(True):
            Pmt = input("enter payment ")
            Pmt = float(Pmt)
            
            PV = input("enter amount borrowed")
            PV = float(PV)
            
            n = input("enter number of months")
            n = int(n)
            
            # check for solution
            if Pmt * n > PV:
                break
            else:
                print('no solution, Pmt * n must be > PV.')
                
            r = computesR(Pmt, PV, n)
            # convert to APR:
            r *= 1200
            print(f"interest = {r: 0.2f}%. APR:")
            

    