from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='segmentation-index'),
    path('predictions/', views.predictions, name='segmentation-predictions'),
]
