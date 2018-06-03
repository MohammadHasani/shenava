from flask import request, jsonify
from . import exam_blureprint
from .models import Exam, PureTone, Dichotic, Single, Binary, Ternary
from flask_login import current_user, login_required
from src.misc.constracts import EXAM_TYPE, EXAM_STATUS
from mongoengine import errors as MongoEngineError
from datetime import datetime
from src.speech_noise.models import SpeechNoise


@exam_blureprint.route('/pure_tone', methods=['post'])
@login_required
def pure_tone():
    req_json = request.get_json()
    # try:
    direction = req_json['dir']
    frequency = req_json['frequency']
    result = req_json['result']
    property = str(direction).title() + '_' + str(frequency)
    passed_exam_before = Exam.passed_pure_before(current_user.id)
    if passed_exam_before:
        print('here')
        pure_tone = passed_exam_before.pure_tone
        pure_tone[property] = result
        passed_exam_before.save()

    else:
        print('2')
        new_pure_tone = PureTone(start_time=datetime.utcnow())
        new_pure_tone.create(property, result)
        new_exam = Exam(user=current_user['id'], type=EXAM_TYPE['PURE_TONE'], pure_tone=new_pure_tone)
        new_exam.save()

    return jsonify({'result': True, 'code': 200})

    # except MongoEngineError.ValidationError as e:
    #     print(e)
    #     return jsonify({'result': False, 'error': str(e)})
    # except Exception as e:
    #     print(e)
    #     return jsonify({'result': False, 'error': str(e)})


@exam_blureprint.route('/pure_tone/report', methods=['get'])
@login_required
def pure_tone_report():
    try:
        exam = Exam.get_puretone_by_user_id(current_user.id)
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
    # try:
    dicho_type = req_json['type'].title()
    results = req_json['result']
    new_dicho = Dichotic()
    new_obj = eval(dicho_type)()

    # passed_exam_before = Exam.passed_dichotic_before(current_user.id)
    #
    # if passed_exam_before:
    passed_dichotic_before = Exam.passed_dichotic_before(current_user.id)
    passed_dicho_type_before = Exam.passed_dicho_type_before(current_user.id, dicho_type)
    # prev_values = getattr(passed_dichotic_before.dichotic, dicho_type)
    if passed_dichotic_before:
        if passed_dicho_type_before:
            for exam_number, result in enumerate(results):
                exam_number = 'd' + str(exam_number + 1)
                pull_all = 'pull__dichotic__' + dicho_type + '__' + exam_number

                prev_values = getattr(passed_dichotic_before.dichotic, dicho_type)
                prev_values = getattr(prev_values, exam_number)[0:]

                for prev_value in prev_values:
                    pull_all_pair = {pull_all: prev_value}
                    passed_dichotic_before.update(**pull_all_pair)

                key_name = 'add_to_set__dichotic__' + dicho_type + '__' + exam_number
                key_value = {key_name: result}
                passed_dichotic_before.update(**key_value)
                # {'add_to_set__dichotic__Single__d1': [5, 5]}
                passed_dichotic_before.update(add_to_set__dichotic__Single__d1=[5, 5])
                passed_dichotic_before.save()
            return jsonify({'result': passed_dichotic_before, 'code': 200})
        else:
            print('h2222ere')
            for exam_number, result in enumerate(results):
                exam_number = 'd' + str(exam_number + 1)

                key_name = 'add_to_set__dichotic__' + dicho_type + '__' + exam_number
                key_value = {key_name: result}
                passed_dichotic_before.update(**key_value)
                passed_dichotic_before.save()
            # passed_dichotic_before.dichotic[dicho_type]={}
            # for exam_number, result in enumerate(results):
            #     exam_number = 'd' + str(exam_number + 1)
            #     passed_dichotic_before.dichotic[dicho_type][exam_number]: result
            #
            # passed_dichotic_before.save()
            return jsonify({'result': passed_dichotic_before, 'code': 200})
    else:
        print('here')
        for exam_number, result in enumerate(results):
            exam_number = 'd' + str(exam_number + 1)
            new_obj.create(exam_number, result)
        for attr, value in new_obj.__dict__.items():
            new_dicho.create(dicho_type, new_obj)

        new_exam = Exam(user=current_user['id'], type=EXAM_TYPE['DICHOTIC'], dichotic=new_dicho)
        new_exam.save()
        return jsonify({'result': new_exam, 'code': 200})
        # except Exception as e:
        #     print(e)
        #     return jsonify({'result': 'error', 'code': 500})


@exam_blureprint.route('/dichotic/report', methods=['get'])
@login_required
def dichotic_report():
    try:
        exam = Exam.get_dichotic_by_user_id(current_user.id)
        dichotic_report = exam.pure_tone_report()
        return jsonify({'result': dichotic, 'code': 200})
    except MongoEngineError.ValidationError as e:
        print(e)
        return jsonify({'result': False, 'error': str(e)})
    except MongoEngineError.DoesNotExist as e:
        print(e)
        return jsonify({'result': False, 'error': 'ExamDoesNotExist'})
    except Exception as e:
        print(e)
        return jsonify({'result': False, 'error': str(e)})


@exam_blureprint.route('/dichotic/single', methods=['get'])
@login_required
def get_single_dichotic():
    try:
        exam = Exam.objects.get(user=current_user.id)
        return jsonify({'result': exam.dichotic.Single, 'code': 200})
    except Exception as e:
        return jsonify({'result': False, 'code': 409})


@exam_blureprint.route('/speech_noise', methods=['post'])
@login_required
def speech_noise():
    req_json = request.get_json()
    # try:
    right_silence_result = req_json['result'][0:24]
    left_silence_result = req_json['result'][25:49]
    right_noise_result = req_json['result'][50:74]
    left_noise_result = req_json['result'][75:99]
    results = {'right_silence_result': right_silence_result, 'left_silence_result': left_silence_result,
               'right_noise_result': right_noise_result, 'left_noise_result': left_noise_result}
    print('here')

    passed_speech_noise_before = Exam.passed_speech_noise_before(current_user.id)
    if passed_speech_noise_before:
        speech_noise = passed_speech_noise_before.speech_noise
        speech_noise['right_silence'] = right_silence_result
        speech_noise['left_silence'] = left_silence_result
        speech_noise['right_noise'] = right_noise_result
        speech_noise['left_noise'] = left_noise_result
        passed_speech_noise_before.save()
    else:

        new_speech_noise = SpeechNoise(start_time=datetime.utcnow())
        for exam, result in results.items():
            new_speech_noise.create(exam, result)
        print(new_speech_noise['right_silence'])
        new_exam = Exam(user=current_user['id'], type=EXAM_TYPE['SPEECH_NOISE'], speech_noise=new_speech_noise)
        new_exam.save()

    return jsonify({'result': True, 'code': 200})

    # except MongoEngineError.ValidationError as e:
    #     print(e)
    #     return jsonify({'result': False, 'error': str(e)})
    # except Exception as e:
    #     print(e)
    #     return jsonify({'result': False, 'error': str(e)})


@exam_blureprint.route('/test', methods=['get'])
@login_required
def test():
    return 'one'
