"""
This is the "test_factoring" module.
The test_factoring module tests the functionality of the factoring module.
"""

import factoring;
import sympy;

#def test_is_pt_smooth():
#    assert factoring.is_pt_smooth(8,1) == True


from hypothesis import given
import hypothesis.strategies as st

# Would parameter space exploration differ meaningfully if
# we passed a list of factor exponents of b instead of b
# as an integer?
#
# Notes for later - maybe should go at the is_pt_smooth_function:
# Recursive function is terrible here because of the recursion depth!!!
# Let's redo it as iterative function.
@given( b=st.integers(min_value=1), t=st.integers(min_value=1), delta_t=st.integers(min_value=1) )
def test_is_pt_smooth( b, t, delta_t ):
    print( "Testing with b={}, t={}, delta_t={}".format( b, t, delta_t ) )
    if factoring.is_pt_smooth( b, t ):
        assert ( b % sympy.prime( t + delta_t ) ) != 0
    else:
        assert sympy.prime( t ) < b
