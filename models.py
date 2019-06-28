"""Models for Adopt."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pets."""

    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
        )

    name = db.Column(
        db.String(50),
        nullable=False
        )

    species = db.Column(
        db.String(50),
        nullable=False
        )

    photo_url = db.Column(
        db.Text,
        nullable=True,
        default='https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/South_Shetland-2016-Deception_Island%E2%80%93Chinstrap_penguin_%28Pygoscelis_antarctica%29_04.jpg/220px-South_Shetland-2016-Deception_Island%E2%80%93Chinstrap_penguin_%28Pygoscelis_antarctica%29_04.jpg'
        )

    age = db.Column(
        db.Integer,
        nullable=False
        )

    notes = db.Column(
        db.Text,
        nullable=True
        )

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
        )

