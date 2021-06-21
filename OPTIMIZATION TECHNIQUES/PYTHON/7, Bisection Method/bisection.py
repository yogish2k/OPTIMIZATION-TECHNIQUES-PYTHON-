import math as mp


def BS_with_interations(a,b,N):
    i=1
    while(i<=N):
        z=(a+b)/2
        if z < -0.01 or z > 0.01:
            zZ=0.01*abs(z)
        elif z < 0.01 and z > -0.01:
            zZ=0.0001
        f_dz=(f(z+zZ)-f(z-zZ))/(2*zZ)
        
        if(f_dz<0):
            a=z
            b=b
        elif (f_dz>0):
            b=z
            a=a
        print("Iteration:{}  z={}  f'(z)={}  interval=({},{})".format(i,z,f_dz,a,b))
        i=i+1


def BS_with_termination(a,b,E):
    i=1
    n=100
    while(i<=n):
        z=(a+b)/2
        if z < -0.01 or z > 0.01:
            zZ=0.01*abs(z)
        elif z < 0.01 and z > -0.01:
            zZ=0.0001
        f_dz=(f(z+zZ)-f(z-zZ))/(2*zZ)
        
        if (abs(f_dz)<E):
            print("Total iterations:{}\nFinal z:{},".format(i,z))
            print("minimum is at",z)
            break
        elif(f_dz<0):
            a=z
            b=b
        elif (f_dz>0):
            b=z
            a=a
        print("Iteration:{}  z={}  f'(z)={}  min in interval=({},{})".format(i,z,f_dz,a,b))
        i=i+1 
        
fun=input('Enter the function: ')
def f(x):
    return  eval(fun) #For function evaluations

print("Enter the lower bound:")
a=float(input())
print("Enter the upper bound:")
b=float(input())
if a < -0.01 or a > 0.01:
    aA=0.01*abs(a)
elif a < 0.01 and a > -0.01:
    aA=0.0001
if b < -0.01 or b > 0.01:
    bB=0.01*abs(b)
elif b < 0.01 and b > -0.01:
    bB=0.0001 
f_da=(f(a+aA)-f(a-aA))/(2*aA)
f_db=(f(b+bB)-f(b-bB))/(2*bB)
if (f_da <0 and f_db>0):
        print("Bisection method can be performed ")
        print("Please specify if you want to give E or the number of iterations.\
        Press N for No. of iterations, Else press E")
        c = input()
        if c == "N" or c == "n":
           print("Number of evaluations")
           N=float(input())
           BS_with_interations(a,b,N)
        else:
           print("Enter the tolerance error")
           E=float(input())
           BS_with_termination(a,b,E)    
else:
    print("Bisection method can't be performed")