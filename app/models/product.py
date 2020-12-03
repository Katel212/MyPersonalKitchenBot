from datetime import datetime

from sqlalchemy.sql import Select

from app.misc import db
from app.models.user import UserRelatedModel


class Product(UserRelatedModel):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    name = db.Column(db.String, nullable=False)
    expiration_date = db.Column(db.Date)
    bought_date = db.Column(db.Date)
    info = db.Column(db.String)
    query: Select

    @staticmethod
    def create_product(id: int, name: str, expiration_date: datetime, bought_date: datetime, info: str, user_id: int):
        product = Product()
        product.id = id
        product.name = name
        product.expiration_date = expiration_date
        product.bought_date = bought_date
        product.info = info
        product.user_id = user_id
        return product
