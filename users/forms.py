import email
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from users.models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']


class UserUpdateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    # def __init__(self, *args, **kwargs):
    #    super(UserUpdateForm, self).__init__(*args, **kwargs)
    #    del self.fields['password1']
    #    del self.fields['password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']