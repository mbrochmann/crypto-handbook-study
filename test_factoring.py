"""
This is the "test_factoring" module.
The test_factoring module tests the functionality of the factoring module.
"""

import factoring;

def test_is_pt_smooth():
    assert factoring.is_pt_smooth(8,1) == True
