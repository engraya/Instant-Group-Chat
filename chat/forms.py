from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder" : "Enter your Email here"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder" : "Enter your Username here"}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder" : "Enter your Password here", "type" : "passworrd"}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder" : "Confirm your passowrd here"}))
    
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["username"].widget.attrs.update({"class": "form-control"})
    #     self.fields["email"].widget.attrs.update({"class": "form-control"})
    #     self.fields["password1"].widget.attrs.update({"class": "form-control"})
    #     self.fields["password2"].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        def save(self, commit=True):
            user = super(UserRegistrationForm, self,).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user

class ProfileUpdateForm(ModelForm):
    model = Profile
    fields = '___all__'


