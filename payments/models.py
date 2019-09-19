from django.db import models
from members.models import Member
from groups.models import Group
from rest_framework.reverse import reverse

# Create your models here.
class Payment(models.Model):

	payer = models.ForeignKey(Member,on_delete=models.CASCADE)
	group = models.ForeignKey(Group,on_delete=models.CASCADE)
	datetime = models.DateTimeField(auto_now_add=True)
	amount = models.IntegerField(default=0,editable=False)

	class Meta:
		verbose_name = "Payment"
		verbose_name_plural = "Payments"

	def __str__(self):
		return "%s's payment in %s group on %s" %(self.payer,self.group,self.datetime)

	def get_absolute_url(self):
		return reverse("payment-detail",kwargs={"group_pk":self.group.pk,"member_pk":self.payer.pk})

    