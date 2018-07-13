from django import forms

from user.models import User


class UserForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)


class UserDeleteForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.RadioSelect, initial=None)
