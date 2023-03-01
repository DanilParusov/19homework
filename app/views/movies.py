from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.movie import MovieSchema
from app.helpers import auth_required, admin_required
from app.implemented import movie_service

movie_ns = Namespace('movies')

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        filters = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
        }
        return movies_schema.dump(movie_service.get_all(filters)), 200

    @admin_required
    def post(self):
        data = request.json
        movie_service.create(data)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    @auth_required
    def get(self, mid):
        return movie_schema.dump(movie_service.get_one(mid)), 200

    @admin_required
    def put(self, mid):
        data = request.json
        if "id" not in data:
            data["id"] = mid
        movie_service.update(data)
        return "", 204

    @admin_required
    def delete(self, mid):
        movie_service.delete(mid)
        return "", 204
