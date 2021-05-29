from django import forms
from django.forms import ModelForm
from .models import basic_info
from django.forms import TextInput,EmailInput

class basicForm(ModelForm):
	class Meta:
		model = basic_info
		fields = ('name','mobile_number')

		widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter name'
                }),
            'mobile_number': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Enter Mobile number'
                })
        }