import os
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from source.resources.leaves import RequestLeave, GetAllUserLeaves, \
    WithdrawLeave, CancelLeave, RespondToRequests
from source.resources.user import UserRegister, UserLogin
from source.db import db


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['PROPAGATE_EXCEPTIONS'] = True  # To allow flask propagating exception even if debug is set to false on app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.testing = True
app.config['JWT_SECRET_KEY'] = 'elms-project'
jwt = JWTManager(app)
CORS(app)


@app.route('/')
def index():
    return 'Hello World!'


@app.before_first_request
def create_tables():
    db.create_all()


# Routes
api.add_resource(RequestLeave, '/leaves')
api.add_resource(RespondToRequests, '/leaves/<int:l_id>')
api.add_resource(GetAllUserLeaves, '/leaves/<string:uid>')
api.add_resource(WithdrawLeave, '/leaves/<int:l_id>/withdraw')
api.add_resource(CancelLeave, '/leaves/<int:l_id>/cancel')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')


if __name__ == '__main__':
    app.run(debug=True)
