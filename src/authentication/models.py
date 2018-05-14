from werkzeug.security import generate_password_hash, check_password_hash
from src.user.models import User
from uuid import uuid4
import os
from datetime import datetime
from mongoengine import errors as MongoEngineException


class AuthenticationManager():
    # @staticmethod
    #     def authenticate_user(phonenumber, password):
    #         user = User.get(phonenumber)
    #         password_hash = user.password
    #         if check_password_hash(password_hash, password):
    #             if phonenumber == user.email and user.email_status == USER_INFO_STATUS['PENDING']:
    #                 raise EmailNotVerified(user.username)
    #             return user
    #         else:
    #             return False

    @staticmethod
    def register_user(phonenumber, email,password, fname, lname, sex, age, address, melli_code,
                      role='USER'
                      ):
        # TODO generate random pass and mail to user
        password = password
        password_hash = generate_password_hash(password)
        registration_time = datetime.utcnow()
        user = User(phonenumber=phonenumber,
                    password=password_hash, email=email, fname=fname, lname=lname, sex=sex, age=age,
                    address=address,
                    melli_code=melli_code, role=role, datetime=registration_time
                    )

        return user.save()

    @staticmethod
    def check_auth(phonenumber, password):

        is_user = User.objects.get(phonenumber=phonenumber)

        hash_pass = is_user.password
        if check_password_hash(hash_pass, password):
            return True, is_user
        else:
            return False, False
