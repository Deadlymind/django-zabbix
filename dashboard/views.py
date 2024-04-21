from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ticket.models import Ticket

from django.shortcuts import render

@login_required
def engineer_dashboard(request):
    return render(request, 'dashboard/engineer_dashboard.html')
 
def customer_dashboard(request):
    return render(request, 'dashboard/customer_dashboard.html')
def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')

def dashboard(request):
    if request.user.is_authenticated: 
        if request.user.is_customer:
            tickets = Ticket.objects.filter(customer=request.user).count
            active_tickets = Ticket.objects.filter(customer=request.user, is_resolved=False).count
            closed_tickets = Ticket.objects.filter(customer=request.user, is_resolved=True).count
            context = {
                'tickets': tickets,
                'active_tickets': active_tickets,
                'closed_tickets': closed_tickets
            }
            return render(request, 'dashboard/dashboard.html', context)
        elif request.user.is_engineer:
            tickets = Ticket.objects.filter(engineer=request.user).count
            active_tickets = Ticket.objects.filter(engineer=request.user, is_resolved=False).count
            closed_tickets = Ticket.objects.filter(engineer=request.user, is_resolved=True).count
            context = {
                'tickets': tickets, 'active_tickets': active_tickets,
                'closed_tickets': closed_tickets
            }
            return render(request, 'dashboard/dashboard.html', context)
        elif request.user.is_superuser:
            return render(request, 'dashboard/dashboard.html')
    else:
        
        return redirect('login') 

    
    
