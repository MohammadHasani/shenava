from flask import request, jsonify
from . import exam_blureprint
from .models import Exam, PureTone, Dichotic, Single, Binary, Ternary
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

    try:
        dicho_type = req_json['type'].title()
        results = req_json['result']
        new_dicho = Dichotic()

        new_obj = eval(dicho_type)()

        passed_exam_before = Exam.passed_exam_before(current_user.id)

        if passed_exam_before:
            for exam_number, result in enumerate(results):
                exam_number = 'd' + str(exam_number + 1)
                pull_all = 'pull__dichotic__Single__' + exam_number
                prev_value = getattr(passed_exam_before.dichotic.Single, exam_number)[0]
                pull_all_pair = {pull_all: prev_value}

                key_name = 'add_to_set__dichotic__Single__' + exam_number
                key_value = {key_name: result}
                passed_exam_before.update(**pull_all_pair)
                passed_exam_before.update(**key_value)
            passed_exam_before.save()
            return jsonify({'result': passed_exam_before, 'code': 200})


        else:
            for exam_number, result in enumerate(results):
                exam_number = 'd' + str(exam_number + 1)
                new_obj.create(exam_number, result)
            for attr, value in new_obj.__dict__.items():
                new_dicho.create(dicho_type, new_obj)

            new_exam = Exam(user=current_user['id'], type=EXAM_TYPE['DICHOTIC'], dichotic=new_dicho)
            new_exam.save()
            return jsonify({'result': new_exam, 'code': 200})


    except Exception as e:
        print(e)

