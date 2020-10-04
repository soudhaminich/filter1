from django.conf.urls import url
from . import views


urlpatterns = [
    url('',views.home,name='home'),
    # url('',views.TicketListView.as_view(),name='home'),
    url('ticket_create', views.ticket_create,name='ticket_create') 
         
         
]
   