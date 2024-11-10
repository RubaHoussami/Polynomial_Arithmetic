def gf2_modulo_reduction(poly, irreducible_poly):
    poly_degree = poly.bit_length() - 1
    irr_degree = irreducible_poly.bit_length() - 1

    # While the degree of the polynomial is greater than or equal to the irreducible polynomial
    while poly_degree >= irr_degree:
        # Calculate the difference in degree
        shift = poly_degree - irr_degree
        poly ^= (irreducible_poly << shift)
        # Update the polynomial degree
        poly_degree = poly.bit_length() - 1

    return poly

