from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def rooms(request):  
    return render(request, 'rooms.html')

@login_required(login_url='login')
def download(request):
    return render(request, 'download.html')







    



