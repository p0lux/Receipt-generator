from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()


class RegisterForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.PasswordInput()
    sudo = forms.BooleanField()
