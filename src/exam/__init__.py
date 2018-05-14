from flask import Blueprint

exam_blureprint = Blueprint('exam',__name__,template_folder='templates')

from . import views