from flask import Blueprint

user_blureprint = Blueprint('user',__name__,template_folder='templates')

from . import views