from marshmallow import Schema, fields


class ErrorBodySchema(Schema):
    status = fields.Str()
    status_code = fields.Int()
    type = fields.Str()
    category = fields.Str()
    message = fields.Str()


class ErrorSchema(Schema):
    error = fields.Nested(ErrorBodySchema)
