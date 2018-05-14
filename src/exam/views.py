from flask import request, jsonify
from . import exam_blureprint
from .models import Exam, PureTone, Dichotic, Single,Binary,Ternary
from flask_login import current_user, login_required
from src.misc.constracts import EXAM_TYPE, EXAM_STATUS
from mongoengine import errors as MongoEngineError
from datetime import datetime


@exam_blureprint.route('/pure_tone', methods=['post'])
@login_required
def pure_tone():
    req_json = request.get_json()
    try:
        direction = req_json['dir']
        frequency = req_json['frequency']
        result = req_json['result']
        property = str(direction).title() + '_' + str(frequency)
        passed_exam_before = Exam.passed_exam_before(current_user.id)
        if passed_exam_before:
            pure_tone = passed_exam_before.pure_tone
            pure_tone[property] = result
            passed_exam_before.save()
        else:
            new_pure_tone = PureTone(start_time=datetime.utcnow())
            new_pure_tone.create(property, result)
            new_exam = Exam(user=current_user['id'], type=EXAM_TYPE['PURE_TONE'], pure_tone=new_pure_tone)
            new_exam.save()

        return jsonify({'result': True, 'code': 200})

    except MongoEngineError.ValidationError as e:
        print(e)
        return jsonify({'result': False, 'error': str(e)})
    except Exception as e:
        print(e)
        return jsonify({'result': False, 'error': str(e)})


@exam_blureprint.route('/pure_tone/report', methods=['get'])
@login_required
def pure_tone_report():
    try:
        exam = Exam.get_by_user_id(current_user.id)
        pure_tone_report = exam.pure_tone_report()
        return jsonify({'result': pure_tone_report, 'code': 200})
    except MongoEngineError.ValidationError as e:
        print(e)
        return jsonify({'result': False, 'error': str(e)})
    except Exception as e:
        print(e)
        return jsonify({'result': False, 'error': str(e)})


@exam_blureprint.route('/dichotic', methods=['post'])
@login_required
def dichotic():

    req_json = request.get_json()

    type = req_json['type']
    exam_number = req_json['exam_number']
    result = req_json['result']
    new_dicho = Dichotic()
    new_obj = eval(type.title())()

    new_obj.create(exam_number, result)
    new_dicho.create(type.title(), new_obj)
    print(new_dicho[type.title()])
    # new_pure_tone = PureTone(start_time=datetime.utcnow())
    # new_pure_tone.create(property, result)
    new_exam = Exam(user=current_user['id'], type=EXAM_TYPE['PURE_TONE'], dichotic=new_dicho)
    new_exam.save()

    # try:
    #     type = req_json['type']
    #     exam_number = req_json['exam_number']
    #     result = req_json['result']
    #     new_dicho = Dichotic()
    #
    #     new_obj = eval(type.title())()
    #
    #     passed_exam_before = Exam.passed_exam_before(current_user.id)
    #
    #     new_obj.create(exam_number, result)
    #     new_dicho.create(type.title(), new_obj)
    #     print(new_dicho[type.title()])
    #     # new_pure_tone = PureTone(start_time=datetime.utcnow())
    #     # new_pure_tone.create(property, result)
    #     new_exam = Exam(user=current_user['id'], type=EXAM_TYPE['PURE_TONE'], pure_tone=new_dicho)
    #     new_exam.save()
    #
    #     if passed_exam_before:
    #         pure_tone = passed_exam_before.pure_tone
    #         pure_tone[property] = result
    #         passed_exam_before.save()
    #     else:
    #         new_obj.create(exam_number, result)
    #         new_dicho.create(type.title(),new_obj)
    #         print(new_dicho[type.title()])
    #         # new_pure_tone = PureTone(start_time=datetime.utcnow())
    #         # new_pure_tone.create(property, result)
    #         new_exam = Exam(user=current_user['id'], type=EXAM_TYPE['PURE_TONE'], pure_tone=new_dicho)
    #         new_exam.save()
    #
    # except:
    #     pass

    return 'ok'