from typing import List

from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(80), nullable=False, unique=True)
    name = db.Column(db.String(80), nullable=False)
    msrp_price = db.Column(db.Float(precision=2), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    ean_code = db.Column(db.Integer, nullable=True)

    warehouse_id = db.Column(db.Integer, db.ForeignKey("warehouses.id"), nullable=False)
    warehouse = db.relationship("WarehouseModel", back_populates="items")

    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    category = db.relationship("CategoryModel", back_populates="items")

    @classmethod
    def find_by_code(cls, code: str) -> "ItemModel":
        return cls.query.filter_by(code=code).first()

    @classmethod
    def find_all(cls) -> List["ItemModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
