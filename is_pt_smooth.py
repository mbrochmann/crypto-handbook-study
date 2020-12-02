# is_pt_smooth.py>

import sympy;

# test by trial division whether b is pt smooth
# if pt smooth, return the order of the factors
# in an array from high to low (?)
# t is the index of the prime
def is_pt_smooth(b,t):
    print("is_pt_smooth")
    pt=sympy.prime(t)
    print("{}'th prime: {}".format(t,pt))
    print("===")
    get_factor_degree(b,pt)


# how many times is n1 divided evenly by n2?
def get_factor_degree(n1,n2):
    exponent=0
    dividend=n1
    # "loop-and-a-half"
    while True:
        tempdividend=dividend/n2
        remainder=n1%n2
        print("{}/{}: {}".format(dividend,n2,tempdividend))
        print("{}%{}: {}".format(dividend,n2,remainder))
        print("===")
        if ( remainder != 0 ):
            break
        else:
            exponent+=1
            dividend=tempdividend
            if ( dividend == 1 ):
                break
    print("{}={}^{}*{}".format(n1,n2,exponent,dividend))


