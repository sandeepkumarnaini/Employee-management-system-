from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('getempviewset',views.firstviewset,basename='getempviewset')

urlpatterns=[
    path('',views.apiview),
    path('get/',views.viewapi),
    path('modify/<int:pk>/',views.modifyapi),
    path('register/',views.register),
    path('login/',obtain_auth_token),
    path('classapi/',views.Firstapiview.as_view()),
    path('classgenericlist/',views.Firstgenericview.as_view()),
    path('listcreateapiview/',views.listcreateapiview.as_view()),
    path('fud/<int:pk>/',views.fetchupdatedelete.as_view())
    
]

urlpatterns+=router.urls