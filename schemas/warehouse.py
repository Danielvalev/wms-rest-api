from ma import ma
from models.warehouse import WarehouseModel
from schemas.item import ItemSchema


class WarehouseSchema(ma.SQLAlchemyAutoSchema):
    items = ma.Nested(ItemSchema, many=True)

    class Meta:
        model = WarehouseModel
        load_instance = True
        dump_only = ("id",)
        include_fk = True
