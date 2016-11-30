from django import forms
from django.contrib.auth.models import User
from .models import Order

class Logi_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]


class Register_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
        ]


class Add_form(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'time',
        ]