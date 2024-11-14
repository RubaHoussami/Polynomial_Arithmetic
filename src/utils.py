from typing import Literal
from src.constants import irreducible_polynomials_map

def get_irreducible_polynomial(m: int) -> int:
    poly = irreducible_polynomials_map.get(m)
    if poly is None:
        poly = (1 << (m - 1)) | 1
    return poly

def hex_to_int(hex_string: str) -> int:
    return int(hex_string, 16)

def bin_to_int(binary_string: str) -> int:
    return int(binary_string, 2)

def int_to_hex(number: int) -> str:
    return hex(number)

def int_to_bin(number: int) -> str:
    return bin(number)

def hex_bin_to_int(number: int, type: Literal['hex', 'bin']) -> int:
    if type == 'hex':
        return hex_to_int(number)
    return bin_to_int(number)

def int_to_hex_bin(number: int, bits: int) -> tuple[str, str]:
    return int_to_hex(number), int_to_bin(number)
