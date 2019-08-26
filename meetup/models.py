from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
import datetime

class RegisMentor(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    field=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    date=models.DateField(_("Date"),default=datetime.date.today)
    grad_year=models.CharField("Graduation year",max_length=4,default=None)
    Batch_id=models.CharField("Batch Id",max_length=8,default=None)

    def __str__(self):
        return f'{self.first_name},{self.email},{self.field}'
