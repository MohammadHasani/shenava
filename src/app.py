from src import login_manager
from src.user.models import User
from itsdangerous import Serializer
import base64
from mongoengine import errors as MongoEngineExceptions
from src.authentication.models import AuthenticationManager


@login_manager.request_loader
def load_user_from_request(request):
    # next, try to login using Basic Auth
    api_key = request.headers.get('Authorization')
    if api_key:
        phonenumber = None
        password = None
        api_key = api_key.replace('Basic ', '', 1)
        try:
            api_key = base64.b64decode(api_key).decode('utf-8')
            phonenumber = api_key.split(':')[0]
            password = api_key.split(':')[1]

            # if user.check_password(password):
            result, user = AuthenticationManager.check_auth(phonenumber, password)
            if user and result:
                return user
        except TypeError:
            print('type error')
        except Exception as e:
            print(e)
            return None

    # finally, return None if both methods did not login the user
    return None


