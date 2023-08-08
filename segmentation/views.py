from django.shortcuts import render, redirect
from .forms import DataForm

from django.db.models import F
from .models import Data

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('segmentation-predictions')
    else:
        form = DataForm()


    context = {
        'form': form,

    }
    return render(request, 'segmentation/index.html', context)



def predictions(request):
    predicted_cluster = Data.objects.all().order_by('-id')[:4]
    context = {
        'predicted_cluster': predicted_cluster
    }
    return render(request, 'segmentation/predictions.html', context)
