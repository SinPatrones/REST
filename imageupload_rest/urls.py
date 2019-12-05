from django.conf.urls import include, url
from imageupload_rest import viewsets

urlpatterns = [
    url(r'^upload/$', viewsets.ImageCreateAPIView.as_view()),
]