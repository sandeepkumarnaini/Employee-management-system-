from django.urls import path
from . import views

urlpatterns=[
    path('',views.firstview),
    path('hi/',views.secondview)
]