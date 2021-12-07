from django import forms
from .models import NewUser


# class UserRegForm(forms.ModelForm):
#     class Meta:
#         model = NewUser
#         fields = ['full_name', 'email', 'password1', 'password2']
#         widgets = {
#             'name':forms.TextInput(attrs={'class':'form-control'}),
#             'email':forms.EmailInput(attrs={'class':'form-control'}),
#             'password1':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
#             'password2':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
#         }

class RegisterForm(forms.Form):
    full_name = forms.CharField(label='Full Name', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your Name'}))

    user_name = forms.CharField(label='Username', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your Username'}))

    email = forms.EmailField(label='Email', required=False,
                             widget=forms.EmailInput(attrs={'placeholder': 'example@email.com'}))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Password'}))

    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))

    image = forms.ImageField(label='image', required=False)


class LoginForm(forms.Form):
    user_name = forms.CharField(label='Username', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your Username'}))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
