from django import forms 
from .models import Coffee
from django.contrib.auth.models import User 




class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ['beans', 'roast', 'syrup', 'powder', 'espresso', 'foam', 'milk', 'water', 'extra', 'name']


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