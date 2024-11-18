from src.utils import get_irreducible_polynomial
from src.logger import logger

class PolyServices:
    def __init__(self):
        pass

    @staticmethod
    def xor_in_gf(m: int, poly1: int, poly2: int) -> int:
        return (poly1 ^ poly2) & ((1 << m) - 1)

    def add_in_gf(self, m: int, poly1: int, poly2: int) -> int:
        logger.info("Enter add_in_gf method")
        result = self.xor_in_gf(m, poly1, poly2)
        logger.info(f"Exit add_in_gf method with result: {result}")
        return result

    def subtract_in_gf(self, m: int, poly1: int, poly2: int) -> int:
        logger.info("Enter subtract_in_gf method")
        result = self.xor_in_gf(m, poly1, poly2)
        logger.info(f"Exit subtract_in_gf method with result: {result}")
        return result

    @staticmethod
    def multiply_in_gf(poly1: int, poly2: int, m: int) -> int:
        logger.info("Enter multiply_in_gf method")
        irreducible_poly = get_irreducible_polynomial(m)
        logger.info(f"Irreducible polynomial: {irreducible_poly}")
        result = 0
        
        while poly2:
            if poly2 & 1:
                result ^= poly1

            poly1 <<= 1

            if poly1 & (1 << m):
                poly1 ^= irreducible_poly

            poly2 >>= 1

        logger.info(f"Exit multiply_in_gf method with result: {result}")
        return result
    
    @staticmethod
    def divide_in_gf(divident: int, divisor: int, m: int) -> tuple[int, int]:
        logger.info("Enter divide_in_gf method")
        quotient = 0
        remainder = divident

        divisor_degree = divisor.bit_length() - 1

        while remainder.bit_length() - 1 >= divisor_degree:
            degree_diff = remainder.bit_length() - 1 - divisor_degree
            quotient ^= (1 << degree_diff)
            remainder ^= (divisor << degree_diff)

        logger.info(f"Exit divide_in_gf method with quotient: {quotient} and remainder: {remainder}")
        return quotient, remainder

    @staticmethod
    def modulo_in_gf(poly: int, m: int) -> int:
        logger.info("Enter modulo_in_gf method")
        irreducible_poly = get_irreducible_polynomial(m)
        logger.info(f"Irreducible polynomial: {irreducible_poly}")

        poly_degree = poly.bit_length() - 1
        irreducible_degree = irreducible_poly.bit_length() - 1

        while poly_degree >= irreducible_degree:
            shift = poly_degree - irreducible_degree
            poly ^= (irreducible_poly << shift)
            poly_degree = poly.bit_length() - 1

        logger.info(f"Exit modulo_in_gf method with result: {poly}")
        return poly

    def invert_in_gf(self, poly: int, m: int) -> int:
        logger.info("Enter invert_in_gf method")
        if poly == 0:
            raise ValueError(f'Zero has no inverse in GF(2^{m})')

        irreducible_poly = get_irreducible_polynomial(m)
        logger.info(f"Irreducible polynomial: {irreducible_poly}")

        a2, a3 = 0, irreducible_poly
        b2, b3 = 1, poly

        while a3 > 1:
            quotient, remainder = self.divide_in_gf(a3, b3, m)

            multiply = self.multiply_in_gf(quotient, b2, m)
            temp = self.subtract_in_gf(a2, multiply, m)

            a2, a3, b2, b3 = b2, b3, temp, remainder

        logger.info(f"b3 value: {b3}")
        if b3 != 1:
            raise ValueError(f'No inverse exists for {poly} in GF(2^{m})')

        logger.info(f"Exit invert_in_gf method with result: {b2}")
        return b2