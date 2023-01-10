from django.contrib import admin
from django.urls import path, include

import todoapp
from . import views

urlpatterns = [
    path('', views.add, name='add'),
    # # path('details', views.details, name='details'),
    # path('delete/<int:tid>/', views.delete, name='delete'),
    # path('update/<int:tid>/', views.update, name='update'),
    path('cbvindex/', views.Tasklistview.as_view(), name='cbvindex'),
    # path('cbvshow/', views.Tasklistview.as_view(), name='cbvshow'),
    path('cbvdetail/<int:pk>/', views.Taskdetailtview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Taskupdatetview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.Taskdeleteview.as_view(), name='cbvdelete'),
]
