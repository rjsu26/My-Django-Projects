from django import forms
from django.contrib.auth.models import User
from basicApp.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(required=True,widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ("username","email","password")

class UserProfileInfoForm(forms.ModelForm):    
    # Editing not needed. So not needed to write again.
    # portfolio = forms.URLField(, required=False)
    # picture = forms.ImageField(required=False)
    class Meta: #connects this form to its model
        model = UserProfileInfo
        fields = ("portfolio_site","profile_pic")

