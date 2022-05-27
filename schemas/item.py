from ma import ma
from models.item import ItemModel
from models.warehouse import WarehouseModel


class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemModel
        load_instance = True  # Whether to load model instances
        load_only = ("",)  # Not going to be returned
        dump_only = ("id",)
        include_fk = True
