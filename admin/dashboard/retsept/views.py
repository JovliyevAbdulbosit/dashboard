from django.shortcuts import render
from django.views.generic.edit import UpdateView , DeleteView
from .form import Retseptform
from dashboard.models import Retsept
from django.urls import reverse_lazy
def retseptViews(requests):
	a=False
	ctg_form=Retseptform()
	if requests.POST:
		forms=Retseptform(requests.POST or None, requests.FILES or None )
		if forms.is_valid():
			
			forms.save()
			a=True

	return render(requests,'dashboard/retsept/form.html', {'form':ctg_form , 'a':a})
def retseptallViews(requests):
	all=Retsept.objects.all()
	
	return render(requests,'dashboard/retsept/list.html', {'all':all})


class RetsepteditViews(UpdateView):
	model=Retsept
	fields=['name','prep','photo','ingrednts','steps','rete','ctg']
	template_name='dashboard/retsept/edit.html'

def retseptdetialViews(requests,pk):
	one=Retsept.objects.get(id=pk)
	return render(requests, 'dashboard/retsept/detial.html' , {'one':one})

class RetseptDeleteViews(DeleteView):
	model=Retsept
	template_name='dashboard/retsept/delete.html'
	success_url=reverse_lazy('ret_list')	