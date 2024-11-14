from src.utils import get_irreducible_polynomial

class PolyServices:
    def __init__(self):
        pass

    @staticmethod
    def xor_in_gf(m: int, poly1: int, poly2: int) -> int:
        return (poly1 ^ poly2) & ((1 << m) - 1)

    def add_in_gf(self, m: int, poly1: int, poly2: int) -> dict:
        return {'result': self.xor_in_gf(m, poly1, poly2)}

    def subtract_in_gf(self, m: int, poly1: int, poly2: int) -> dict:
        return {'result': self.xor_in_gf(m, poly1, poly2)}

    @staticmethod
    def multiply_in_gf(m: int, poly1: int, poly2: int) -> dict:
        irreducible_poly = get_irreducible_polynomial(m)
        result = 0

        while poly2:
            if poly2 & 1:
                result ^= poly1

            poly1 <<= 1

            if poly1 & (1 << m):
                poly1 ^= irreducible_poly

            poly2 >>= 1

        return {'result': result}
    
    @staticmethod
    def divide_in_gf(divident: int, divisor: int, m: int) -> dict:
        quotient = 0
        remainder = divident

        divisor_degree = divisor.bit_length() - 1

        while remainder.bit_length() - 1 >= divisor_degree:
            degree_diff = remainder.bit_length() - 1 - divisor_degree
            quotient ^= (1 << degree_diff)
            remainder ^= (divisor << degree_diff)

        return {'result': {'quotient': quotient, 'remainder': remainder}}

    def invert_in_gf(self, number: int, m: int, polynomial: int = None) -> dict:
        if number == 0:
            return {'error': 'Zero has no inverse in GF(2^m)'}

        if not polynomial:
            polynomial = get_irreducible_polynomial(m)

        a2, a3 = 0, polynomial
        b2, b3 = 1, number

        while a3 > 1:
            quotient, remainder = self.divide_in_gf(a3, b3, m)
            temp = self.subtract_in_gf(a2, self.multiply_in_gf(quotient, b2, m, polynomial), m)
            a2, a3, b2, b3 = b2, b3, temp, remainder

        if b3 != 1:
            return {'error': 'No inverse exists for number in GF(2^m)'}

        return {'result': b2}

    @staticmethod
    def gf2_modulo_reduction(m: int, poly: int, irreducible_poly: int = None) -> dict:
        if not irreducible_poly:
            irreducible_poly = get_irreducible_polynomial(m)

        poly_degree = poly.bit_length() - 1
        irr_degree = irreducible_poly.bit_length() - 1

        while poly_degree >= irr_degree:
            shift = poly_degree - irr_degree
            poly ^= (irreducible_poly << shift)
            poly_degree = poly.bit_length() - 1

        return {'result': poly}