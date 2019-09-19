from django.db import models
from members.models import Member
from rest_framework.reverse import reverse
import uuid
from random import choice

# Create your models here.

class Group(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	max_capacity = models.IntegerField(default=1)
	is_searchable = models.BooleanField("Public group",default=True)
	admin = models.ForeignKey(Member,on_delete=models.CASCADE,related_name='owner')
	members = models.ManyToManyField(Member)
	savings_amount = models.IntegerField(default=0)
	started = models.DateField(auto_now_add=True)
	collector = models.ForeignKey(Member,on_delete=models.CASCADE,related_name='collector',null=True)
	uuid = models.UUIDField(unique=True,default=uuid.uuid4,editable=False)


	class Meta:
		verbose_name = 'Group'
		verbose_name_plural = 'Groups'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('group-detail',kwargs={pk:self.pk})