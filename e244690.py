#!/usr/bin/env python
from collections import namedtuple

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
                log_error('Invalid input format.')
                exit_with_code(1)
            for i in range(4):
                try: float(lines[i])
                except:
                    log_error(f'Invalid formatting for parameter {Parameters._fields[i]}.')
                    exit_with_code(1)

            return Parameters(
                x_lower = float(lines[0]),
                x_upper = float(lines[1]),
                e_tolerance = float(lines[2]),
                max_iter = int(lines[3])
            )
    
    except IOError:
        log_error(f'No such file or directory : \'{file_name}\'')
        exit_with_code(1)

def log_error(msg = 'Unknown Error.'):
    print(f'[Error] {msg}')

def exit_with_code(code = 0):
    print(f'Exiting...\nExit Code {code}')
    exit()

if __name__ == '__main__':
    param = read_input('sample_input.txt')
    print(param[0])

