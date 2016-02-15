from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect

from socute_app.forms import AnonTextForm, TextForm, AuthForm, RegisterForm, ViewTextForm
from socute_app.models import *
from socute_app.tools import *

import datetime

def add(request):
    if user_is_auth(request):
        username = user_name(request)
        user = UserModel.objects.get(username=username)
    else:
        user = None

    if request.method == 'POST':
        if user_is_auth(request):
            form = TextForm(request.POST)
            expire = datetime.date.today() + datetime.timedelta(days=30)
        else:
            form = AnonTextForm(request.POST)
            expire = datetime.date.today() + datetime.timedelta(days=7)
        if form.is_valid():
            text = TextModel()
            text.text = request.POST['text_hid']
            text.expire_time = expire
            text.header = request.POST['header']
            text.owner = user
            text.public = True if 'public' in request.POST else False
            text.full_clean()
            text.save()
            return render(request, 'socute_app/success.html', {'post': text})
    elif request.method == 'GET':
        if user_is_auth(request):
            form = TextForm()
        else:
            form = AnonTextForm()
    else:
        return HttpResponse(status=403)
    return render(request, 'socute_app/add.html', {'form': form})


def index(request):
    return render(request, 'socute_app/index.html')


def log_in(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    _login(request, user)
                    return HttpResponseRedirect('/index')
                else:
                    return HttpResponse('Your account is disabled', status=200)
            else:
                return HttpResponse('Wrong login or password', status=200)
    elif request.method == 'GET':
        form = AuthForm()
    else:
        return HttpResponse(status=403)
    return render(request, 'socute_app/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = UserModel()
            user.username = request.POST['username']
            plain_pass = request.POST['password']
            user.salt = generate_salt()
            user.password = calculate_password_hash(plain_pass, user.salt)
            user.is_active = True
            user.full_clean()
            user.save()
            return HttpResponseRedirect('/index')
    elif request.method == 'GET':
        form = RegisterForm()
    else:
        return HttpResponse(status=403)
    return render(request, 'socute_app/register.html', {'form': form})


def post(request):
    if request.method == 'GET':
        try:
            post_id = request.GET['post_id']
            post = TextModel.objects.get(pk=post_id)
        except TextModel.DoesNotExist:
            return HttpResponse('Wrong post id', status=404)
        if not post.public:
            if not user_is_auth(request):
                return HttpResponseRedirect('/login')
            username = user_name(request)
            user = UserModel.objects.get(username=username)
            if user != post.owner:
                return HttpResponseRedirect('/login')
        crypted = post.text
        post.text = ""
        form = ViewTextForm(instance=post, initial={'text_hid': crypted})
        return render(request, 'socute_app/post.html', {'form': form})
    else:
        return HttpResponse('Unavailable', status=403)

def log_out(request):
    _logout(request)
    return HttpResponseRedirect('/index')


def posts(request):
    if not user_is_auth(request):
        return HttpResponseRedirect('/login')
    username = user_name(request)
    user = UserModel.objects.get(username=username)
    posts = TextModel.objects.filter(owner_id=user.pk).order_by('header')
    return render(request, 'socute_app/posts.html', {'posts': posts})


def authenticate(username, password):
    try:
        user = UserModel.objects.get(username=username)
    except:
        return None
    if user and calculate_password_hash(password, user.salt) != user.password:
        return None
    return user


def _login(request, user):
    request.session['logged_in_user_name'] = user.username
    request.session.cycle_key()


def _logout(request):
    request.session.flush()