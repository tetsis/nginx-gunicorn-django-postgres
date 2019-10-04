from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from model.models import Table
from django.conf import settings
from pymongo import MongoClient

def index(request):
    rows = Table.objects.all()
    access_time_str_list_rdb = []
    for row in rows:
        access_time_str_list_rdb.append(row.access_time.strftime('%Y/%m/%d %H:%M:%S'))


    mongo_client = MongoClient("mongodb+srv://" + settings.NOSQL_DATABASE['USER'] + ":" + settings.NOSQL_DATABASE['PASSWORD'] + "@" + settings.NOSQL_DATABASE['HOST'], serverSelectionTimeoutMS=1000)
    db_name = settings.NOSQL_DATABASE['NAME']
    db = mongo_client[db_name]
    collection = db.collection

    access_time_str_list_nosql = []
    for post in collection.find():
        access_time_str_list_nosql.append(post['access_time'])

    context = {
        'access_time_str_list_rdb': access_time_str_list_rdb,
        'access_time_str_list_nosql': access_time_str_list_nosql
    }
    return render(request, 'index.html', context)

def save_rdb(request):
    new_table = Table(access_time=timezone.now())
    new_table.save()
    return redirect('index')

def save_nosql(request):
    mongo_client = MongoClient("mongodb+srv://" + str(settings.NOSQL_DATABASE['USER']) + ":" + str(settings.NOSQL_DATABASE['PASSWORD']) + "@" + str(settings.NOSQL_DATABASE['HOST']), serverSelectionTimeoutMS=1000)
    db_name = settings.NOSQL_DATABASE['NAME']
    db = mongo_client[db_name]
    collection = db.collection
    access_time = timezone.now().strftime('%Y/%m/%d %H:%M:%S')
    collection.insert_one({
        'access_time': access_time
    })

    return redirect('index')
