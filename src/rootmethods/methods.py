#!/usr/bin/env python
from collections import namedtuple
from math import copysign, sqrt

'''
Error Computation
'''

def compute_error(f, xr, x_old, rel_err):
    err = None
    if rel_err:
        if xr != 0:
            err = abs((xr - x_old) / xr) * 100.0
            if err > 100 and xr*x_old > 0:
                err = abs(f(xr))
                rel_err = False
    else:
            err = abs(f(xr))
    return err, rel_err

'''
Root Finding Methods
'''

def bisection_method(func, x_lower, x_upper, e_tolerance, max_iter, log_iter = False):
    f_lower = func(x_lower)
    x_old, xr, err, rel_err = 0.0, 0.0, None, True
    for i in range(1,max_iter):
        xr = (x_lower + x_upper) / 2.0
        f_xr = func(xr)
        err, rel_err = compute_error(func, xr, x_old, rel_err)
        sign_test = f_lower * f_xr
        if sign_test < 0: x_upper = xr
        elif sign_test > 0:
            x_lower = xr
            f_lower = f_xr
        else: err = 0

        if log_iter: log_iteration('Bisection', i, xr, f_xr, err)
        x_old = xr
        if err is not None and err < e_tolerance: return xr

    log_warning(f'Maximum number of iterations have reached : MAX_ITER = {max_iter}')
    return xr

def false_position_method(func, x_lower, x_upper, e_tolerance, max_iter, log_iter = False):
    f_lower, f_upper = func(x_lower), func(x_upper)
    x_old, xr, err, rel_err = 0.0, 0.0, None, True 
    for i in range(1,max_iter):
        xr = x_upper - f_upper * (x_lower - x_upper) / (f_lower - f_upper)
        f_xr = func(xr)
        err, rel_err = compute_error(func, xr, x_old, rel_err)
        sign_test = f_lower * f_xr

        if sign_test < 0:
            x_upper = xr
            f_upper = f_xr
        elif sign_test > 0:
            x_lower = xr
            f_lower = f_xr
        else: err = 0

        if log_iter: log_iteration('False Position', i, xr, f_xr, err)
        x_old = xr
        if err is not None and err < e_tolerance: return xr
    
    log_warning(f'Maximum number of iterations have reached : MAX_ITER = {max_iter}')
    return xr
    

def newton_method(func, func_p, x0, e_tolerance, max_iter, log_iter = False):
    x_old, err, rel_err = x0, None, True
    for i in range(1, max_iter):
        xr =  x_old - func(x_old) / func_p(x_old)
        f_xr = func(xr)
        err, rel_err = compute_error(func, xr, x_old, rel_err)
        
        if log_iter: log_iteration('Newton', i, xr, f_xr, err)
        x_old = xr
        if err is not None and err < e_tolerance: return xr
    
    log_warning(f'Maximum number of iterations have reached : MAX_ITER = {max_iter}')
    return xr

def secant_method(func, x0, x1, e_tolerance, max_iter, log_iter = False):
    x_old_0, x_old_1, err, rel_err = x0, x1, None, True
    for i in range(1,max_iter):
        xr = x_old_1 - func(x_old_1) * (x_old_0 - x_old_1) / (func(x_old_0) - func(x_old_1))
        f_xr = func(xr)
        err, rel_err = compute_error(func, xr, x_old_1, rel_err)
        
        if log_iter: log_iteration('Secant', i, xr, f_xr, err)
        x_old_0 = x_old_1
        x_old_1 = xr
        if err is not None and err < e_tolerance: return xr
    
    log_warning(f'Maximum number of iterations have reached : MAX_ITER = {max_iter}')
    return xr

def polynomial_method(func, x_lower, x_upper, e_tolerance, max_iter, log_iter = True):
    f_lower, f_upper = func(x_lower), func(x_upper)
    x_old, xr, xi, err, rel_err = 0.0, 0.0, 0, None, True
    for i in range(1,max_iter):
        xi = (x_lower + x_upper) / 2.0
        f_i = func(xi)
        a = (f_lower - f_i) / (x_lower - xi) / (x_lower - x_upper) +\
            (f_i - f_upper) / (x_upper - xi) / (x_lower - x_upper)
        b = (f_lower - f_i) * (xi - x_upper) / (x_lower - xi) / (x_lower - x_upper) -\
            (f_i - f_upper) * (x_lower - xi) / (x_upper - xi) / (x_lower - x_upper)
        c = f_i
        xr = xi - 2*c / (b + copysign(sqrt(b**2 - 4*a*c),b))
        f_xr = func(xr)
        err, rel_err = compute_error(func, xr, x_old, rel_err)
        sign_test = f_lower * f_xr
        if sign_test < 0: 
            x_upper = xr
            f_upper = f_xr
        elif sign_test > 0:
            x_lower = xr
            f_lower = f_xr
        else: err = 0

        if log_iter: log_iteration('Polynomial', i, xr, f_xr, err)
        x_old = xr
        if err is not None and err < e_tolerance: return xr

    log_warning(f'Maximum number of iterations have reached : MAX_ITER = {max_iter}')
    return xr

'''
Input and Error Handling
'''
Parameters = namedtuple('Parameters',
                        ['x_lower',
                         'x_upper',
                         'e_tolerance',
                         'max_iter'
                        ])

def read_input(file_name = 'input.txt'):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if len(lines) < 4:
                log_error(1, 'Invalid input format')
            for i in range(4):
                try: float(lines[i])
                except:
                    log_error(1, f'Invalid formatting for parameter {Parameters._fields[i]}')

            return Parameters(
                x_lower = float(lines[0]),
                x_upper = float(lines[1]),
                e_tolerance = float(lines[2]),
                max_iter = int(lines[3])
            )
    
    except IOError:
        log_error(1, f'No such file or directory : \'{file_name}\'')

'''
Logging functions
'''

def log_iteration(method,iter, xr, f_xr, err):
    if err is not None:
        print(f'[{method}] {iter:3d} {xr:+3.8f} {f_xr:+2.8f} {err:3.8f}')
    else:
        print(f'[{method}] {iter:3d} {xr:+3.8f} {f_xr:+2.8f} ----')

def log_warning(msg):
    print(f'[Warning] {msg}.')

def log_error(code : int, msg = 'Unknown Error'):
    print(f'[Error] {msg}.')
    print(f'Exiting...\nExit Code {code}')
    exit() 

