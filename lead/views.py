from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import  lead
#from django.contrib import messages
#from django.contrib.auth.models import User
from django.core.paginator import Paginator
import json
from django.http import JsonResponse, HttpResponse
import datetime
import csv 
from django.db.models import Q


@login_required(login_url='/authentication/login')
def index(request):

    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(Industry__istartswith=q) | Q(Website__icontains=q))
        data = lead.objects.filter(multiple_q)
        paginator = Paginator(data, 5)
    else:
        data = lead.objects.all()
        paginator = Paginator(data, 5)


    
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)


    context = {
        'data': data,
        'page_obj': page_obj
    }
    return render(request, 'lead/index.html', context)


def stats_view(request):
    return render(request, 'lead/stats.html')

def export_csv(request):
    response= HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=Data'+\
        str(datetime.datetime.now())+'.csv'
    writer=csv.writer(response)
    writer.writerow(['Website', 'Industry', 'Size', 'Location'])
    Lead = lead.objects.filter()
    for leads in Lead:
        writer.writerow([leads.Website, leads.Industry, leads.Size, leads.Location])
    return response


