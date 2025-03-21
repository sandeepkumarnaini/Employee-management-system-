from django.urls import path
from . import views

urlpatterns=[
    path('insert/',views.dbprocess),
    path('select/',views.selectdb,name='selectempurl'),
    #path('update/',views.updatedb,name='update1'),
    #path('update2/',views.updatedb2,name='update2'),
    path('update/<int:eno>',views.updatedb,name='updateempurl'),
    path('delete/<int:eno>',views.deletedb,name='deleteempurl')
]