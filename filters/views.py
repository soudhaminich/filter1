from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import Ticket
from django.views.generic import ListView
from .filters import TicketFilter
            
def home(request):
    
    ticketsdetails = Ticket.objects.all()
    myfilter=TicketFilter(request.GET,queryset=ticketsdetails)
    ticketsdetails=myfilter.qs
    count=Ticket.objects.all().count()
    context = {
    "tickets": ticketsdetails,
    "myfilter":myfilter,
    "count":count,
    }
    return render(request,"filters/home.html", context)



    

def ticket_create(request):
    
    form_class = TicketForm 
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ticket_create')
    else:
        form = TicketForm()
    return render(request,'filters/ticket_create.html', {'form': form })
                    
                     
                        
                   