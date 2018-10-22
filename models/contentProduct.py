from marshmallow import Schema, fields


class ContentProduct(object):
    def __init__(self, product_id, name, introduction, price, quantity):
        self.product_id = product_id
        self.name = name
        self.introduction = introduction
        self.price = price
        self.quantity = quantity


class ProductSchema(Schema):
    product_id = fields.Str(attribute="_id")
    name = fields.Str()
    introduction = fields.Str()
    price = fields.Number()
    quantity = fields.Number()
