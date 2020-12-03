# factoring.py>

import sympy;
import numpy;

__all__ = [ "is_pt_smooth", "get_factor_degree" ]

# test by trial division whether b is pt smooth
# if pt smooth, return the order of the factors
# in an array from high to low (?)
# t is the index of the prime
def is_pt_smooth(b,t):
    print("is_pt_smooth")
    pt=sympy.prime(t)
    print("{}'th prime: {}".format(t,pt))
    print("===")
    exponent,quotient=get_factor_degree(b,pt)
    if ( quotient == 1 ):
        return True
    elif t == 1:
        return False
    else:
        return is_pt_smooth(quotient,t-1)


# how many times is n1 divided evenly by n2?
def get_factor_degree(n1,n2):
    return get_factor_degree_recursive(n1,n2)
    
    
def get_factor_degree_recursive(n1,n2):
    quotient=n1/n2
    remainder=n1%n2
    print("{}/{}: {}".format(n1,n2,quotient))
    print("{}%{}: {}".format(n1,n2,remainder))
    print("===")
    if ( remainder != 0 ):
        return 0,n1;
    elif ( quotient == 1 ):
        return 1,1;
    else:
        return numpy.add( (1,0), get_factor_degree_recursive(quotient,n2) )
    
    
def get_factor_degree_iterative(n1,n2):
    if ( n2 == 0 ):
        return -1,n1
    if ( n2 > n1 ):
        return 0,n1
    exponent=0
    quotient=n1
    # "loop-and-a-half"
    while True:
        tempquotient=quotient/n2
        remainder=quotient%n2
        print("{}/{}: {}".format(quotient,n2,tempquotient))
        print("{}%{}: {}".format(quotient,n2,remainder))
        print("===")
        if ( remainder != 0 ):
            break
        else:
            exponent+=1
            quotient=tempquotient
            if ( quotient == 1 ):
                break
    print("{}={}^{}*{}".format(n1,n2,exponent,quotient))
    return exponent,quotient

