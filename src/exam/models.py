from src import db
from src.misc.constracts import EXAM_TYPE, EXAM_STATUS
from src.user.models import User


class PureTone(db.EmbeddedDocument):
    start_time = db.DateTimeField()
    Right_125 = db.BooleanField()
    Right_250 = db.BooleanField()
    Right_500 = db.BooleanField()
    Right_1000 = db.BooleanField()
    Right_2000 = db.BooleanField()
    Right_4000 = db.BooleanField()
    Right_8000 = db.BooleanField()
    Left_125 = db.BooleanField()
    Left_250 = db.BooleanField()
    Left_500 = db.BooleanField()
    Left_1000 = db.BooleanField()
    Left_2000 = db.BooleanField()
    Left_4000 = db.BooleanField()
    Left_8000 = db.BooleanField()

    def __repr__(self):
        return '[PureTone] id: {}, status: {}'.format(self.start_time, self.Left_125)

    def create(self, property, result):
        self.__setattr__(property, result)
        return self


class Single(db.EmbeddedDocument):
    start_time = db.DateTimeField()
    d1 = db.ListField()
    d2 = db.ListField()
    d3 = db.ListField()
    d4 = db.ListField()
    d5 = db.ListField()
    d6 = db.ListField()
    d7 = db.ListField()
    d8 = db.ListField()
    d9 = db.ListField()
    d10 = db.ListField()
    d11 = db.ListField()
    d12 = db.ListField()
    d13 = db.ListField()
    d14 = db.ListField()
    d15 = db.ListField()
    d16 = db.ListField()
    d17 = db.ListField()
    d18 = db.ListField()
    d19 = db.ListField()
    d20 = db.ListField()
    d21 = db.ListField()
    d22 = db.ListField()
    d23 = db.ListField()
    d24 = db.ListField()
    d25 = db.ListField()

    def create(self, property, result):
        self.__setattr__(property, [result])
        return self


class Binary(db.EmbeddedDocument):
    start_time = db.DateTimeField()
    d1 = db.ListField()
    d2 = db.ListField()
    d3 = db.ListField()
    d4 = db.ListField()
    d5 = db.ListField()
    d6 = db.ListField()
    d7 = db.ListField()
    d8 = db.ListField()
    d9 = db.ListField()
    d10 = db.ListField()
    d11 = db.ListField()
    d12 = db.ListField()
    d13 = db.ListField()
    d14 = db.ListField()
    d15 = db.ListField()
    d16 = db.ListField()
    d17 = db.ListField()
    d18 = db.ListField()
    d19 = db.ListField()
    d20 = db.ListField()
    d21 = db.ListField()
    d22 = db.ListField()
    d23 = db.ListField()
    d24 = db.ListField()
    d25 = db.ListField()

    def create(self, property, result):
        self.__setattr__(property, result)
        return self


class Ternary(db.EmbeddedDocument):
    start_time = db.DateTimeField()
    d1 = db.ListField()
    d2 = db.ListField()
    d3 = db.ListField()
    d4 = db.ListField()
    d5 = db.ListField()
    d6 = db.ListField()
    d7 = db.ListField()
    d8 = db.ListField()
    d9 = db.ListField()
    d10 = db.ListField()
    d11 = db.ListField()
    d12 = db.ListField()
    d13 = db.ListField()
    d14 = db.ListField()
    d15 = db.ListField()
    d16 = db.ListField()
    d17 = db.ListField()
    d18 = db.ListField()
    d19 = db.ListField()
    d20 = db.ListField()
    d21 = db.ListField()
    d22 = db.ListField()
    d23 = db.ListField()
    d24 = db.ListField()
    d25 = db.ListField()

    def create(self, property, result):
        self.__setattr__(property, result)
        return self


class Dichotic(db.Document):
    Single = db.EmbeddedDocumentField('Single')
    Binary = db.EmbeddedDocumentField('Binary')
    Ternary = db.EmbeddedDocumentField('Ternary')

    def create(self, property, result):
        self.__setattr__(property, result)
        return self

    def create_test(self, type, exam_number, result):
        new_obj = eval(type.title())()
        setattr(new_obj, exam_number, result)
        setattr(self, type)

    @staticmethod
    def overwrite(dicho_type_exam,result):
        for i in dicho_type_exam:
            if i == 'start_time':
                continue
            elif len(dicho_type_exam[i]) != 0:
                dicho_type_exam[i] = result

        return dicho_type_exam



class Exam(db.Document):
    user = db.ReferenceField('User')
    type = db.StringField(choices=EXAM_TYPE)
    pure_tone = db.EmbeddedDocumentField('PureTone')
    dichotic = db.EmbeddedDocumentField('Dichotic')

    def __repr__(self):
        return '[Exam] user :{} type:{} pure_tone:{}'.format(self.user, self.type, self.pure_tone)

    @classmethod
    def passed_exam_before(cls, userid):
        return cls.objects.get(user=userid) if cls.objects(user=userid) else False

    @classmethod
    def get_by_user_id(cls, userid):
        return cls.objects.get(user=userid)

    def pure_tone_report(self):
        result = {}
        result['Right_125'] = self.pure_tone.Right_125
        result['Right_250'] = self.pure_tone.Right_250
        result['Right_500'] = self.pure_tone.Right_500
        result['Right_1000'] = self.pure_tone.Right_1000
        result['Right_2000'] = self.pure_tone.Right_2000
        result['Right_4000'] = self.pure_tone.Right_4000
        result['Right_8000'] = self.pure_tone.Right_8000
        result['Left_125'] = self.pure_tone.Left_125
        result['Left_250'] = self.pure_tone.Left_250
        result['Left_500'] = self.pure_tone.Left_500
        result['Left_1000'] = self.pure_tone.Left_1000
        result['Left_2000'] = self.pure_tone.Left_2000
        result['Left_4000'] = self.pure_tone.Left_4000
        result['Left_8000'] = self.pure_tone.Left_8000

        count = 0
        for i in result:
            if i == False:
                count += 1
        if count > 3:
            need_to_clinic = True
        else:
            need_to_clinic = False

        return {'result': result, 'need': need_to_clinic}
