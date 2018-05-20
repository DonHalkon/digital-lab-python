from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'digitallab'
urlpatterns = [
    path('', TemplateView.as_view(template_name='digitallab/index.html')),
    path('compounds/view-compounds', views.CompoundView.as_view()),
    path('compounds/edit-compound', views.edit_compound),
    path('compounds/save-compound', views.save_compound),
    path('reagents/view-reagents', views.ReagentsView.as_view()),
    path('reagents/add-reagent', views.edit_reagents),
    path('reagentlocations/view-reagentlocations', views.reagent_locations),
    path('reagentlocations/save', views.reagent_locations),
    path('reagentlocations/add-reagentlocation', views.edit_reagent_location),
]
