from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns=[
    url(r'^home/$', views.home, name='home'),
    url(r'^$',views.signup, name='signup'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^upload/$', views.upload_image, name='upload_image')
]