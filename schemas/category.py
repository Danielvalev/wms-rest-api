from ma import ma
from models.category import CategoryModel
from schemas.item import ItemSchema


class CategorySchema(ma.SQLAlchemyAutoSchema):
    items = ma.Nested(ItemSchema, many=True)

    class Meta:
        model = CategoryModel
        load_instance = True
        dump_only = ("id",)
        include_fk = True
