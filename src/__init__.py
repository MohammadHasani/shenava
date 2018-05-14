from flask_mongoengine import MongoEngine
from flask import Flask, jsonify,request
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager()
login_manager.init_app(app)

db = MongoEngine(app)

from src.user import user_blureprint
from src.authentication import auth_blureprint
from src.exam import exam_blureprint

app.register_blueprint(user_blureprint, url_prefix='/user')
app.register_blueprint(auth_blureprint, url_prefix='/auth')
app.register_blueprint(exam_blureprint, url_prefix='/exam')


@app.errorhandler(401)
def error_401(error):
    return jsonify({'result': False, 'code': 401})
