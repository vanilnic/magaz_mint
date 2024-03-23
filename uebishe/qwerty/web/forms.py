from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from web.models import *




class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users

class Balancee(ModelForm):
    class Meta:
        model = Balance
        fields = ['money']

class BasketA(ModelForm):
    class Meta:
        model = Basket
        fields = ['tea_id']