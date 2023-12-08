from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('corporate',views.corporate,name='corporate'),
    path('wedding',views.wedding,name='wedding'),
    path('birthday',views.birthday,name='birthday'),
]