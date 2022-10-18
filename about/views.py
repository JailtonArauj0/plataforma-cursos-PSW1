from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def sobre(request):
    return render(request, 'sobre.html')