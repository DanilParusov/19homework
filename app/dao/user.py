from app.dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user):
        new_user = User(**user)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user):
        user_update = self.get_one(user.get("id"))
        user_update.name = user.get("name")
        user_update.password = user.get("password")

        self.session.add(user_update)
        self.session.commit()
