from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from src.services import PolyServices
from src.schemas import ArithmeticPolySchema
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
