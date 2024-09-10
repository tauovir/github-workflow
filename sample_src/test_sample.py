import pytest
import os
import json
from sample import CommonCase



def test_factorial():
    """
    Test sample function
    """
    obj = CommonCase()
    fact = obj.get_factorial(num=5)
    assert fact == 120,f"Factorial Test failed output:{fact}, expected:120"
