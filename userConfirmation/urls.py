from django.urls import path
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.usuario_list),
    path('users/<int:pk>/', views.usuario_detail),
    path('nUsers/', views.user_list),
    path('nUsers/<pk>/', views.user_detail),
    path('confirmPass/', views.confirmPass),
    path('confirmInventario/', views.confirmInventario),
    path('inventario/',views.inventario_list),
    #path('upload-img/', views.UploadImg.as_view()),
    #path('', FileUploadView.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
