from ma import ma
from models.user import UserModel


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True  # Whether to load model instances
        load_only = ("password",)
        dump_only = ("id",)
