# -*- coding: utf-8 -*-
"""
Created on Thu Oct 8 11:31:13 2020

@author: yogi
"""
import timeit
import math as mp
fun=input('Enter the function: ')
def f(x):
    return eval(fun)  #For function evaluations

def para(a,b,e,N):
    con=False #variable con to check whether root exists
    startTime = timeit.default_timer()
    if a < -0.01 or a > 0.01:
        a_=0.01*abs(a)
    elif a < 0.01 and a > -0.01:
        a_=0.0001
    if b < -0.01 or b > 0.01:
        b_=0.01*abs(b)
    elif b < 0.01 and b > -0.01:
        b_=0.0001 
    f_da=(f(a+a_)-f(a-a_))/(2*a_)
    f_db=(f(b+b_)-f(b-b_))/(2*b_)
    if (f_da <0 and f_db>0):
        print("Secant method can be performed as the root exists in (a,b)")
    else:
        print("Secant method can't be performed")
        con=True
    try:
        denominator=(f_db-f_da)/(b-a)
        z= b - f_db/denominator
    except ZeroDivisionError:
        raise Exception("Error! - denominator zero for z") # Abort with error
    if z < -0.01 or z > 0.01:
        z_=0.01*abs(z)
    elif z < 0.01 and z > -0.01:
        z_=0.0001
    f_dz=(f(z+z_)-f(z-z_))/(2*z_)
    It=1
    print("{},{}".format(f_dz,z))
    while (It <=N):
        if con:       #breaks if no root exists
            break
        if (f_dz > 0):
            a=a
            b=z
        else:
            a=z
            b=b
        print("Iteration:{}  z={}  f'(z)={}  interval=({},{})".format(It,z,f_dz,a,b))
        if a < -0.01 or a > 0.01:
            a_=0.01*abs(a)
        elif a < 0.01 or a > -0.01:
            a_=0.0001
        if b < -0.01 and b > 0.01:
            b_=0.01*abs(b)
        elif b < 0.01 and b > -0.01:
            b_=0.0001    
        f_da=(f(a+a_)-f(a-a_))/(2*a_)
        f_db=(f(b+b_)-f(b-b_))/(2*b_)
        z= (b - ((b-a)*f_db)/(f_db - f_da))
        if z < -0.01 and z > 0.01:
            z_=0.01*abs(z)
        elif z < 0.01 and z > -0.01:
            z_=0.0001    
        f_dz=(f(z+z_)-f(z-z_))/(2*z_)
        It=It+1
        if abs(f_dz)<e:
            print("Total iterations:{}\nFinal z:{},".format(It,z))
            if f_dz>0:
                a=a
                b=z  
            elif f_dz<0:
                a=z
                b=b
            break
    executionTime = timeit.default_timer() - startTime        
    return a,b,executionTime,con

def main():
    print("Enter the lower bound:")
    a=float(input())
    print("Enter the upper bound:")
    b=float(input())
    print("Enter the tolerance error")
    e=float(input())
    print("Number of evaluations")
    N=float(input())
    x1,x2,t,c=para(a,b,e,N)
    if c==False:
        return ("The minimum lies in interval ({},{})\nExecution time={}".format(x1,x2,t))
    else:
        return("The process exited without performing secant method!")

print(main())     