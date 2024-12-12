from src.utils import get_irreducible_polynomial
from src.logger import logger

class PolyServices:
    def __init__(self):
        pass

    @staticmethod
    def xor_in_gf(m: int, poly1: int, poly2: int) -> int:
        xor = poly1 ^ poly2
        while xor.bit_length() > m:
            xor ^= get_irreducible_polynomial(m)
            m -= 1
        return xor

    def add_in_gf(self, m: int, poly1: int, poly2: int) -> int:
        logger.info("Enter add method")
        result = self.xor_in_gf(m, poly1, poly2)
        logger.info(f"Exit add method with result: {result}")
        return result

    def subtract_in_gf(self, m: int, poly1: int, poly2: int) -> int:
        logger.info("Enter subtract method")
        result = self.xor_in_gf(m, poly1, poly2)
        logger.info(f"Exit subtract method with result: {result}")
        return result

    @staticmethod
    def multiply_in_gf(m: int, poly1: int, poly2: int) -> int:
        logger.info("Enter multiply method")
        irreducible_poly = get_irreducible_polynomial(m)
        logger.info(f"Irreducible polynomial: {irreducible_poly}")
        
        result = 0
        for _ in range(m):
            if (poly2 & 1) != 0:
                result ^= poly1

            poly2 >>= 1

            carry = (poly1 & (1 << (m - 1))) != 0
            poly1 <<= 1
            if carry:
                poly1 ^= irreducible_poly

            poly1 &= (1 << m) - 1

        logger.info(f"Exit multiply method with result: {result}")
        return result
    
    def divide_in_gf(self, m: int, dividend: int, divisor: int) -> tuple[int, int]:
        logger.info("Enter divide method")
        if divisor == 0:
            logger.info("Division by zero")
            raise ZeroDivisionError(f"Division by zero in GF(2^{m})")

        irreducible_poly = get_irreducible_polynomial(m)
        logger.info(f"Irreducible polynomial: {irreducible_poly}")

        divisor_inv = self.invert_in_gf(m, divisor)
        result = self.multiply_in_gf(m, dividend, divisor_inv)

        logger.info(f"Exit divide method with result: {result}")
        return result

    @staticmethod
    def modulo_in_gf(m: int, poly: int) -> int:
        logger.info("Enter modulo method")
        irreducible_poly = get_irreducible_polynomial(m)
        logger.info(f"Irreducible polynomial: {irreducible_poly}")

        while poly.bit_length() > m + 1:
            shift = poly.bit_length() - (m + 1)
            poly ^= irreducible_poly << shift

        logger.info(f"Exit modulo method with result: {poly}")
        return poly


    def invert_in_gf(self, m: int, poly: int) -> int:
        logger.info("Enter invert method")
        if poly == 0:
            logger.info(f"Zero has no inverse in GF(2^{m})")
            raise ValueError(f"Zero has no inverse in GF(2^{m})")

        irreducible_poly = get_irreducible_polynomial(m)
        logger.info(f"Irreducible polynomial: {irreducible_poly}")

        u = poly
        v = irreducible_poly
        g1 = 1
        g2 = 0

        while u != 1 and v != 0:
            if u.bit_length() < v.bit_length():
                u, v = v, u
                g1, g2 = g2, g1

            shift = u.bit_length() - v.bit_length()
            u ^= v << shift
            g1 ^= g2 << shift

        if u == 1:
            result = self.modulo_in_gf(m, g1)
            logger.info(f"Exit invert method with result: {result}")
            return result
        raise ValueError(f"No inverse exists for {poly} in GF(2^{m})")
