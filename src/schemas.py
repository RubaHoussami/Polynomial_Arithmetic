from marshmallow import Schema, fields, validate, ValidationError, validates_schema

class InputSchema(Schema):
    m = fields.Integer(required=True, validate=validate.Range(min=1, max=2**13))
    bits = fields.Integer(required=True, validate=validate.OneOf([16, 32, 64, 128, 256]))
    type = fields.String(required=True, validate=validate.OneOf(['bin', 'hex']))
    bin = fields.String(required=False, validate=validate.Regexp(r'^[01]*$'))
    hex = fields.String(required=False, validate=validate.Regexp(r'^[0-9A-F]*$'))

    @validates_schema
    def validate_input(self, data, **kwargs):
        if 'bin' not in data or 'hex' not in data:
            raise ValidationError('Either bin or hex must be provided')

        if data['bin'] and data['hex']:
            raise ValidationError('Either bin or hex must be provided, not both')
        
        if data['type'] == 'bin' and not data['bin']:
            raise ValidationError('bin is required when type is bin')

        if data['type'] == 'hex' and not data['hex']:
            raise ValidationError('hex is required when type is hex')
        
        if data['type'] == 'bin' and len(data['bin']) != data['bits']:
            raise ValidationError('bin must be of length bits')

        if data['type'] == 'hex' and len(data['hex']) != data['bits'] / 4:
            raise ValidationError('hex must be of length bits / 4')

class ArithmeticPolySchema(Schema):
    m = fields.Integer(required=True, validate=validate.Range(min=1, max=2**13))
    bits = fields.Integer(required=True, validate=validate.OneOf([16, 32, 64, 128, 256]))
    type = fields.String(required=True, validate=validate.OneOf(['bin', 'hex']))
    bin1 = fields.String(required=False, validate=validate.Regexp(r'^[01]*$'))
    hex1 = fields.String(required=False, validate=validate.Regexp(r'^[0-9A-F]*$'))
    bin2 = fields.String(required=False, validate=validate.Regexp(r'^[01]*$'))
    hex2 = fields.String(required=False, validate=validate.Regexp(r'^[0-9A-F]*$'))

    @validates_schema
    def validate_input(self, data, **kwargs):
        if 'bin1' not in data and 'hex1' not in data:
            raise ValidationError('Either bin1 or hex1 must be provided')

        if 'bin1' in data and 'hex1' in data:
            raise ValidationError('Either bin1 or hex1 must be provided, not both')
        
        if data['type'] == 'bin' and 'bin1' not in data:
            raise ValidationError('bin1 is required when type is bin')

        if data['type'] == 'hex' and 'hex1' not in data:
            raise ValidationError('hex1 is required when type is hex')
        
        if data['type'] == 'bin' and len(data['bin1']) != data['bits']:
            raise ValidationError('bin1 must be of length bits')

        if data['type'] == 'hex' and len(data['hex1']) != data['bits'] / 4:
            raise ValidationError('hex1 must be of length bits / 4')

        if 'bin2' not in data and 'hex2' not in data:
            raise ValidationError('Either bin2 or hex2 must be provided')

        if 'bin2' in data and 'hex2' in data:
            raise ValidationError('Either bin2 or hex2 must be provided, not both')
        
        if data['type'] == 'bin' and 'bin2' not in data:
            raise ValidationError('bin2 is required when type is bin')

        if data['type'] == 'hex' and 'hex2' not in data:
            raise ValidationError('hex2 is required when type is hex')
        
        if data['type'] == 'bin' and len(data['bin2']) != data['bits']:
            raise ValidationError('bin2 must be of length bits')

        if data['type'] == 'hex' and len(data['hex2']) != data['bits'] / 4:
            raise ValidationError('hex2 must be of length bits / 4')