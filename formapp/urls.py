from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.loginform,name='loginurl'),
    path('logout/',views.logoutform,name='logouturl'),
    path('signup/',views.signupform),
    path('addition/',views.addition),
    path('insert/',views.insertform),
    path('select/<int:pno>',views.selectform,name='selecturl'),
    path('detail/<int:eno>',views.detailform,name='detailurl')

]