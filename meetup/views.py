from django.shortcuts import render,redirect
from meetup.models import Register_user
from meetup.forms import RegisterForm,LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime
import bcrypt

def index(request):
    return render(request,'home.html')

def Register(request):
    if request.method=='POST':
       form =RegisterForm(request.POST)
       print("post")

       if form.is_valid():
           user=form.cleaned_data['first_name']
           print(user)
           us=Register_user()
           #url=confirm/user
           print("form valid")
           us.first_name=form.cleaned_data['first_name']
           name=form.cleaned_data['first_name']
           us.last_name=form.cleaned_data['last_name']
           us.email=form.cleaned_data['email']
           us.branch=form.cleaned_data['choice']
           us.curr_year=form.cleaned_data['curr_year']
           us.roll_no=form.cleaned_data['adm_no']
           user=form.cleaned_data['password']
           user=user.encode('utf-8')
           us.password=bcrypt.hashpw(user,bcrypt.gensalt())
           print(us.password)
           us.save()
           print("branch,curr_year",us.branch,us.curr_year)

           return HttpResponseRedirect(reverse('confirm_regis',args=(name,)))

    else:
        #proposed_date=datetime.date.today()+datetime.timedelta(weeks=3)

        form=RegisterForm()

    context={
    'form':form,
    }


    return render(request,'Register.html',context)

def confirm(request,user):
    context={
    'user':user,
    }
    return render(request,'confirm_regis.html',context)

def login(request):
    if request.method=='POST':
       form =LoginForm(request.POST)
       print("post")

       if form.is_valid():
           print("form valid")
           user=form.cleaned_data['adm_no']
           request.session['name']=user
           print("sesssion set!")
           return HttpResponseRedirect(reverse('user-dashboard',args=(user,)))

    else:
        #proposed_date=datetime.date.today()+datetime.timedelta(weeks=3)

        form=LoginForm()

    context={
    'form':form,
    }


    return render(request,'login.html',context)


def dashboard(request,user):
    if request.session.get('name'):
        return render(request,'dashboard.html',{'user':user,})
    else:
        return login(request)

def logout(request):
    try:
          del request.session['name']
          print("user deleted")
          print(request.session.get('name'))
    except :
          pass
    return  login(request)
