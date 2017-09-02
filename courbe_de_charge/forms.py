from django import forms
from .models import UsersLP


class LPForm(forms.ModelForm) :
    class Meta :
        model = UsersLP
        fields = ('location', 'power', 'bill',)
