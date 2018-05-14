import os

CSRF_ENABLED = True
SECRET_KEY = '324732uy4hj23j4h2i3yudgisdl@#$@#$@#$236y2u3jkey2u3e927gduh23uhdjgvcsgyuycsy34v23$@#$@#$@#$@#$#2jh4g28374iu23jh42j3k42krjjhdsf'
WTF_CSRF_SECRET_KEY = 'ghsadga67d832gy24h3b42v3n42ashgchvastdgavtg vahhbdjw'


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = BASE_DIR + '/src/static/user_data/'

IMAGE_ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
VIDEO_ALLOWED_EXTENSIONS = set(['mp4', 'avi'])
AUDIO_ALLOWED_EXTENSIONS = set(['mp3', 'ogg'])
DOCUMENT_ALLOWED_EXTENSIONS = set(['pdf'])
ALLOWED_EXTENSIONS = set(IMAGE_ALLOWED_EXTENSIONS | VIDEO_ALLOWED_EXTENSIONS | AUDIO_ALLOWED_EXTENSIONS | DOCUMENT_ALLOWED_EXTENSIONS)


MONGODB_SETTINGS = {
    'db': 'shenava',
    'host': 'localhost',
    'port': 27017
}

BABEL_DEFAULT_LOCALE = 'en'

DEBUG = True
SITE_BASE_URL = 'localhost'

# MAIL_SERVER = 'smtp.googlemail.com'
# MAIL_PORT = 465
# MAIL_USE_TLS = False
# MAIL_USE_SSL = True
# MAIL_USERNAME = 'pooya.kn.73@gmail.com'
# MAIL_PASSWORD = 'weqproqzsexpwjpq'
# MAIL_DEFAULT_SENDER = 'pooya.kn.73@gmail.com'

BP_TERMINAL_ID = 217
BP_USERNAME = 'user217'
BP_PASSWORD = '83642285'
# BP_CALLBACK_URL = SITE_BASE_URL + '/payment/verify-payment'