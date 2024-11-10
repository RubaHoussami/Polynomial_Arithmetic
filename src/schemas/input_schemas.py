from marshmallow import Schema, fields, validate, ValidationError, validates_schema

class InputSchema(Schema):
    m = fields.Integer(required=True, validate=validate.Range(min=1, max=2**13))
    bits = fields.Integer(required=True, validate=validate.OneOf([16, 32, 64, 128, 256]))
    type = fields.String(required=True, validate=validate.OneOf(['bin', 'hex']))
    bin = fields.String(required=False, validate=validate.Regexp(r'^[01]*$'))
    hex = fields.String(required=False, validate=validate.Regexp(r'^[0-9A-F]*$'))

    @validates_schema
    def validate_input(self, data, **kwargs):
        if not data['bin'] and not data['hex']:
            raise ValidationError('Either bin or hex must be provided')

        if data['bin'] and data['hex']:
            raise ValidationError('Either bin or hex must be provided, not both')
        
        if data['type'] == 'bin' and not data['bin']:
            raise ValidationError('bin is required when type is bin')

        if data['type'] == 'hex' and not data['hex']:
            raise ValidationError('hex is required when type is hex')
        
        if data['type'] == 'bin' and len(data['bin']) != 2 ** data['bits']:
            raise ValidationError('bin must be of length 2^bits')

        if data['type'] == 'hex' and len(data['hex']) != data['bits'] / 4:
            raise ValidationError('hex must be of length bits / 4')


