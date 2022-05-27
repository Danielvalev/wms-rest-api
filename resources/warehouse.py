from flask_restful import Resource
from flask import request
from models.warehouse import WarehouseModel
from schemas.warehouse import WarehouseSchema
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')
fh = logging.FileHandler('warehouse.log')
fh.setFormatter(formatter)

logger.addHandler(fh)

NAME_ALREADY_EXISTS = "A warehouse with name '{}' already exists."
ERROR_INSERTING = "An error occurred while inserting the warehouse."
WAREHOUSE_NOT_FOUND = "Warehouse not found."
WAREHOUSE_DELETED = "Warehouse deleted."
INCORRECT_DATA = "Incorrect input data."


warehouse_schema = WarehouseSchema()
warehouse_list_schema = WarehouseSchema(many=True)


class Warehouse(Resource):
    @classmethod
    def get(cls, name: str):
        warehouse = WarehouseModel.find_by_name(name)
        if warehouse:
            return warehouse_schema.dump(warehouse), 200

        return {"message": WAREHOUSE_NOT_FOUND}, 404

    @classmethod
    def post(cls, name: str):
        if WarehouseModel.find_by_name(name):
            return {"message": NAME_ALREADY_EXISTS.format(name)}, 400

        warehouse_json = request.get_json()
        warehouse_address = warehouse_json["address"]
        warehouse_capacity = warehouse_json["capacity"]

        warehouse = WarehouseModel(name=name, address=warehouse_address, capacity=warehouse_capacity)
        try:
            warehouse.save_to_db()
        except:
            return {"message": ERROR_INSERTING}, 500

        return warehouse_schema.dump(warehouse), 201

    @classmethod
    def delete(cls, name: str):
        warehouse = WarehouseModel.find_by_name(name)
        if warehouse:
            warehouse.delete_from_db()
            return {"message": WAREHOUSE_DELETED}, 200

        return {"message": WAREHOUSE_NOT_FOUND}, 404

    @classmethod
    def put(cls, name: str):
        warehouse_json = request.get_json()
        warehouse = WarehouseModel.find_by_name(name)

        if warehouse:
            warehouse.address = warehouse_json['address']
            warehouse.capacity = warehouse_json['capacity']

        else:
            warehouse_json['name'] = name
            warehouse = warehouse_schema.load(warehouse_json)

        try:
            warehouse.save_to_db()
        except Exception as err:
            logger.info(err)
            return {"message": INCORRECT_DATA}, 400

        return warehouse_schema.dump(warehouse), 200


class WarehouseList(Resource):
    @classmethod
    def get(cls):
        return {"warehouses": warehouse_list_schema.dump(WarehouseModel.find_all())}, 200
