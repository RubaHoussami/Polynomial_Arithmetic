# define irreducible polynomials for specific m values in GF(2^m)
irreducible_polynomials = {
    8: 0x11B,  # x^8 + x^4 + x^3 + x + 1
    163: 0x800000000000000000000000000000000000000C9,  # x^163 + x^7 + x^6 + x^3 + 1
    233: 0x2000000000000000000000000000000000000000000000013A,  # x^233 + x^74 + 1
    239: 0x80000000000000000000000000000000000000000000000105,  # x^239 + x^36 + 1
    283: 0x800000000000000000000000000000000000000000000000020A,  # x^283 + x^12 + x^7 + x^5 + 1
    409: 0x20000000000000000000000000000000000000000000000000000000000000029,  # x^409 + x^87 + 1
    571: 0x8000000000000000000000000000000000000000000000000000000000000000000000000000000253  # x^571 + x^10 + x^5 + x^2 + 1
}

def gf2m_multiply(poly1: int, poly2: int, m: int = 163) -> int:
    """
    Multiplies two polynomials in the Galois Field GF(2^m).
    
    This function performs polynomial multiplication over GF(2^m) and reduces
    the result modulo an irreducible polynomial for the specified field.
    
    Parameters:
    poly1 (int): The first polynomial, represented as an integer.
    poly2 (int): The second polynomial, represented as an integer.
    m (int): The degree of the Galois Field (default is 163).
    
    Returns:
    int: The result of the polynomial multiplication in GF(2^m).
    """
    
    # retrieve the irreducible polynomial for GF(2^m)
    irreducible_poly = irreducible_polynomials[m]
    result = 0  # initialize the result of multiplication to 0

    # perform polynomial multiplication using the standard binary multiplication algorithm
    while poly2:
        # if the least significant bit of poly2 is 1, XOR the result with poly1
        if poly2 & 1:
            result ^= poly1

        # left shift poly1 to move to the next bit in the multiplication process
        poly1 <<= 1

        # if the most significant bit of poly1 is 1, reduce by XORing with the irreducible polynomial
        if poly1 & (1 << m):
            poly1 ^= irreducible_poly

        # right shift poly2 to move to the next bit in the multiplication process
        poly2 >>= 1

    return result


