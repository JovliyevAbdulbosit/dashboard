from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from dashboard import default_prep,reting
# Create your models here.
class Category(models.Model):
	name=models.CharField(max_length=256)
	slug=models.SlugField(unique=True , max_length=256 )
	def save(self,*args,**kwargs):
		if not self.slug :
			self.slug=slugify(self.name)
		super(Category ,self ).save(*args,**kwargs)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('detial', args=[str(self.id)])
	
class Ingrednts(models.Model):
	product=models.CharField(max_length=256)
	porsiya=models.CharField(max_length=256)
	def __str__(self):
		return self.product
class Retsept(models.Model):
	name=models.CharField(max_length=256)
	prep=models.JSONField(default=default_prep())		
	photo=models.ImageField(blank=True)
	ingrednts=models.ManyToManyField(Ingrednts )
	steps=models.TextField()
	time=models.DateTimeField(auto_now_add=True)
	rete=models.SmallIntegerField(choices=reting())
	ctg=models.ForeignKey(Category, on_delete=models.CASCADE)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('detial', args=[str(self.id)])
	


class User(models.Model):
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	email = models.EmailField(max_length=150)



