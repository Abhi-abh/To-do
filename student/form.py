from django import forms
from .models import insert_details


class insert_form(forms.ModelForm):
    class Meta:
        model = insert_details
        fields = '__all__'