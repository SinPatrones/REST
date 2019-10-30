from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from userConfirmation import views
from .views import *

urlpatterns = [
    path('users/', views.usuario_list),
    path('users/<int:pk>/',views.usuario_detail),
    path('nUsers/',views.user_list),
    path('nUsers/<pk>/',views.user_detail),
    path('confirmPass/',views.confirmPass),
    path('uploadImg/',views.uploadImg),
    #path('', FileUploadView.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
