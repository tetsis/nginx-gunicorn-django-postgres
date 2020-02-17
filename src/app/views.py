from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from model.models import Table
from django.conf import settings

def index(request):
    rows = Table.objects.all()
    access_time_str_list_rdb = []
    for row in rows:
        access_time_str_list_rdb.append(row.access_time.strftime('%Y/%m/%d %H:%M:%S'))

    context = {
        'access_time_str_list_rdb': access_time_str_list_rdb
    }
    return render(request, 'index.html', context)

def save_rdb(request):
    new_table = Table(access_time=timezone.now())
    new_table.save()
    return redirect('index')