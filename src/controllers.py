from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from src.services import PolyServices
from src.schemas import ArithmeticPolySchema, SinglePolySchema
from src.utils import hex_bin_to_int, int_to_hex_bin


poly_endpoints = Blueprint('poly_endpoints', __name__)


@poly_endpoints.route('/poly_endpoints/poly', methods=['POST'])
def add_poly():
    """
    Add two polynomials in GF(2^m)
    ---
    tags:
        - poly
    consumes:
        - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - m
            - bits
            - type
            - bin1
            - bin2
            - hex1
            - hex2
          properties:
            m:
              type: integer
              required: true
              description: The degree of the polynomial
            bits:
              type: integer
              required: true
              description: The number of bits of the polynomial
            type:
              type: string
              required: true
              description: The type of the polynomial
            bin1:
              type: string
              required: false
              description: The first polynomial in binary
            bin2:
              type: string
              required: false
              description: The second polynomial in binary
            hex1:
              type: string
              required: false
              description: The first polynomial in hexadecimal
            hex2:
              type: string
              required: false
              description: The second polynomial in hexadecimal
    responses:
        200:
            description: Polynomial addition result
        500:
            description: Internal server error
    """
    data = request.json
    schema = ArithmeticPolySchema()
    try:
        schema.load(data)
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400
    
    m = data['m']
    bits = data['bits']
    type = data['type']
    service = PolyServices()
    try:
        if type == 'bin':
            poly1 = data['bin1']
            poly2 = data['bin2']
        else:
            poly1 = data['hex1']
            poly2 = data['hex2']
        result = service.add_in_gf(m, hex_bin_to_int(poly1, type), hex_bin_to_int(poly2, type))
        hex_result, bin_result = int_to_hex_bin(result['result'], bits)
        return jsonify({'result': {'hex': hex_result, 'bin': bin_result}}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@poly_endpoints.route('/poly_endpoints/subtract', methods=['POST'])
def subtract_poly():
    """
    Subtract two polynomials in GF(2^m)
    ---
    tags:
        - poly
    consumes:
        - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - m
            - bits
            - type
            - bin1
            - bin2
            - hex1
            - hex2
          properties:
            m:
              type: integer
              description: The degree of the polynomial (1 to 2^13)
            bits:
              type: integer
              description: The number of bits (16,32,64,128,256)
            type:
              type: string
              description: Input type ('bin' or 'hex')
            bin1:
              type: string
              description: First polynomial in binary
            bin2:
              type: string
              description: Second polynomial in binary
            hex1:
              type: string
              description: First polynomial in hexadecimal
            hex2:
              type: string
              description: Second polynomial in hexadecimal
    responses:
        200:
            description: Polynomial subtraction result
        400:
            description: Validation error
        500:
            description: Internal server error
    """
    data = request.json
    schema = ArithmeticPolySchema()
    try:
        schema.load(data)
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400
    
    m = data['m']
    bits = data['bits']
    type = data['type']
    service = PolyServices()
    
    try:
        if type == 'bin':
            poly1 = data['bin1']
            poly2 = data['bin2']
        else:
            poly1 = data['hex1']
            poly2 = data['hex2']
            
        result = service.subtract_in_gf(m, hex_bin_to_int(poly1, type), hex_bin_to_int(poly2, type))
        hex_result, bin_result = int_to_hex_bin(result['result'], bits)
        
        return jsonify({
            'result': {
                'hex': hex_result,
                'bin': bin_result
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@poly_endpoints.route('/poly_endpoints/multiply', methods=['POST'])
def multiply_poly():
    """
    Multiply two polynomials in GF(2^m)
    ---
    tags:
        - poly
    consumes:
        - application/json
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - m
            - bits
            - type
            - bin1
            - bin2
            - hex1
            - hex2
    """
    data = request.json
    schema = ArithmeticPolySchema()
    try:
        schema.load(data)
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400
    
    m = data['m']
    bits = data['bits']
    type = data['type']
    service = PolyServices()
    
    try:
        if type == 'bin':
            poly1 = data['bin1']
            poly2 = data['bin2']
        else:
            poly1 = data['hex1']
            poly2 = data['hex2']
            
        result = service.multiply_in_gf(m, hex_bin_to_int(poly1, type), hex_bin_to_int(poly2, type))
        hex_result, bin_result = int_to_hex_bin(result['result'], bits)
        
        return jsonify({
            'result': {
                'hex': hex_result,
                'bin': bin_result
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@poly_endpoints.route('/poly_endpoints/divide', methods=['POST'])
def divide_poly():
    data = request.json
    schema = ArithmeticPolySchema()
    try:
        schema.load(data)
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400
    
    m = data['m']
    bits = data['bits']
    type = data['type']
    service = PolyServices()
    
    try:
        if type == 'bin':
            dividend = data['bin1']
            divisor = data['bin2']
        else:
            dividend = data['hex1']
            divisor = data['hex2']
            
        # Convert inputs to integers
        dividend_int = hex_bin_to_int(dividend, type)
        divisor_int = hex_bin_to_int(divisor, type)
        
        
        # Perform division
        result = service.divide_in_gf(dividend_int, divisor_int, m)
        
        
        # Get quotient and remainder
        quotient = result[0]
        remainder = result[1]
        
        
        quotient_hex,quotient_bin=int_to_hex_bin(quotient,bits)
        remainder_hex,remainder_bin=int_to_hex_bin(remainder,bits)
        
        response = {
            'quotient_hex': quotient_hex,
            'remainder_hex': remainder_hex,
            'quotient_bin': quotient_bin,
            'remainder_bin': remainder_bin
        }
        
        print(f"DEBUG - Response structure: {response}")  # Debug print
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@poly_endpoints.route('/poly_endpoints/modulo', methods=['POST'])
def modulo_poly():
    """
    Modulo reduction in GF(2^m)
    """
    data = request.json
    schema = SinglePolySchema()
    try:
        schema.load(data)
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400
    
    m = data['m']
    bits = data['bits']
    type = data['type']
    service = PolyServices()
    
    try:
        if type == 'bin':
            poly = data['bin']
        else:
            poly = data['hex']
            
            
        result = service.gf2_modulo_reduction(m, hex_bin_to_int(poly, type))
        hex_result, bin_result = int_to_hex_bin(result['result'], bits)
        
        return jsonify({
            'result': {
                'hex': hex_result,
                'bin': bin_result
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@poly_endpoints.route('/poly_endpoints/invert', methods=['POST'])
def invert_poly():
    data = request.json
    print(request.json)

    schema = SinglePolySchema()
    try:
        schema.load(data)
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400
    
    m = data['m']
    bits = data['bits']
    type = data['type']
    service = PolyServices()
    
    try:
        if type == 'bin':
            poly = data['bin']
        else:
            poly = data['hex']
            
        # Convert input to integer
        print(poly)
        poly_int = hex_bin_to_int(poly, type)
        print(poly_int)
        # Find inverse
        result = service.invert_in_gf(poly_int, m)
        print ("done")
        if 'error' in result:
            return jsonify(result), 400
            
        # Convert result to hex/bin based on input type
        hex_result,bin_result=int_to_hex_bin(result,bits)
        response = {
            'result': {
                'hex': hex_result,
                'bin': bin_result
            }
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500