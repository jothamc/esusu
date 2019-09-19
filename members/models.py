from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class Member(AbstractUser):
	uuid = models.UUIDField(default=uuid.uuid4,editable=False)

	class Meta:
		verbose_name = "Member"
		verbose_name_plural = "Members"
		ordering = ['date_joined']

	def __str__(self):
		return "%s %s" %(self.last_name, self.first_name)
    