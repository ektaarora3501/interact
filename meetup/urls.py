from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="home"),
    path('mentor/Register',views.RgMentor,name="register_mentor"),
    path('confirm/<user>',views.confirm,name='confirm_regis'),
]
