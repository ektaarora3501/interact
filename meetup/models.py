from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
import datetime

class Register_user(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    curr_year=models.CharField(max_length=100)
    roll_no=models.CharField(max_length=8,default=None)
    password=models.CharField(max_length=200,default="")
    github=models.CharField(max_length=100,default=None)


    def __str__(self):
        return f'{self.first_name},{self.email}'


#class ExampleModel(models.Model):
#    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
