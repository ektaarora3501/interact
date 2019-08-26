from django.shortcuts import render,redirect
from meetup.models import RegisMentor
from meetup.forms import RegisMentorForm
# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

def index(request):
    return render(request,'home.html')

def RgMentor(request):
    if request.method=='POST':
       form =RegisMentorForm(request.POST)
       print("post")

       if form.is_valid():
           user=form.cleaned_data['first_name']
           print(user)
           us=RegisMentor()
           #url=confirm/user
           print("form valid")
           us.first_name=form.cleaned_data['first_name']
           us.last_name=form.cleaned_data['last_name']
           us.email=form.cleaned_data['email']
           us.field=form.cleaned_data['choice']
           us.grad_year=form.cleaned_data['grad_year']
           us.Batch_id=form.cleaned_data['Batch_id']
           us.save()
           print("field_value=",us.field)

           return HttpResponseRedirect(reverse('confirm_regis',args=(user,)))

    else:
        #proposed_date=datetime.date.today()+datetime.timedelta(weeks=3)

        form=RegisMentorForm()

    context={
    'form':form,
    }


    return render(request,'MentorRegis.html',context)

def confirm(request,user):
    context={
    'user':user,
    }
    return render(request,'confirm_regis.html',context)
