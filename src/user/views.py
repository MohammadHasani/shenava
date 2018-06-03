from flask import jsonify, json, render_template, request
from . import user_blureprint
from .models import User
from src.authentication.models import AuthenticationManager
from flask_login import login_required, current_user
from mongoengine import errors as MongoEngineException


@user_blureprint.route('/register', methods=['post'])
def register():
    req_json = request.get_json()
    phonenumber = req_json.get('phonenumber')
    email = req_json.get('email')
    fname = req_json.get('fname')
    lname = req_json.get('lname')
    sex = req_json.get('sex')
    age = req_json.get('age')
    address = req_json.get('address')
    melli_code = req_json.get('melli_code')

    try:
        if req_json.get('password') == req_json.get('confirm_password'):
            password = req_json.get('password')
    except:
        return jsonify({'result': False, 'code': 403})
    try:
        AuthenticationManager.register_user(phonenumber, email, password, fname, lname, sex, age, address, melli_code)

        return jsonify({'result': True, 'code': 200})
    except MongoEngineException.NotUniqueError:
        return jsonify({'result': False, 'code': 409})
    except MongoEngineException.ValidationError as e:
        for i, j in e.errors.items():
            print(i, j)
            return jsonify({'result': False, 'error': str(e)})


@user_blureprint.route('/login', methods=['post'])
@login_required
def login():
    return jsonify({'result': True, 'code': 200})

    # req_json = request.get_json()
    # phonenumber = req_json.get('phonenumber')
    # password = req_json.get('password')
    # try:
    #     res = AuthenticationManager.check_auth(phonenumber, password)
    #     print(res)
    #     if res:
    #         return jsonify({'result': True, 'code': 200})
    #     else:
    #         return jsonify({'result': False, 'code': 404})
    # except MongoEngineException.DoesNotExist:
    #     print('fuck')
    #     return jsonify({'result': False, 'code': 404})
    # except Exception as e:
    #     print(e)
    #     return jsonify({'result': False, 'code': 500})


@user_blureprint.route('/currentuser', methods=['get'])
@login_required
def CurrentUser():
    return jsonify({'user_info': {
        'fname': current_user.fname,
        'lname': current_user.lname,
        'age': current_user.age,
        'email': current_user.email,
        'sex': current_user.sex,
        'address': current_user.address,
        'melli_code': current_user.melli_code,
        'role': current_user.role,
        'register_time': current_user.datetime}
        , 'code': 200})


@user_blureprint.route('/dropdb')
def drop_db():
    from src import db
    db.connection.drop_database('shenava')
    return'done'