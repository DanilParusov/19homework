from app.dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        return self.dao.get_one(did)

    def get_all(self):
        return self.dao.get_all()

    def create(self, director):
        return self.dao.create(director)

    def update(self, director):
        self.dao.update(director)
        return self.dao

    def delete(self, did):
        self.dao.delete(did)
