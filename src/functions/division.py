import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from utils import get_irreducible_polynomial
from inverse import invert_in_gf, divide_in_gf 
from funtions import multiplication 

def divide_in_gf(a: int, b: int, m: int) -> int:
    
    polynomial= get_irreducible_polynomial(m)
    inverse_b = invert_in_gf(b, m, polynomial)
    if 'error' in inverse_b:
        raise ValueError(inverse_b['error'])
    b_inv = inverse_b['result']
    result = multiplication.gf2m_multiply(a, b_inv, m, polynomial)
    return result

