from django.conf.urls import url
from tankyou import views
from django.urls import path

urlpatterns = [
    path('', views.viewInicio, name='inicio'),
    path('sobre/', views.viewSobrec, name='sobre'),
    path('lancamentos/', views.viewLancamentos, name='lancamentos'),
]
