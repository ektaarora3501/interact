from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="home"),
    path('Register',views.Register,name="register"),
    path('confirm/<user>',views.confirm,name='confirm_regis'),
    path('login',views.login,name='login_user'),
    path('user_dashboard/<user>',views.dashboard,name='user-dashboard'),
]
