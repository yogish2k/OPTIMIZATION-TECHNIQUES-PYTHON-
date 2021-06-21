
import math as m
#function input and parameters
#step 1
def func(x,y):
    f = m.exp(((x-0.2)**2/2)+4*(y**2)+m.sin(y))
    #print (x , y , f)
    return(f)
X= float(input('Enter the x-coordinate of starting point:'))
Y= float(input('Enter the y-coordinate of starting point:'))
dx = float(input('Enter the increment parameter for X:'))
dy = float(input('Enter the increment parameter for Y:'))
i = int(input('Enter the number of iterations'))
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
        return x, Y
    elif (func(x,y_add)<func(x,Y)and func(x,y_add)<func(x,y_sub)):
        return x, y_add
    elif(func(x,y_sub)<func(x,Y) and func(x,y_sub)<func(x,y_add)):
        return x, y_sub
    else:
        return x, Y


#Pattern move
def pat_move(x,y,x_new,y_new):
    x_new = (2*x_new)-x
    y_new = (2*y_new)-y
    return (x_new,y_new)

#Hooke-jeeves Pattern search
x_new,y_new = exp_move(X,Y,dx,dy)
x_prev,y_prev = x_new,y_new
X,Y = pat_move(X,Y,x_new,y_new)
x_new,y_new = exp_move(X,Y,dx,dy)
print(k)
while  k <= i:
    if func(x_new,y_new) == func(x_prev,y_prev):
        dx, dy = dx / 2, dy / 2
    print(k)
    k=k+1
    X,Y = pat_move(X,Y,x_new,y_new)
    x_prev,y_prev = x_new,y_new
    x_new,y_new = exp_move(X,Y,dx,dy)
    print(x_new, y_new)
print(('The minimum point is ({}, {})'.format(x_new, y_new)))
exit()
