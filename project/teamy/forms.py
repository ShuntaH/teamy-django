from django import forms
from django.contrib.auth import password_validation, get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Department, Club


class SearchForm(forms.Form):
    department = forms.ModelChoiceField(
        queryset=Department.objects, label='Department ', required=False
    )
    club = forms.ModelChoiceField(
        queryset=Club.objects, label='Club', required=False
    )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        User = get_user_model()
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'department', 'club',]
