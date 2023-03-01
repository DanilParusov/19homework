from app.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, director):
        new_director = Director(**director)
        self.session.add(new_director)
        self.session.commit()
        return new_director

    def delete(self, did):
        director = self.get_one(did)
        self.session.delete(director)
        self.session.commit()

    def update(self, director):
        director_update = self.get_one(director.get("id"))
        director_update.name = director.get("name")

        self.session.add(director_update)
        self.session.commit()
