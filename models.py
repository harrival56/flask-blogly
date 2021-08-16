"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
def connect_db(app):
    db.app = app
    db.init_app(app)



class User(db.Model):
    __tablename__ = 'users'

    @classmethod
    def user_list(cls):
        return cls.query.all()


    def __repr__(self):
        player = self
        return f"<User = id={player.id} first_name={player.first_name} last_name={player.last_name} url={player.image_url} "

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)
    image_url = db.Column(db.String, nullable=False)


    def greet(self):
        """greets user"""
        return f"Hi, welcome to my profile page, I'm {self.first_name} {self.last_name}"