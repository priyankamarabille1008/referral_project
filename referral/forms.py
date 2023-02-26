from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    referral_code=forms.CharField(max_length=10, required=False)

    class Meta:
        model = User
        field = ['username','email','password1','password2','referral_code']