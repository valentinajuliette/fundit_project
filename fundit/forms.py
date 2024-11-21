from django import forms
from django.contrib.auth.models import User
from .models import Subscription

class UserRegistrationForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'contraseña']

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['tipo_de_suscripción', 'número_de_tarjeta_de_crédito', 'CVV', 'fecha_de_expiración']

