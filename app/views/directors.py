from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.director import DirectorSchema
from app.helpers import auth_required, admin_required
from app.implemented import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        return directors_schema.dump(director_service.get_all()), 200

    @admin_required
    def post(self):
        data = request.json
        director_service.create(data)
        return "", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        return director_schema.dump(director_service.get_one(did)), 200

    @admin_required
    def put(self, did):
        data = request.json
        if "id" not in data:
            data["id"] = did
        director_service.update(data)
        return "", 204

    @admin_required
    def delete(self, did):
        director_service.delete(did)
        return "", 204
