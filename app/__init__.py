from flask import Flask,jsonify

from app.api.v1.view import blueprint


app = Flask(__name__)


def create_app():
    app.register_blueprint(blueprint, url_prefix='/api/v1')
    return app


@app.errorhandler(404)
def error_handler(e):
    return jsonify({
        "status":404,
        "error":"bad request not found"
    }),404


@app.errorhandler(405)
def method_error_handler(e):
    return jsonify(
        {
            "status":405,
            "error":"method not allowed"
        }
    ),405
