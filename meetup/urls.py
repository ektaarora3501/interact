from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="home"),
    path('Register',views.Register,name="register"),
    path('confirm/<user>',views.confirm,name='confirm_regis'),
    path('login',views.login,name='login_user'),
    path('user_dashboard/<user>',views.dashboard,name='user-dashboard'),
    path('logout/<user>',views.logout,name='logout'),
    path('profile/<user>',views.profile,name='user-profile'),
    path('filter/technical/<skill>',views.get_skill_tech,name='skill_filter_tech'),
    path('filter/member/<group>',views.get_member,name='member_filter'),
    path('study_stuff',views.material,name="studyy_stuff"),
    path('send_mail',views.contact,name="contact-us"),
]
