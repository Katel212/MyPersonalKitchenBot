from app.misc import db
from app.models import Product, ShoppingList
from app.models.base import BaseModel


class ShoppingListToProduct(BaseModel):
    __tablename__ = "shopping_list_to_product"

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    product_id = db.Column(
        db.ForeignKey(f"{Product.__tablename__}.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    shopping_list_id = db.Column(
        db.ForeignKey(f"{ShoppingList.__tablename__}.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
