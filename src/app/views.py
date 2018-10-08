from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from model.models import Table

def index(request):
    rows = Table.objects.all()
    access_time_str_list = []
    for row in rows:
        access_time_str_list.append(row.access_time.strftime('%Y/%m/%d %H:%M:%S'))
    context = {
        'access_time_str_list': access_time_str_list
    }
    return render(request, 'index.html', context)

def save(request):
    new_table = Table(access_time=timezone.now())
    new_table.save()
    return redirect('index')
