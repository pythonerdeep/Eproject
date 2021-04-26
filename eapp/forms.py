from django import forms
from .models import Name,Id,Company,Information,Venue,Domain

class NameForm(forms.ModelForm):
    class Meta:
        model=Name
        fields = '__all__'

class IdForm(forms.ModelForm):
    class Meta:
        model=Id
        fields='__all__'

class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields = '__all__'

class InformationForm(forms.ModelForm):
    class Meta:
        model=Information
        fields='__all__'


class VenueForm(forms.ModelForm):
    class Meta:
        model=Venue
        fields='__all__'

class DomainForm(forms.ModelForm):
    class Meta:
        model=Domain
        fields='__all__'

class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(
        widget=forms.PasswordInput()

    )
