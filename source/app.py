from flask import Flask
from flask_restful import Api

from source.leaves import RequestLeave

app = Flask(__name__)
api = Api(app)
app.config['PROPAGATE_EXCEPTIONS'] = True  # To allow flask propagating exception even if debug is set to false on app


@app.route('/')
def index():
    return 'Hello World!'


# Routes
api.add_resource(RequestLeave, '/leaves')

if __name__ == '__main__':
    app.run(debug=True)
