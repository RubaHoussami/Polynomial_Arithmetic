from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from src.services import PolyServices
from src.schemas import SinglePolySchema, DoublePolySchema
from src.utils import hex_bin_to_int, int_to_hex_bin
from src.logger import logger


poly_endpoints = Blueprint('poly_endpoints', __name__)


@poly_endpoints.route('/add', methods=['POST'])
def add():
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
        400:
            description: Validation error
        500:
            description: Internal server error
    """
    logger.info("Enter add endpoint")
    data = request.json
    schema = DoublePolySchema()

    try:
        schema.load(data)
    except ValidationError as e:
        logger.info(f"Validation error in add endpoint: {e.messages}")
        return jsonify({'error': e.messages}), 400
    
    m = data['m']
    bits = data['bits']
    type = data['type']

    service = PolyServices()

    try:
        poly1 = data[type + '1']
        poly2 = data[type + '2']

        poly1 = hex_bin_to_int(poly1, type)
        poly2 = hex_bin_to_int(poly2, type)

        result = service.add_in_gf(m, poly1, poly2)
        hex_result, bin_result = int_to_hex_bin(result, bits)

        logger.info("Exit add endpoint")
        return jsonify({
            'result': {
                'hex': hex_result,
                'bin': bin_result
            }
        }), 200
    except Exception as e:
        logger.error(f"An unexpected error occurred in add endpoint: {str(e)}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


@poly_endpoints.route('/subtract', methods=['POST'])
def subtract():
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
    logger.info("Enter subtract endpoint")
    data = request.json
    schema = DoublePolySchema()

    try:
        schema.load(data)
    except ValidationError as e:
        logger.info(f"Validation error in subtract endpoint: {e.messages}")
        return jsonify({'error': e.messages}), 400

    m = data['m']
    bits = data['bits']
    type = data['type']

    service = PolyServices()
    
    try:
        poly1 = data[type + '1']
        poly2 = data[type + '2']

        poly1 = hex_bin_to_int(poly1, type)
        poly2 = hex_bin_to_int(poly2, type)

        result = service.subtract_in_gf(m, poly1, poly2)
        hex_result, bin_result = int_to_hex_bin(result, bits)

        logger.info("Exit subtract endpoint")
        return jsonify({
            'result': {
                'hex': hex_result,
                'bin': bin_result
            }
        }), 200
    except Exception as e:
        logger.error(f"An unexpected error occurred in subtract endpoint: {str(e)}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500
    
@poly_endpoints.route('/multiply', methods=['POST'])
def multiply():
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
            description: Polynomial multiplication result
        400:
            description: Validation error
        500:
            description: Internal server error
    """
    logger.info("Enter multiply endpoint")
    data = request.json
    schema = DoublePolySchema()

    try:
        schema.load(data)
    except ValidationError as e:
        logger.info(f"Validation error in multiply endpoint: {e.messages}")
        return jsonify({'error': e.messages}), 400
    
    m = data['m']
    bits = data['bits']
    type = data['type']

    service = PolyServices()
    
    try:
        poly1 = data[type + '1']
        poly2 = data[type + '2']

        poly1 = hex_bin_to_int(poly1, type)
        poly2 = hex_bin_to_int(poly2, type)
          
        result = service.multiply_in_gf(m, poly1, poly2)
        hex_result, bin_result = int_to_hex_bin(result, bits)

        logger.info("Exit multiply endpoint")
        return jsonify({
            'result': {
                'hex': hex_result,
                'bin': bin_result
            }
        }), 200
    except Exception as e:
        logger.error(f"An unexpected error occurred in multiply endpoint: {str(e)}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


@poly_endpoints.route('/divide', methods=['POST'])
def divide():
    """
    Divide two polynomials in GF(2^m)
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
            description: Polynomial multiplication result
        400:
            description: Validation error
        404:
            description: Division by zero
        405:
            description: Polynomial not invertible
        500:
            description: Internal server error
    """
    logger.info("Enter divide endpoint")
    data = request.json
    schema = DoublePolySchema()

    try:
        schema.load(data)
    except ValidationError as e:
        logger.info(f"Validation error in divide endpoint: {e.messages}")
        return jsonify({'error': e.messages}), 400
    
    m = data['m']
    bits = data['bits']
    type = data['type']

    service = PolyServices()
    
    try:
        dividend = data[type + '1']
        divisor = data[type + '2']

        dividend = hex_bin_to_int(dividend, type)
        divisor = hex_bin_to_int(divisor, type)
        
        result = service.divide_in_gf(m, dividend, divisor)

        result_hex, result_bin = int_to_hex_bin(result, bits)

        logger.info("Exit divide endpoint")
        return jsonify({
            'hex': result_hex,
            'bin': result_bin
        }), 200
    except ZeroDivisionError as e:
        return jsonify({'error': str(e)}), 404
    except ValueError as e:
        return jsonify({'error': str(e)}), 405
    except Exception as e:
        logger.error(f"An unexpected error occurred in divide endpoint: {str(e)}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500
    
@poly_endpoints.route('/modulo', methods=['POST'])
def modulo():
    """
    Modulo reduce a polynomial in GF(2^m)
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
            - bin
            - hex
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
            bin:
              type: string
              description: Polynomial in binary
            hex:
              type: string
              description: Polynomial in hexadecimal 
    responses:
        200:
            description: Polynomial modulo reduction result
        400:
            description: Validation error
        500:
            description: Internal server error
    """
    logger.info("Enter modulo endpoint")
    data = request.json
    schema = SinglePolySchema()

    try:
        schema.load(data)
    except ValidationError as e:
        logger.info(f"Validation error in modulo endpoint: {e.messages}")
        return jsonify({'error': e.messages}), 400
    
    m = data['m']
    bits = data['bits']
    type = data['type']

    service = PolyServices()
    
    try:
        poly = data[type]
        poly = hex_bin_to_int(poly, type)

        result = service.modulo_in_gf(m, poly)
        hex_result, bin_result = int_to_hex_bin(result, bits)

        logger.info("Exit modulo endpoint")
        return jsonify({
            'result': {
                'hex': hex_result,
                'bin': bin_result
            }
        }), 200
    except Exception as e:
        logger.error(f"An unexpected error occurred in modulo endpoint: {str(e)}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500
    
@poly_endpoints.route('/invert', methods=['POST'])
def invert():
    """
    Invert a polynomial in GF(2^m)
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
            - bin
            - hex
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
            bin:
              type: string
              description: Polynomial in binary
            hex:
              type: string
              description: Polynomial in hexadecimal
    responses:
        200:
            description: Polynomial inversion result
        400:
            description: Validation error
        405:
            description: Polynomial not invertible
        500:
            description: Internal server error
    """
    logger.info("Enter invert endpoint")
    data = request.json
    schema = SinglePolySchema()

    try:
        schema.load(data)
    except ValidationError as e:
        logger.info(f"Validation error in invert endpoint: {e.messages}")
        return jsonify({'error': e.messages}), 400
    
    m = data['m']
    bits = data['bits']
    type = data['type']

    service = PolyServices()

    try:
        poly = data[type]
        poly = hex_bin_to_int(poly, type)

        result = service.invert_in_gf(m, poly)
        hex_result, bin_result = int_to_hex_bin(result,bits)

        logger.info("Exit invert endpoint")
        return jsonify({
            'result': {
                'hex': hex_result,
                'bin': bin_result
            }
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 405
    except Exception as e:
        logger.error(f"An unexpected error occurred in invert endpoint: {str(e)}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500
