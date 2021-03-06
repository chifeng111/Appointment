from django.conf.urls import url
from . import views

app_name = 'conferance'

urlpatterns = [
    url(r'^$', views.list, name='list'),#列出所有会议室
    url(r'^(?P<id>[0-9]+)/$', views.appointment, name='appointment'),#列出预约情况
    url(r'^logi/$', views.logi, name='logi'),
    url(r'^logo/$', views.logo, name='logo'),
    url(r'^register/$', views.register, name='register'),
    url(r'^(?P<id>[0-9]+)/add/$', views.add, name='add'),
    url(r'^(?P<room_id>[0-9]+)/(?P<order_id>[0-9]+)/delete/$', views.delete, name='delete'),
]