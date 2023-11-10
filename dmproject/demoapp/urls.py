from . import views
from django.urls import path

urlpatterns = [

    path('',views.hello,name='hello'),
    # path('add/',views.addition,name='addition')
]
