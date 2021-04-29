from django.db import models
from django.urls import reverse

class Costumer(models.Model):
	id = models.AutoField('ID', primary_key=True, blank=False)
	firstName = models.CharField('First name', max_length=50)
	lastName = models.CharField('Last name', max_length=50)
	age = models.IntegerField('Age')
	address = models.CharField('Address', max_length=200)
	def __str__(self):
		return self.firstName

	def get_absolute_url(self):
		return reverse("costumer-detail", kwargs={"id": self.id}) #f"/costumer/{self.id}/"
