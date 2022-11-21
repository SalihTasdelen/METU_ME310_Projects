from math import sin
from math import cos
from math import log as ln
from math import e

def f1(x): return x**2-(1-x)**5

def f2(x): return x*e**x-1

def f3(x): return cos(x)-x**3

def f4(x): return ln(x)

def f5(x): return x**3

def f6(x): return e**(x**2+7*x-30)-1

def f7(x): return x**-1-sin(x)+1

def fp1(x): return x*2+5*(1-x)**4

def fp2(x): return e**x+x*e**x

def fp3(x): return -sin(x)-3*x**2

def fp4(x): return 1/x

def fp5(x): return 3*x**2

def fp6(x): return e**(x**2+7*x-30)*(2*x+7)

def fp7(x): return -x**-2-cos(x)
