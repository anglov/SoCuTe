from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect

from socute_app.forms import TextForm
from socute_app.models import *

def index(request):
    if request.method == 'POST': # Jeśli zapytanie jest post to
        # próbujemy przetworzyć dane z od użytkownika
        form = TextForm(request.POST) # Tworzymy formularz
        if form.is_valid(): # Jeśli jest poprawny
            text = TextModel()
            text.text = request.POST['text']
            text.full_clean()
            text.save()
    elif request.method == 'GET':
        form = TextForm() # Zapytanie jest GET więc tworzymy formularz
    else:
        return HttpResponse(status=403)
    # Tutaj możemy dość jeśli:
    # * Zapytanie jest GET (wtedy tworzymy nowy formularz)
    # * Zapytanie jest POST i formularz jest **niepoprawny**,
    #   wtedy pojawia się formularz z zaznaczonymi blędami
    return render(request, 'socute_app/index.html', {'form': form})
