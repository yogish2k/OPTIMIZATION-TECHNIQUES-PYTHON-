#quardiatic search
from math import*
def f(x):
    return eval(function)
function=input(" Enter the function ")
delta=float(input("Enter the delta value "))
x1=float(input("Enter the initial point "))
xf=[]
flag=0
x2=x1+delta
f1=f(x1)
f2=f(x2)
if f1>=f2:
    x3=x1+(2*delta)
else:
    x3=x1-delta
f3=f(x3)
xf.append([x1,f(x1)])
xf.append([x2,f(x2)])
xf.append([x3,f(x3)])
choice = input("Do you want to enter the no. of iterations : y/n ")
if choice=='y' or choice == 'Y':
    n=int(input("Enter the no. of iterations "))
    while n!=0:
        n=n-1
        fmin=min(xf[0][1],xf[1][1],xf[2][1])
        if(fmin==xf[0][1]):
            xmin=xf[0][0]
        elif fmin==xf[1][1]:
            xmin=xf[1][0]
        else:
            xmin=xf[2][0]
        a1=(xf[1][1]-xf[0][1])/(xf[1][0]-xf[0][0])
        a2=(1/(xf[2][0]-xf[1][0]))*(((xf[2][1]-xf[0][1])/(xf[2][0]-xf[0][0]))-a1)
        x_=((xf[0][0]+xf[1][0])/2)-(a1/(2*a2))
        xf.append([x_,f(x_)])
        if n==0:
            xf.sort(key=lambda k:k[1])
            print(f"Minimum point : {xf[0][0]}, Minimum value : {xf[0][1]}")
        else:
            xf.sort(key=lambda k:k[1])
            xf.pop(3)
            xf.sort() 
else:
    e=float(input("Enter the termination parameter"))
    while flag==0:
        fmin=min(xf[0][1],xf[1][1],xf[2][1])
        if(fmin==xf[0][1]):
            xmin=xf[0][0]
        elif fmin==xf[1][1]:
            xmin=xf[1][0]
        else:
            xmin=xf[2][0]
        a1=(xf[1][1]-xf[0][1])/(xf[1][0]-xf[0][0])
        a2=(1/(xf[2][0]-xf[1][0]))*(((xf[2][1]-xf[0][1])/(xf[2][0]-xf[0][0]))-a1)
        x_=((xf[0][0]+xf[1][0])/2)-(a1/(2*a2))
        xf.append([x_,f(x_)])
        if abs(fmin-xf[3][1])<e and abs(xmin-xf[3][0])<e:
            flag=1
            xf.sort(key=lambda k:k[1])
            print(f"Minimum point : {xf[0][0]}, Minimum value : {xf[0][1]}")
        else:
            xf.sort(key=lambda k:k[1])
            xf.pop(3)
            xf.sort()