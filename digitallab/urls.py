from django.views.generic import TemplateView
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='digitallab/index.html'), name='index'),
    url(r'^compounds/view-compounds$', views.CompoundView.as_view(), name='view-compounds'),
    url(r'^compounds/add-compound$', views.add_compound, name='add-compound'),
    url(r'^reagents/view-reagents$', views.ReagentsView.as_view(), name='view-reagents'),
    url(r'^reagents/add-reagent$', views.add_reagent, name='add-reagent'),
    url(r'^reagentlocations/view-reagentlocations$', views.reagent_locations, name='view-reagentlocations'),
    url(r'^reagentlocations/add-reagentlocation$', views.add_reagent_location, name='add-reagentlocation'),
]
