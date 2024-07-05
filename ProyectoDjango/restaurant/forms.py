from django import forms
from .models import Contacto, Producto
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3
from django.forms import ModelForm
from django.contrib.auth.models import User



class ContactoForm(ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Contacto
        fields = "__all__"





class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categorias', 'imagen', 'precio', 'disponibilidad']