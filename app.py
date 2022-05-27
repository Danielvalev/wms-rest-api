from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from blocklist import BLOCKLIST
from dotenv import load_dotenv
from db import db
from ma import ma
from resources.user import UserRegister, User, UserLogin, UserLogout, TokenRefresh
from resources.item import Item, ItemList
from resources.warehouse import Warehouse, WarehouseList
from marshmallow import ValidationError
import os

# env
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # turn off Flask modification tracker
app.config['JWT_BLACKLIST_ENABLED'] = True  # enable blacklist feature
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']  # allow blacklisting for access and refresh tokens
app.config['PROPAGATE_EXCEPTIONS'] = True  # for errorhandler
app.secret_key = os.getenv('FLASK_SECRET_KEY')
api = Api(app)


# creating database
@app.before_first_request
def create_tables():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


jwt = JWTManager(app)


# This function will check if a token is block listed, and will be called automatically when blocklist is enabled
@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    return jwt_payload["jti"] in BLOCKLIST


# User resources
api.add_resource(UserRegister, '/register')  # {{url}}/register
api.add_resource(User, "/user/<int:user_id>")  # {{url}}/user/<id>
api.add_resource(UserLogin, "/login")  # {{url}}/login
api.add_resource(UserLogout, "/logout")  # {{url}}/logout
api.add_resource(TokenRefresh, "/refresh")  # {{url}}/refresh

# Item resources
api.add_resource(Item, "/item/<string:code>")  # {{url}}/item/<code>
api.add_resource(ItemList, "/items")  # {{url}}/items

# Warehouse resources
api.add_resource(Warehouse, "/warehouse/<string:name>")  # {{url}}/warehouse/<name>
api.add_resource(WarehouseList, "/warehouses")  # {{url}}/warehouses

if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
