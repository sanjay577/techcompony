from django.urls import path
from .import views

urlpatterns = [
    #path('index',index),
   path('',views.techOverview,name='techOverview'),
    path('tech-list/', views.ShowAll, name='tech-list'),
    path('tech-detail/<int:pk>/', views.Viewtech, name='tech-detail'),
    path('tech-create/', views.Createtech, name='tech-create'),
   path('tech-update/<int:pk>/', views.updatetech, name='tech-update'),
    path('tech-delete/<int:pk>/', views.deletetech, name='tech-delete'),
   
]