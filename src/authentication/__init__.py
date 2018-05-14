from flask import Blueprint

auth_blureprint = Blueprint('auth',__name__,template_folder='templates')

from . import views