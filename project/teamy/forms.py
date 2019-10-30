from django import forms
from .models import Department, Club


class SearchForm(forms.Form):
    department = forms.ModelChoiceField(
        queryset=Department.objects, label='Department ', required=False
    )

    club = forms.ModelChoiceField(
        queryset=Club.objects, label='Club ', required=False
    )
