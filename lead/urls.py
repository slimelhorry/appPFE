from django.urls import path
from . import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="lead"),
    #path('search-lead', csrf_exempt(views.search_lead), name="search_lead"),
    path('stats', views.stats_view,
         name="stats"),
    path('export_csv', views.export_csv,
         name="export-csv")
]
