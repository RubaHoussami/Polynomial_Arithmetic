from utils import get_irreducible_polynomial

def divide_in_gf(divident: int, divisor: int, m: int) -> tuple[int, int]:
    quotient = 0
    remainder = divident

    divisor_degree = divisor.bit_length() - 1

    while remainder.bit_length() - 1 >= divisor_degree:
        degree_diff = remainder.bit_length() - 1 - divisor_degree
        quotient ^= (1 << degree_diff)
        remainder ^= (divisor << degree_diff)

    return quotient, remainder

def invert_in_gf(number: int, m: int, polynomial: int = None) -> dict:
    if number == 0:
        return {'error': 'Zero has no inverse in GF(2^m)'}

    if not polynomial:
        polynomial = get_irreducible_polynomial(m)

    a2, a3 = 0, polynomial
    b2, b3 = 1, number

    while a3 > 1:
        quotient, remainder = divide_in_gf(a3, b3, m)
        temp = subtract_in_gf(a2, multiply_in_gf(quotient, b2, m, polynomial), m)
        a2, a3, b2, b3 = b2, b3, temp, remainder

    if b3 != 1:
        return {'error': 'No inverse exists for number in GF(2^m)'}

    return {'result': b2}
