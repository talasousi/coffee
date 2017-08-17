from django import forms 
from .models import *
from django.contrib.auth.models import User 



class BeanForm(forms.ModelForm):
    class Meta:
        model = Bean
        fields = ['name', 'price']

class SyrupForm(forms.ModelForm):
    class Meta:
        model = Syrup
        fields = ['name', 'price']

class PowderForm(forms.ModelForm):
    class Meta:
        model = Powder
        fields = ['name', 'price']

class RoastForm(forms.ModelForm):
    class Meta:
        model = Roast
        fields = ['name', 'price']    

class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ['beans', 'roast', 'syrup', 'powder', 'shot', 'foam', 'milk', 'water', 'extra', 'name', 'price']


class UserSignUp(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = {
        'password' : forms.PasswordInput(),
        }
    
class UserLogin(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())