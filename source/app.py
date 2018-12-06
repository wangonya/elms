from flask import Flask
from flask_restful import Api

from source.leaves import RequestLeave, GetAllUserLeaves, GetUserLeaveHistory, WithdrawLeave, CancelLeave, RespondToRequests

app = Flask(__name__)
api = Api(app)
app.config['PROPAGATE_EXCEPTIONS'] = True  # To allow flask propagating exception even if debug is set to false on app


@app.route('/')
def index():
    return 'Hello World!'


# Routes
api.add_resource(RequestLeave, '/leaves')
api.add_resource(RespondToRequests, '/leaves/<int:leave_id>')
api.add_resource(GetAllUserLeaves, '/leaves/<string:uid>')
api.add_resource(GetUserLeaveHistory, '/users/<string:uid>/leaves')
api.add_resource(WithdrawLeave, '/users/<string:uid>/leaves/<int:leave_id>/withdraw')
api.add_resource(CancelLeave, '/users/<string:uid>/leaves/<int:leave_id>/cancel')

if __name__ == '__main__':
    app.run(debug=True)
