from django import forms
from .models import Contacto
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3
from django.forms import ModelForm
from django.contrib.auth.models import User



class ContactoForm(ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Contacto
        fields = "__all__"


