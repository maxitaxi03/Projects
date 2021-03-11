from django.shortcuts import render
from django.http import HttpResponse
from .models import List

# Create your views here.
def index(request):
    return HttpResponse("Hey there it is I")

def todo(request):
    context = {
        'lists': List.objects.all()
    }
    print(request.GET)
    print(request.POST)
    return render(request, "list/index.html")