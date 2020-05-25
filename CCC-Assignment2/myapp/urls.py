from django.conf.urls import url, include
from myapp import views

urlpatterns = [
    url(r'tweet/get_geodata', views.get_geodata, ),
    url(r'tweet/get_data', views.get_data),
    url(r'tweet/get_combine_data', views.get_combine_data),
    url(r'information/get_info', views.get_information_data),
    url(r'information/send_info', views.send_information_data),
    url(r'^$', views.index)
]
 