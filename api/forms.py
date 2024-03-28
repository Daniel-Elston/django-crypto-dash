# forms.py
from __future__ import annotations

from django import forms


class FilterForm(forms.Form):
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
    columns = forms.MultipleChoiceField(
        choices=[
            ('timestamp', 'Timestamp'),
            ('close', 'Close Price'),
            # Add more fields as needed
        ],
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
