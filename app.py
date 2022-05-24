from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from db import db
from resources.user import UserRegister, User
import os

# env
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # turn off Flask modification tracker
app.secret_key = os.getenv('FLASK_SECRET_KEY')
api = Api(app)


# creating database
@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(UserRegister, '/register')  # {{url}}/register
api.add_resource(User, "/user/<int:user_id>")  # {{url}}/user/<id>

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
