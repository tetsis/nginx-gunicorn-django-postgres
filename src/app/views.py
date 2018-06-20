from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from model.models import Table

def index(request):
    rows = Table.objects.all()
    context = {
        'rows': rows
    }
    return render(request, 'index.html', context)

def save(request):
    new_table = Table(access_time=timezone.now())
    new_table.save()
    return redirect('index')
