from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.user import UserSchema
from app.implemented import user_service

user_ns = Namespace('users')

users_schema = UserSchema(many=True)
user_schema = UserSchema()


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        return users_schema.dump(user_service.get_all()), 200

    def post(self):
        data = request.json
        user_service.create(data)
        return "", 201


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        return user_schema.dump(user_service.get_one(uid)), 200

    def put(self, uid):
        data = request.json
        if "id" not in data:
            data["id"] = uid

        user_service.update(data)
        return "", 204

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204
