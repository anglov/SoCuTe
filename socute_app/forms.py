from django import forms
from socute_app.models import UserModel
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Textarea, TextInput, HiddenInput
from socute_app.models import TextModel


def validate_unique(value):
    if UserModel.objects.filter(username=value):
        raise ValidationError('%s już istnieje' % value)

class AuthForm(forms.Form):
    username = forms.CharField(label='Login', max_length=100)
    password = forms.CharField(label='Password',min_length=5, max_length=100, widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username = forms.CharField(label='Login', max_length=100, validators=[validate_unique])
    password = forms.CharField(label='Password',min_length=5, max_length=100, widget=forms.PasswordInput())


class TextForm(ModelForm):
    text_hid = forms.CharField(widget=HiddenInput)

    class Meta:
        model = TextModel
        fields = ('header', 'text', 'public', 'write')
        widgets = {
            'header': TextInput(),
            'text': Textarea(attrs={'cols': 150, 'rows': 60}),
        }