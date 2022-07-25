from multiprocessing import context
from django.shortcuts import render
from django.http import JsonResponse
from .models import room
from django.contrib.auth.decorators import login_required

# Create your views here.


def rooms(request):  
    lists = room.objects.all()
    return render(request, 'rooms.html',
                    {'lists': lists}) 


def reserve(request):
    return render(request, 'reserve.html')







    



