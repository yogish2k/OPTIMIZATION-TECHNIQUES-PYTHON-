
import math as m
#function input and parameters
#step 1
def func(x,y):
    f = ((x-1)**2)+((y-2)**2)
    #print (x , y , f)
    return(f)
X= float(input('Enter the x-coordinate of starting point:'))
Y= float(input('Enter the y-coordinate of starting point:'))
dx = float(input('Enter the increment parameter for X:'))
dy = float(input('Enter the increment parameter for Y:'))
a = float(input('The reduction Parameter(>1):'))
if (a<=1):
    print('|The reduction Parameter must be greater than one|')
    exit()
e = float(input('The termination Parameter:'))
k = 0
#exploratory move
def exp_move(X,Y,dx,dy):
    x_add = X+dx
    x_sub = X-dx
    y_add = Y+dy
    y_sub = Y-dy
    if(func(X,Y)<func(x_add,Y) and func(X,Y)<func(x_sub,Y)):
        x = X
    elif(func(x_add,Y)<func(X,Y)and func(x_add,Y)<func(x_sub,Y)):
        x = x_add
    elif(func(x_sub,Y)<func(x_add,Y) and func(x_sub,Y)<func(X,Y)):
        x = x_sub
    if(func(x,Y)<func(x,y_add) and func(x,Y)<func(x,y_sub)):
        return x, Y, 1
    elif (func(x,y_add)<func(x,Y)and func(x,y_add)<func(x,y_sub)):
        return x, y_add, 1
    elif(func(x,y_sub)<func(x,Y) and func(x,y_sub)<func(x,y_add)):
        return x, y_sub, 1
    else:
        return x, Y, 0


#Pattern move
def pat_move(x,y,x_new,y_new):
    x_new = (2*x_new)-x
    y_new = (2*y_new)-y
    return (x_new,y_new)

#Hooke-jeeves Pattern search
# step 2
x_new,y_new,status = exp_move(X,Y,dx,dy)
#print(x_new, y_new)
# step 3
while status==0 and m.sqrt((dx** 2) + (dy** 2)) >= e :
    dx, dy = dx / a, dy / a
    x_new, y_new, status = exp_move(X, Y,dx,dy)
if (m.sqrt(dx** 2 + dy** 2) < e):
    print(('The minimum point is ({}, {})'.format(X,Y)))
    exit()
#step 4
x_prev,y_prev = x_new,y_new
k=k+1
X,Y = pat_move(X,Y,x_new,y_new)
x_new,y_new,status = exp_move(X,Y,dx,dy)
while func(x_new,y_new)< func(x_prev,y_prev):
    k=k+1
    X,Y = pat_move(X,Y,x_new,y_new)
    x_prev,y_prev = x_new,y_new
    x_new,y_new,status = exp_move(X,Y,dx,dy)
if (func(x_new,y_new )>= func(x_prev,y_prev)):
    while  m.sqrt(dx ** 2 + dy ** 2) >= e:
        dx, dy = dx / a, dy / a
        x_new, y_new, status = exp_move(X, Y, dx, dy)
    if (m.sqrt(dx ** 2 + dy ** 2) < e):
        print(('The minimum point is ({}, {})'.format(X, Y)))
        exit()
