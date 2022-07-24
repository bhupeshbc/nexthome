from django.urls import path
from rooms import views

urlpatterns = [
    path('', views.rooms, name='home'),
    path('download/', views.download, name='download'),
   

]