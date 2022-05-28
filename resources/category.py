from flask_restful import Resource
from flask import request
from models.category import CategoryModel
from schemas.category import CategorySchema
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')
fh = logging.FileHandler('category.log')
fh.setFormatter(formatter)

logger.addHandler(fh)

NAME_ALREADY_EXISTS = "A category with name '{}' already exists."
ERROR_INSERTING = "An error occurred while inserting the category."
CATEGORY_NOT_FOUND = "Category not found."
CATEGORY_DELETED = "Category deleted."
INCORRECT_DATA = "Incorrect input data."

category_schema = CategorySchema()
category_list_schema = CategorySchema(many=True)


class Category(Resource):
    @classmethod
    def get(cls, name: str):
        category = CategoryModel.find_by_name(name)
        if category:
            return category_schema.dump(category), 200

        return {"message": CATEGORY_NOT_FOUND}, 404

    @classmethod
    def post(cls, name: str):
        if CategoryModel.find_by_name(name):
            return {"message": NAME_ALREADY_EXISTS.format(name)}, 400

        category_json = request.get_json()
        category_short_name = category_json["short_name"]

        category = CategoryModel(name=name, short_name=category_short_name)

        try:
            category.save_to_db()
        except:
            return {"message": ERROR_INSERTING}, 500

        return category_schema.dump(category), 201

    @classmethod
    def delete(cls, name: str):
        category = CategoryModel.find_by_name(name)
        if category:
            category.delete_from_db()
            return {"message": CATEGORY_DELETED}, 200

        return {"message": CATEGORY_NOT_FOUND}, 404

    @classmethod
    def put(cls, name: str):
        category_json = request.get_json()
        category = CategoryModel.find_by_name(name)

        if category:
            category.short_name = category_json["short_name"]

        else:
            category_json['name'] = name
            category = category_schema.load(category_json)

        try:
            category.save_to_db()
        except Exception as err:
            logger.info(err)
            return {"message": INCORRECT_DATA}, 400

        return category_schema.dump(category), 200


class CategoryList(Resource):
    @classmethod
    def get(cls):
        return {"categories": category_list_schema.dump(CategoryModel.find_all())}, 200
