#!/usr/bin/env python
from collections import namedtuple
from f import function

'''
Root Finding Methods
'''

def bisection_method(func, x_lower, x_upper, e_tolerance, max_iter, log_iter = False):
    f_lower = func(x_lower)
    x_old, xr, err = 0.0, 0.0, None
    for i in range(1,max_iter):
        xr = (x_lower + x_upper) / 2.0
        f_xr = func(xr)
        if xr != 0:
            err = abs((xr - x_old) / xr) * 100.0
        sign_test = f_lower * f_xr
        if sign_test < 0: x_upper = xr
        elif sign_test > 0:
            x_lower = xr
            f_lower = f_xr
        else: err = 0

        if log_iter: log_iteration('Bisection', i, xr, f_xr, err)
        x_old = xr
        if err and err < e_tolerance: return xr

    log_warning(f'Maximum number of iterations have reached : MAX_ITER = {max_iter}')
    return xr

def false_position_method(func, x_lower, x_upper, e_tolerance, max_iter, log_iter = False):
    f_lower, f_upper = func(x_lower), func(x_upper)
    x_old, xr, err = 0.0, 0.0, None 
    for i in range(1,max_iter):
        xr = x_upper - f_upper * (x_lower - x_upper) / (f_lower - f_upper)
        f_xr = func(xr)
        if xr != 0:
            err = abs((xr - x_old) / xr) * 100
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
        if err and err < e_tolerance: return xr
    
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
    if err:
        print(f'[{method}] {iter:3d} {xr:+3.8f} {f_xr:+2.8f} {err:3.8f}')
    else:
        print(f'[{method}] {iter:3d} {xr:+3.8f} {f_xr:+2.8f} ----')

def log_warning(msg):
    print(f'[Warning] {msg}.')

def log_error(code : int, msg = 'Unknown Error'):
    print(f'[Error] {msg}.')
    print(f'Exiting...\nExit Code {code}')
    exit() 

if __name__ == '__main__':
    param = read_input('sample_input.txt')
    bisection_method(function, param.x_lower, param.x_upper, param.e_tolerance, param.max_iter, True)
    false_position_method(function, param.x_lower, param.x_upper, param.e_tolerance, param.max_iter, True)
