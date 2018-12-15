from flask_restful import Resource, reqparse
from source.models.leaves import LeaveModel
from flask_jwt_extended import jwt_required


class RequestLeave(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('uid',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('l_type',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('l_from',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('l_to',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('l_details',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('l_status',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    @jwt_required
    def post(self):
        data = RequestLeave.parser.parse_args()
        leave = LeaveModel(**data)

        if LeaveModel.find_by_status(data['uid']):
            return {'message': "Hi {}. Your last leave application status is still {}."
                    .format(data['uid'], data['l_status'])}, 400

        try:
            leave.save_to_db()
        except:
            return {"message": "An error occurred while inserting the data."}, 500

        return leave.json(), 201

    @jwt_required
    def get(self):
        return list(map(lambda x: x.json(), LeaveModel.query.all())), 200


class RespondToRequests(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('l_status',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    @jwt_required
    def patch(self, l_id):
        data = RespondToRequests.parser.parse_args()
        leave = LeaveModel.find_by_l_id(l_id)

        if leave:
            leave.l_status = data['l_status']
            leave.save_to_db()
            return leave.json(), 200
        else:
            return {'message': 'No leave with id {}'.format(l_id)}, 404


class GetAllUserLeaves(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('uid',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    @jwt_required
    def get(self, uid):
        leave = LeaveModel.find_by_uid_all(uid)

        if leave:
            return list(map(lambda x: x.json(), leave)), 200
        else:
            return {'message': 'An error occurred while fetching the data.'}, 500


class WithdrawLeave(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('l_status',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    @jwt_required
    def patch(self, l_id):
        data = WithdrawLeave.parser.parse_args()
        leave = LeaveModel.find_by_l_id(l_id)

        if leave.l_status == 'pending approval':
            leave.l_status = data['l_status']
            leave.save_to_db()
            return leave.json(), 200
        else:
            return {'message': 'Cannot withdraw leave with status {}. Request a cancel from admin.'
                    .format(leave.l_status)}, 400


class CancelLeave(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('l_status',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    @jwt_required
    def patch(self, l_id):
        leave = LeaveModel.find_by_l_id(l_id)
        data = CancelLeave.parser.parse_args()

        if leave.l_status != 'pending approval':
            leave.l_status = data['l_status']
            leave.save_to_db()
            return leave.json(), 200
        else:
            return {'message': 'Cannot cancel leave with status {}. Withdraw request instead.'
                    .format(leave.l_status)}, 400
