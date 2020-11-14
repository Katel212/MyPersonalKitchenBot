from app.misc import db
from app.models.user import UserRelatedModel


class Product(UserRelatedModel):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    name = db.Column(db.String, nullable=False)
    expiration_date = db.Column(db.Date)
    bought_date = db.Column(db.Date)
    info = db.Column(db.String)
