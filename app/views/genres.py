from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.genre import GenreSchema
from app.helpers import auth_required, admin_required
from app.implemented import genre_service

genre_ns = Namespace('genres')

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        return genres_schema.dump(genre_service.get_all()), 200

    @admin_required
    def post(self):
        data = request.json
        genre_service.create(data)
        return "", 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        return genre_schema.dump(genre_service.get_one(gid)), 200

    @admin_required
    def put(self, gid):
        data = request.json
        if "id" not in data:
            data["id"] = gid
        genre_service.update(data)
        return "", 204

    @admin_required
    def delete(self, gid):
        genre_service.delete(gid)
        return "", 204
