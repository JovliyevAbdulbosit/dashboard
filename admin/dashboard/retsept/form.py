from django import forms
from dashboard.models import *


class Retseptform(forms.ModelForm):
	class Meta :
		model=Retsept 
		fields='__all__'

