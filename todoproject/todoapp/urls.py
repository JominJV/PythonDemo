from . import views
from django.urls import path, include

urlpatterns = [

    path('',views.index,name='index'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.Taskdetail.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Taskupdate.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Taskdelete.as_view(),name='cbvdelete'),
]
