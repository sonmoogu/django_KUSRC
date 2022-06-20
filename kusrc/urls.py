from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('1-1', views.one_one, name='1-1'),
    path('1-2', views.one_two, name='1-2'),
    path('2-1', views.two_one, name='2-1'),
    path('2-2', views.two_two, name='2-2'),
    path('2-3', views.two_three, name='2-3'),
    path('5-1', views.five_one, name='5-1'),
]