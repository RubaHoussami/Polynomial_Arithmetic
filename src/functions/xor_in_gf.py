def xor_in_gf(a, b):
  # turns out add and sub are the same
  # XOR 
    c = a ^ b
    return int_to_hex(c), int_to_binary(c)
