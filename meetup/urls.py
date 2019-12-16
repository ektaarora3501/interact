from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns=[
    path('',views.index,name="home"),
    path('Register',views.Register,name="register"),
    path('login',views.login,name='login_user'),
    path('user_dashboard/<user>',views.dashboard,name='user-dashboard'),
    path('logout/<user>',views.logout,name='logout'),
    path('profile/<user>',views.profile,name='user-profile'),
    path('filter/technical/<skill>',views.get_skill_tech,name='skill_filter_tech'),
    path('filter/member/<group>',views.get_member,name='member_filter'),
    path('study_stuff',views.material,name="studyy_stuff"),
    path('send_mail',views.contact,name="contact-us"),
    path('admin/set_notice',views.set_notice,name="notice"),
    path('admin/set_event',views.set_event,name="event"),
    path('admin/show_event',views.show_event,name='show_event'),
    path('admin/delete_event/<id>',views.delete_event,name='delete_event')
]
