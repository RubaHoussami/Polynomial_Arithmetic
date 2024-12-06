from flask import Flask, jsonify
from src.extensions import swagger
from src.logger import logger
from src.controllers import poly_endpoints

def create_app():
    app = Flask(__name__)
    swagger.init_app(app)
    app.register_blueprint(poly_endpoints)
    return app

app = create_app()

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to the Polynomial Arithmetic App'}), 200


if __name__ == '__main__':
    logger.info('Starting the Polynomial Arithmetic App')
    app.run(debug=True)
