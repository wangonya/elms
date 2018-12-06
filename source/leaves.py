from flask_restful import Resource, reqparse


class RequestLeave(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('type',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('from',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('to',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('details',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        return {'msg': 'leave successfully requested'}, 201

    def get(self):
        return {'data': 'all leaves'}, 200
