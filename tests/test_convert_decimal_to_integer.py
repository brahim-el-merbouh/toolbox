from lib2to3.pytree import convert
from toolbox.utils import convert_decimal_to_integer

def test_convert_decimal_to_integer():
    value = convert_decimal_to_integer(23.45)
    assert isinstance(value, int)