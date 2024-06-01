from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/<int:pk>/', views.result, name='result'),
    path('playtime/', views.find_dota_playtime, name='playtime'),
    path('uninstall/', views.uninstall_dota, name='uninstall')
]