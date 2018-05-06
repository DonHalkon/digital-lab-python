from django.shortcuts import render
from django.views import generic

from .models import Compound


# Create your views here.
def index(request):
    return render(request, 'digitallab/index.html')


def edit_compound(request):
    return render(request, 'digitallab/edit-compound.html')


def save_compound(request):
    jmeFile = request.POST['jmeFile']
    cid = request.POST['cid']
    name = request.POST['name']
    formula = request.POST['formula']
    IUPAC_Name = request.POST['IUPAC Name']
    if len(name) == 0:
        name = IUPAC_Name
    Compound(shortName=name, iupacName=IUPAC_Name, molecularFormula=formula, structure=jmeFile, cid=cid).save()
    return render(request, 'digitallab/view-compounds.html', {'compounds_list': Compound.objects.order_by('-id')})


def reagents(request):
    return render(request, 'digitallab/view-reagents.html')


def edit_reagents(request):
    return render(request, 'digitallab/add-reagent.html')


def reagent_locations(request):
    return render(request, 'digitallab/view-reagentlocations.html')


def edit_reagent_location(request):
    return render(request, 'digitallab/add-reagentlocation.html')

class ReagentsView(generic.ListView):
    template_name = 'digitallab/view-reagents.html'
    context_object_name = 'reagents_list'

    def get_queryset(self):
        return

class CompoundView(generic.ListView):
    template_name = 'digitallab/view-compounds.html'
    context_object_name = 'compounds_list'

    def get_queryset(self):
        return Compound.objects.order_by('-id')
