from django.forms.widgets import DateInput
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.list import ListView
from django.utils.text import slugify 
from First.models import Flight
from django.views.generic import DetailView
from django.contrib import messages
from Flightio.settings import TIME_ZONE
from .models import Flight
from .forms import AddSchaduleForm



class schaduleHome(ListView):
    template_name = 'First/schadule.html'
    model = Flight #return all of class
    queryset = Flight.objects.filter() #object_list
    context_object_name = 'Flight' 
    ordering = ['-created']

def DetailFlight(request,flight_id):
    flight = get_object_or_404(Flight,pk=flight_id)
    
    return render(request,'First/detail_schadule.html',{'flight':flight})


def add_Schadule(request):    
    if request.method == 'POST':
        form = AddSchaduleForm(request.POST)
        if form.is_valid():
            new_schadule = form.save(commit=False)
            new_schadule.slug = slugify(f"{form.cleaned_data['Flight_Origin']}-{form.cleaned_data['Flight_Distination']}-{form.cleaned_data['Flight_Airline']}-{form.cleaned_data['Flight_Nomber']}-{form.cleaned_data['Flight_Date']}")            
            
            new_schadule.save()
            messages.success(request, 'submited')
            return redirect('first:index')
        else:
            messages.warning(request, 'ridi')

    else:
        form = AddSchaduleForm()
    return render(request,'First/add_Schadule.html', {'form':form} )