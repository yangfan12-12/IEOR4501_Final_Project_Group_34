from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_view),
    path('map/',views.map),
    path('sightings/',views.list),
    path('sightings/stats/',views.stats),
    path('sightings/add/',views.add),
    path('sightings/<Unique_Squirrel_Id>/',views.update),
]
