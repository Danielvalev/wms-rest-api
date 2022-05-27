from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required
from models.item import ItemModel
from schemas.item import ItemSchema
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')
fh = logging.FileHandler('item.log')
fh.setFormatter(formatter)

logger.addHandler(fh)

CODE_ALREADY_EXISTS = "An item with code '{}' already exists."
ERROR_INSERTING = "An error occurred while inserting the item."
ITEM_NOT_FOUND = "Item not found."
ITEM_DELETED = "Item deleted."
INCORRECT_DATA = "Incorrect input data."

item_schema = ItemSchema()
item_list_schema = ItemSchema(many=True)


class Item(Resource):
    @classmethod
    def get(cls, code: str):
        item = ItemModel.find_by_code(code)
        if item:
            return item_schema.dump(item), 200

        return {"message": ITEM_NOT_FOUND}, 404

    @classmethod
    @jwt_required(fresh=True)
    def post(cls, code: str):
        if ItemModel.find_by_code(code):
            return {"message": CODE_ALREADY_EXISTS.format(code)}, 400

        item_json = request.get_json()
        item_json["code"] = code

        item = item_schema.load(item_json)

        try:
            item.save_to_db()
        except:
            return {"message": ERROR_INSERTING}, 500

        return item_schema.dump(item), 201

    @classmethod
    @jwt_required()
    def delete(cls, code: str):
        item = ItemModel.find_by_code(code)
        if item:
            item.delete_from_db()
            return {"message": ITEM_DELETED}, 200

        return {"message": ITEM_NOT_FOUND}, 404

    @classmethod
    @jwt_required(fresh=True)
    def put(cls, code: str):
        item_json = request.get_json()
        item = ItemModel.find_by_code(code)

        if item:
            item.msrp_price = item_json['msrp_price']
            item.price = item_json['price']
            item.name = item_json['name']
            item.ean_code = item_json['ean_code']

        else:
            item_json['code'] = code
            item = item_schema.load(item_json)

        try:
            item.save_to_db()
        except Exception as err:
            logger.info(err)
            return {"message": INCORRECT_DATA}, 400

        return item_schema.dump(item), 200


class ItemList(Resource):
    @classmethod
    def get(cls):
        return {"items": item_list_schema.dump(ItemModel.find_all())}, 200
