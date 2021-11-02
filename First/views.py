from django.shortcuts import render,get_object_or_404
from django.views.generic.list import ListView

from First.models import Flight
from django.views.generic import DetailView
from .models import Flight



class schaduleHome(ListView):
    template_name = 'First/schadule.html'
    model = Flight #return all of class
    queryset = Flight.objects.filter() #object_list
    context_object_name = 'Flight' 
    ordering = ['-created']

def DetailFlight(request,flight_id):
    flight = get_object_or_404(Flight,pk=flight_id)
    
    return render(request,'First/detail_schadule.html',{'flight':flight})