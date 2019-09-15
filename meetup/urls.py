from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="home"),
    path('Register',views.Register,name="register"),
    path('confirm/<user>',views.confirm,name='confirm_regis'),
]
