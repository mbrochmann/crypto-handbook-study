"""
This is the "factoring" module.
The facoring module supplies various functions used in factoring algorithms.
"""

import sympy;
import numpy;
from sympy import *;

__all__ = [ "is_pt_smooth", "get_factor_degree" ]

def test_is_pt_smooth():
    assert is_pt_smooth(8,1) == True

def is_pt_smooth(b,t):
    """
    test by trial division whether b is pt smooth
    if pt smooth, return the order of the factors
    in an array from high to low (?)
    t is the index of the prime
    """
    print("is_pt_smooth")
    pt=sympy.prime(t)
    print("{}'th prime: {}".format(t,pt))
    print("===")
    exponent,quotient=get_factor_degree(b,pt)
    if ( ( quotient == 1 ) or ( quotient < pt ) ):
        return True
    elif t == 1:
        return False
    else:
        return is_pt_smooth(quotient,t-1)


def get_factor_degree(n1,n2):
    """
    How many times is n1 divided evenly by n2?
    If n1 does not divide n1 evenly, returns
    tuple (0,n1).
    
    If n2 divides n1 evenly once more more,
    returns tuple (exponent,quotient),
    where quotient is the product of the factors
    of n1 that are not n2.
    """
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


# Algorithm 3.34 in Handbook
def sqrt_mod_p(n,p):
    if not isprime(p):
        return False;
    n=n%p # in case n>=p
    print("Need Legendre symbol")
    

# Algorithm 2.149 in Handbook
#
# Returns value of Jacobi symbol (a/n)
#
# If n is prime p, Legendre symbol (a/p) is:
#    0 if p|a
#    1 if a is a quadratic residue of p
#   -1 if a is a quadratic non-residue or p
#
# The Jacobi symbol is the product of the Legendre symbol
# (a/p) for each prime factor p of n, to the power of the
# factor.
def jacobi(a,n):
    a=a%n
    if a == 0:
        return 0
    if a == 1:
        return 1

    #exponent is e
    #quotient is a1
    exponent,quotient=get_factor_degree(a,2);
    if exponent % 2 == 0:
        s=1
    else:
        n_mod_8 = n%8
        abs_n_mod_8 = abs(n_mod_8-4)
        if abs_n_mod_8 == 3:
            s == 1
        elif abs_n_mod_8 == 1:
            s=-1
        if abs(n_mod_8-5) == 2 and quotient % 4 == 3:
            s=-s
    if quotient == 1:
        return s;
    n=n%quotient;
    return(s*jacobi(n,quotient))    


# Eventually write my own implementation,
# for now use sympy function
def isprime(n):
    return sympy.isprime(n)




# I kind of hate doctest as it matches the entire stdout of the function
# rather than just the function return value!!!
if __name__ == "__main__":
    import doctest
    doctest.testmod()
