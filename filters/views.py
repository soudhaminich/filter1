from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import Ticket
from django.views.generic import ListView
from .filters import TicketFilter

# class TicketListView(ListView):
#     model = Ticket
#     template_name = 'filters/ticket_create.html'
    

                    
#     def get_context_data(self,**kwargs): 

     
        
#         context=super().get_context_data(**kwargs)
#         context['filter']=TicketFilter(self.request.GET,queryset=self.get_queryset())
#         return context             
def home(request):
    
    ticketsdetails = Ticket.objects.all()
    # ts=ticketsdetails.order_by.all()
    myfilter=TicketFilter(request.GET,queryset=ticketsdetails)
    ticketsdetails=myfilter.qs
    # t=Ticket.objects.get(id=pk)
    count=Ticket.objects.all().count()
    
    
    stu = {
    "tickets": ticketsdetails,
    "myfilter":myfilter,
    "count":count,
    
    }
   
    
    return render(request,"filters/home.html", stu)



    # total_tickets = ticketsdetails.count()
    # 
    # context = {'ticketsdetails':ticketsdetails, 'tickets':tickets,'total_tickets':total_tickets,'myfilter':myfilter
    # }
    # return render(request,'filters/home.html') 

def ticket_create(request):
    
        form_class = TicketForm 
        if request.method == 'POST':
            form = TicketForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('ticket_create')
        else:
            form = TicketForm()
        return render(request,
                     'filters/ticket_create.html',
                    {
                        'form': form
                    })