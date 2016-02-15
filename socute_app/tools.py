import os, hashlib, base64
from socute_app.models import UserModel

SALT_SIZE=16

def generate_salt():
    return base64.b64encode(os.urandom(SALT_SIZE)).decode('ascii')


def calculate_password_hash(password, salt):
    return hashlib.sha256((salt + '$' + password).encode('ascii')).hexdigest()


def user_is_auth(request):
    if 'logged_in_user_name' in request.session.keys() and \
            UserModel.objects.filter(username=request.session['logged_in_user_name']):
        return True
    else:
        return False


def user_name(request):
    return request.session['logged_in_user_name']