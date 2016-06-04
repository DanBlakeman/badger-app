from app import db


class User(db.Model):
    """Holds information of the members of the site"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())
    first_name = db.Column(db.String())
    surname = db.Column(db.String())

    def __repr__(self):
        return 'User <id {}>'.format(self.id)
