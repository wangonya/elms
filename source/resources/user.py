from flask_restful import Resource, reqparse
from source.models.user import UserModel
from flask_jwt_extended import (create_access_token)


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('uid',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_uid(data['uid']):
            return {'status': 400, "message": "A user with that username already exists"}, 400

        user = UserModel(data['uid'], UserModel.generate_hash(data['password']), False)
        user.save_to_db()

        return {'status': 201, "message": "User created successfully."}, 201


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('uid',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = UserLogin.parser.parse_args()
        user = UserModel.find_by_uid(data['uid'])

        if user is None:
            return {'status': 401, 'message': "User '{}' does not exist".format(data['uid'])}, 401
        else:
            pwd_verify_hash = UserModel.verify_hash(data['password'], user.password)

            if pwd_verify_hash:
                access_token = create_access_token(identity=data['uid'])
                is_admin = False
                if UserModel.find_by_admin(data['uid']):
                    is_admin = True
                return {
                           'status': 200,
                           'token': access_token,
                           'uid': data['uid'],
                           'is_admin': is_admin
                       }, 200
            else:
                return {'status': 401, 'message': "Wrong password"}, 401
