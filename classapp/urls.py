from. import views
from django.urls import path


urlpatterns=[
    path('addition/',views.Firstclassview.as_view()),
    path('multi/',views.Secondclassview.as_view()),
    path('insert/',views.Insertview.as_view()),
    path('select/',views.selectview.as_view()),
    path('update/<int:pk>',views.empupdateview.as_view())
]