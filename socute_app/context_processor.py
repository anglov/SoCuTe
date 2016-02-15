from socute_app.tools import *

def set_login_info(request):
    auth = user_is_auth(request)
    username = user_name(request) if auth else ""
    return {'auth': auth, 'username': username}