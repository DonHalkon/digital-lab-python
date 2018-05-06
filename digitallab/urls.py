from django.urls import path

from . import views

app_name = 'digitallab'
urlpatterns = [
    path('', views.index, name='index'),
    path('compounds/view-compounds', views.CompoundView.as_view()),
    path('compounds/edit-compound', views.edit_compound, name='edit_compound'),
    path('compounds/save-compound', views.save_compound, name='save-compound'),
    path('reagents/view-reagents', views.reagents, name=''),
    path('reagents/add-reagent', views.edit_reagents, name=''),
    path('reagentlocations/view-reagentlocations', views.reagent_locations, name=''),
    path('reagentlocations/add-reagentlocation', views.edit_reagent_location, name=''),
]
