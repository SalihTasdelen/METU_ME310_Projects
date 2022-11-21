import rootmethods.methods as rm
import rootmethods.examples as ex

if __name__ == '__main__':
    TOLERANCE = 0.00001
    MAX_ITER = 30
    '''
    #Function 1
    rm.bisection_method(ex.f1, 0.1, 1, TOLERANCE, MAX_ITER, True)
    rm.false_position_method(ex.f1, 0.1, 1, TOLERANCE, MAX_ITER, True)
    rm.secant_method(ex.f1, 0.1, 1, TOLERANCE, MAX_ITER, True)
    rm.newton_method(ex.f1, ex.fp1, (0.1+1)/2, TOLERANCE, MAX_ITER, True)
    rm.polynomial_method(ex.f1, 0.1, 1, TOLERANCE, MAX_ITER, True)

    #Function 2
    rm.bisection_method(ex.f2, -1, 1, TOLERANCE, MAX_ITER, True)
    rm.false_position_method(ex.f2, -1, 1, TOLERANCE, MAX_ITER, True)
    rm.secant_method(ex.f2, -1, 1, TOLERANCE, MAX_ITER, True)
    rm.newton_method(ex.f2, ex.fp2, (-1+1)/2, TOLERANCE, MAX_ITER, True)
    rm.polynomial_method(ex.f2, -1, 1, TOLERANCE, MAX_ITER, True)

    #Function 3
    rm.bisection_method(ex.f3, 0.1, 1, TOLERANCE, MAX_ITER, True)
    rm.false_position_method(ex.f3, 0.1, 1, TOLERANCE, MAX_ITER, True)
    rm.secant_method(ex.f3, 0.1, 1, TOLERANCE, MAX_ITER, True)
    rm.newton_method(ex.f3, ex.fp3, (0.1+1)/2, TOLERANCE, MAX_ITER, True)
    rm.polynomial_method(ex.f3, 0.1, 1, TOLERANCE, MAX_ITER, True)
   
    #Function 4
    rm.bisection_method(ex.f4, 0.5, 5, TOLERANCE, MAX_ITER, True)
    rm.false_position_method(ex.f4, 0.5, 5, TOLERANCE, MAX_ITER, True)
    rm.secant_method(ex.f4, 0.5, 5, TOLERANCE, MAX_ITER, True)
    rm.newton_method(ex.f4, ex.fp4, (0.5+5)/2, TOLERANCE, MAX_ITER, True)
    rm.polynomial_method(ex.f4, 0.5, 5, TOLERANCE, MAX_ITER, True)

    '''
    #Function 5
    rm.bisection_method(ex.f5, -0.5, 1/3, TOLERANCE, MAX_ITER, True)
    rm.false_position_method(ex.f5, -0.5, 1/3, TOLERANCE, MAX_ITER, True)
    rm.secant_method(ex.f5, -0.5, 1/3, TOLERANCE, MAX_ITER, True)
    rm.newton_method(ex.f5, ex.fp5, (-0.5+1/3)/2, TOLERANCE, MAX_ITER, True)
    rm.polynomial_method(ex.f5, -0.5, 1/3, TOLERANCE, MAX_ITER, True)
'''
    #Function 6
    rm.bisection_method(ex.f6, 2.8, 3.1, TOLERANCE, MAX_ITER, True)
    rm.false_position_method(ex.f6, 2.8, 3.1, TOLERANCE, MAX_ITER, True)
    rm.secant_method(ex.f6, 2.8, 3.1, TOLERANCE, MAX_ITER, True)
    rm.newton_method(ex.f6, ex.fp6, (2.8+3.1)/2, TOLERANCE, MAX_ITER, True)
    rm.polynomial_method(ex.f6, 2.8, 3.1, TOLERANCE, MAX_ITER, True)

    #Function 7
    rm.bisection_method(ex.f7, -1.3, -0.5, TOLERANCE, MAX_ITER, True)
    rm.false_position_method(ex.f7, -1.3, -0.5, TOLERANCE, MAX_ITER, True)
    rm.secant_method(ex.f7, -1.3, -0.5, TOLERANCE, MAX_ITER, True)
    rm.newton_method(ex.f7, ex.fp7, (-1.3-0.5)/2, TOLERANCE, MAX_ITER, True)
    rm.polynomial_method(ex.f7, -1.3, -0.5, TOLERANCE, MAX_ITER, True)
'''
