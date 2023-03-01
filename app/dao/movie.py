from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director_id(self, val):
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self, val):
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year(self, val):
        return self.session.query(Movie).filter(Movie.year == val).all()

    def create(self, movie):
        new_movie = Movie(**movie)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie):
        movie_update = self.get_one(movie.get("id"))
        movie_update.title = movie.get("title")
        movie_update.description = movie.get("description")
        movie_update.trailer = movie.get("trailer")
        movie_update.year = movie.get("year")
        movie_update.rating = movie.get("rating")
        movie_update.genre_id = movie.get("genre_id")
        movie_update.director_id = movie.get("director_id")

        self.session.add(movie_update)
        self.session.commit()
