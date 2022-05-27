from typing import List

from db import db


class WarehouseModel(db.Model):
    __tablename__ = "warehouses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    capacity = db.Column(db.Float(precision=2), nullable=False)
    address = db.Column(db.String(120), nullable=True)

    items = db.relationship("ItemModel", lazy="dynamic")

    @classmethod
    def find_by_name(cls, name: str) -> "WarehouseModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> List["WarehouseModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()