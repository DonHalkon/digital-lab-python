from django.shortcuts import render
from django.views import generic

from .models import Compound
from .models import ReagentLocation
from .models import Reagent
from .forms import CompoundForm, ReagentForm, ReagentLocationForm


# Create your views here.
def add_compound(request):
    form = CompoundForm()

    if request.method == 'POST':
        form = CompoundForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'digitallab/view-compounds.html',
                          {'compounds_list': Compound.objects.order_by('-id')})

    return render(request, 'digitallab/edit-compound.html', {'form': form})


def add_reagent(request):
    return render(request, 'digitallab/add-reagent.html')


def reagent_locations(request):
    return render(request, 'digitallab/view-reagentlocations.html',
                  {'reagentlocations_list': ReagentLocation.objects.order_by('-id')})


def add_reagent_location(request):
    form = ReagentLocationForm()
    if request.method == 'POST':
        form = ReagentLocationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'digitallab/view-reagentlocations.html',
                          {'reagentlocations_list': ReagentLocation.objects.order_by('-id')})
    return render(request, 'digitallab/add-reagentlocation.html', {'form': form})


def save_reagent_location(request):
    descr = request.POST['desct']
    ReagentLocation(descr=descr).save()
    return render(request, 'digitallab/view-reagentlocations.html')


class ReagentsView(generic.ListView):
    template_name = 'digitallab/view-reagents.html'
    context_object_name = 'reagents_list'

    def get_queryset(self):
        return ReagentLocation.objects.order_by('-id')


class CompoundView(generic.ListView):
    template_name = 'digitallab/view-compounds.html'
    context_object_name = 'compounds_list'

    def get_queryset(self):
        return Compound.objects.order_by('-id')
