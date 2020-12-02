from sqlalchemy.sql import Select

from app.misc import db
from app.models.user import UserRelatedModel


class ShoppingList(UserRelatedModel):
    __tablename__ = "shopping_lists"

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    query: Select
