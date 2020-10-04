from django.conf.urls import url
from . import views
from django.urls import path,include


urlpatterns = [
    path('',views.home,name='home'),
    
    path("ticket_create", views.ticket_create,name='ticket_create') 
         
         
]
   