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
    roll_no=models.CharField(max_length=8,default=None,primary_key=True)
    password=models.CharField(max_length=200,default="")
    github=models.CharField(max_length=100,default="")
    summary=models.CharField(max_length=100,default="")
    img_link=models.CharField(max_length=100,default="http://127.0.0.1:8000/media/image.jpeg")
    skill1=models.CharField(max_length=100,default="0")
    skill2=models.CharField(max_length=100,default="0")
    skill3=models.CharField(max_length=100,default="0")
    skill4=models.CharField(max_length=100,default="0")

    ntech1=models.CharField(max_length=100,default="0")
    ntech2=models.CharField(max_length=100,default="0")
    ntech3=models.CharField(max_length=100,default="0")
    ntech4=models.CharField(max_length=100,default="0")


    def __str__(self):
        return f'{self.first_name},{self.email}'


class Event(models.Model):
    event=models.CharField(max_length=100)
    date=models.CharField(max_length=100,null=True)
    time=models.CharField(max_length=100,null=True)
    venue=models.CharField(max_length=100,null=True)

    def __str__(self):
        return f'{self.event},{self.date},{self.time},{self.venue}'

class Notice(models.Model):
    notice=models.CharField(max_length=200)

    def __str__(self):
        return f'{self.notice}``'
