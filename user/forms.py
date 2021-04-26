from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ['name','password','email','mobile']
    name = forms.CharField(max_length=100,
                           label='',
                           widget=forms.TextInput(
                               attrs={
                                   'placeholder':'Enter Name',
                                   'class':'form-control',

                               }
                           )
                           )

    password = forms.CharField(max_length=100,
                           label='',
                           widget=forms.TextInput(
                               attrs={
                                   'placeholder': 'Enter Password',
                                   'class': 'form-control',

                               }
                           )
                           )
    email = forms.CharField(max_length=100,
                               label='',
                               widget=forms.TextInput(
                                   attrs={
                                       'placeholder': 'Enter Email',
                                       'class': 'form-control',

                                   }
                               )
                               )

    mobile = forms.CharField(max_length=100,
                            label='',
                            widget=forms.TextInput(
                                attrs={
                                    'placeholder': 'Enter Mobile',
                                    'class': 'form-control',

                                }
                            )
                            )
class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(
        widget=forms.PasswordInput()
    )
