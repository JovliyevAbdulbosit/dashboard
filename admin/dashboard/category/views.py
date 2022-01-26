from django.shortcuts import render
from django.views.generic.edit import UpdateView , DeleteView
from .form import Categoryform
from dashboard.models import Category
from django.urls import reverse_lazy
def categoryViews(requests):
	a=False
	ctg_form=Categoryform()
	if requests.POST:
		forms=Categoryform(requests.POST or None, requests.FILES or None )
		if forms.is_valid():
			forms.save()
			a=True

	return render(requests,'dashboard/category/forms.html', {'form':ctg_form , 'a':a})
def categoryallViews(requests):
	all=Category.objects.all()
	return render(requests,'dashboard/category/list.html', {'all':all})


class CategoryeditViews(UpdateView):
	model=Category
	fields=['name']
	template_name='dashboard/category/edit.html'

def detialViews(requests,pk):
	one=Category.objects.get(id=pk)
	return render(requests, 'dashboard/category/detial.html' , {'one':one})

class DeleteViews(DeleteView):
	model=Category
	template_name='dashboard/category/delete.html'
	success_url=reverse_lazy('list')	