from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField



'''class CustomUserCreationForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1','password2']'''
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        label="Nombre",
        help_text="Ingresa tu nombre",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre'
        })
    )
    last_name = forms.CharField(
        required=True,
        label="Apellido",
        help_text="Ingresa tu apellido",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Apellido'
        })
    )
    email = forms.EmailField(
        required=True,
        label="Correo Electrónico",
        help_text="Ingresa tu correo electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo Electrónico'
        })
    )
    
    password1 = forms.CharField(
        label="Contraseña",
        help_text="Debe contener al menos 8 caracteres.",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
    )
    
    password2 = forms.CharField(
        label="Confirmar Contraseña",
        help_text="Reingresa la misma contraseña para verificar.",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar Contraseña'
        })
    )

    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de Usuario',
        }
        help_texts = {
            'username': 'Requerido. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.',
        }
        error_messages = {
            'username': {
                'required': "El nombre de usuario es obligatorio.",
                'invalid': "Este nombre de usuario es inválido.",
            },
            'password1': {
                'required': "La contraseña es obligatoria.",
                'password_too_short': "La contraseña es muy corta.",
            },
            'password2': {
                'required': "La confirmación de la contraseña es obligatoria.",
                'password_mismatch': "Las contraseñas no coinciden.",
            },
        }