from django import forms
from dashboard.models import *


class Categoryform(forms.ModelForm):
	class Meta :
		model=Category 
		fields=['name']

