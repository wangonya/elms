from flask_restful import Resource, reqparse


class RequestLeave(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('uid',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
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
    parser.add_argument('status',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        return {'msg': 'leave successfully requested'}, 201

    def get(self):
        return {'data': 'all leaves'}, 200


class RespondToRequests(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('leave_id',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('status',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    def patch(self, leave_id):
        return {'msg': 'leave {} responded to by admin'.format(leave_id)}, 200


class GetAllUserLeaves(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('uid',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    def get(self, uid):
        return {'data': uid}, 200


class GetUserLeaveHistory(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('uid',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    def get(self, uid):
        return {'data': uid}, 200


class WithdrawLeave(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('uid',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('leave_id',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('status',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    def patch(self, uid, leave_id):
        return {'data': uid, 'msg': 'leave {} withdrawn'.format(leave_id)}, 200


class CancelLeave(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('uid',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('leave_id',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('status',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    def patch(self, uid, leave_id):
        return {'data': uid, 'msg': 'leave {} cancelled'.format(leave_id)}, 200