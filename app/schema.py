from marshmallow import Schema, fields

class BookSchema(Schema):
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    published_year = fields.Int(required=True)
    isbn = fields.Str(required=True)
    genre = fields.Str(required=False)
    