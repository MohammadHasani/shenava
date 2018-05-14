from src import db
from src.misc.constracts import ROLES
from flask_login import UserMixin



class User(UserMixin, db.Document):
    phonenumber = db.StringField(max_length=13, required=True, unique=True)
    email = db.EmailField(max_length=128)
    password = db.StringField(min_length=8, max_length=128, required=True)
    fname = db.StringField(max_length=128)
    lname = db.StringField(max_length=256)
    sex = db.StringField()
    age = db.StringField(min_length=1, max_length=2)
    address = db.StringField()
    melli_code = db.StringField(min_length=10, max_length=10)
    role = db.StringField(default=ROLES['USER'], choices=ROLES)
    datetime = db.DateTimeField()


    # phonenumber_status = db.StringField(default=USER_INFO_STATUS['PENDING'])
    # email_status = db.StringField(default=USER_INFO_STATUS['NOT_FILLED'])
    # melli_code_status = db.StringField(default=USER_INFO_STATUS['NOT_FILLED'])
    # status = db.StringField(default=USER_STATUS['ACTIVE'], choices=USER_STATUS)
    # authorization_errors = db.ListField(db.EmbeddedDocumentField(AuthorizationError))
    # email_notifications = db.ListField(db.StringField(choices=EMAIL_NOTIFICATION))
    # email_verification_code = db.StringField()

    meta = {
        'indexes': ['phonenumber']
    }

    def register(self):
        pass
