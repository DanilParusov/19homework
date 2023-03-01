from app.dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, genre):
        new_genre = Genre(**genre)
        self.session.add(new_genre)
        self.session.commit()
        return new_genre

    def delete(self, gid):
        genre = self.get_one(gid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, genre):
        genre_update = self.get_one(genre.get("id"))
        genre_update.name = genre.get("name")

        self.session.add(genre_update)
        self.session.commit()
