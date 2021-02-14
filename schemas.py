from marshmallow import Schema, validate, fields


class VideoSchema(Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=[
        validate.Length(max=250)])
    description = fields.String(required=True, validate=[
        validate.Length(max=500)])
    massage = fields.String(dump_only=True)


class UserSchema(Schema):
    name = fields.String(required=True, validate=[
        validate.Length(max=250)])
    email = fields.String(required=True, validate=[
        validate.Length(max=250)])
    password = fields.String(required=True, validate=[
        validate.Length(max=100)])


class AuthScheme(Schema):


