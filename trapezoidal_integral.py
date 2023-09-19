from math import sin, exp, pi, sqrt
def function1(x):
    return 4/(1+x**2)

def function2(x):
    return (sqrt(pi))*exp(-x**2)

def integral(f,a=0,b=1,n=100):
    h = (b-a)/n
    s = 0
    for i in range(1,n):
        s +=  (h/2)*(f(a+(i-1)*h) + f(a+i*h))
    return s
    
    
print(integral(sin,b=pi/2,n=50))
print(integral(function1))
print(integral(function2,a=-100, b=100,n=1000))

